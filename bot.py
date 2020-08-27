import os
import time
import logging
import json
import aiohttp

import discord
from discord.ext import commands

from dotenv import load_dotenv

extensions = [
	"cogs.player",
	"cogs.general",
	"cogs.logs",
	#"cogs.roles",
	"cogs.admin",
	"cogs.math",
	"cogs.eval"
]

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

start = time.time()

def get_prefix(bot, message):
	"""A callable Prefix for our bot. This could be edited to allow per server prefixes."""

	prefixes = ['msd ', 'max ', '?', '!', '@', ';', '.']

	# Check to see if we are outside of a guild. e.g DM's etc.
	# if not message.guild:
	# Only allow ? to be used in DMs
	#   return '?'

	# If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
	return commands.when_mentioned_or(*prefixes)(bot, message)

class MsdBot(commands.Bot):

	def __init__(self):
		super().__init__(command_prefix=get_prefix, case_insensitive=True, allowed_mentions=discord.AllowedMentions(everyone=False, users=True, roles=True))
		self.logger = logging.getLogger('discord')

		self.start_time = start

		for extension in extensions:
			self.load_extension(extension)

		with open('custom_commands.json', 'r') as f:
			self.custom_commands = json.load(f)

		with open('config.json', 'r') as f:
			self.config = json.load(f)
			if not self.config['blacklist']:
				self.config['blacklist'] = []
			config = self.config

		self.session = aiohttp.ClientSession()

		self.current_count = 0

	async def on_ready(self):
		print(f'logged in as {self.user}')

	async def on_message(self, msg):
		if msg.author.bot:
			return
		if not msg.guild:
			return
		if msg.author.id in self.config['blacklist']:
			return
		await self.process_commands(msg)

		try:
			command = msg.content.split()[0]
		except IndexError:
			pass
		try:
			if command in self.custom_commands:
				await msg.channel.send(self.custom_commands[command])
				return
		except:
			return
		if msg.content == str(self.current_count):
			await msg.add_reaction('✅')
			self.current_count += 1

	def run(self):
		super().run(self.config['token'])
