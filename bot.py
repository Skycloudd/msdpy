import os
import time

from discord.ext import commands

from dotenv import load_dotenv

extensions = [
	"cogs.general",
	"cogs.logs",
	"cogs.roles"
]

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

start = time.time()

class MsdBot(commands.Bot):

	def __init__(self):
		super().__init__(command_prefix=".")

		self.start_time = start

		for extension in extensions:
			self.load_extension(extension)

	async def on_ready(self):
		print(f'logged in as {self.user}')

	async def on_message(self, msg):
		if msg.author.bot:
			return
		if not msg.author.guild:
			return
		await self.process_commands(msg)

	def run(self):
		super().run(token)
