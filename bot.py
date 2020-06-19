import os

from discord.ext import commands

from dotenv import load_dotenv

extensions = [
	"cogs.General",
	"cogs.Logs",
	"cogs.Roles"
]

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


class MsdBot(commands.Bot):

	def __init__(self):
		super().__init__(command_prefix=".")

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
