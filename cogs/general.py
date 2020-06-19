import time

from discord.ext import commands


class General(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(description='Shows the bot’s ping to Discord')
	async def ping(self, ctx):
		await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

	@commands.command(description='Shows Drgrumble\'s game list', aliases=['games'])
	async def gamelist(self, ctx):
		await ctx.send('Drgrumble\'s mobile game list: https://tinyurl.com/y8rzwpst')

	@commands.command(description='Shows how long the bot has been online for')
	async def uptime(self, ctx):
		seconds = time.time() - self.bot.start_time
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)
		d, h = divmod(h, 24)
		w, d = divmod(d, 7)
		await ctx.send(f"I've been online for `{int(w)}w : {int(d)}d : {int(h)}h : {int(m)}m : {int(s)}s`")


def setup(bot):
	bot.add_cog(General(bot))
