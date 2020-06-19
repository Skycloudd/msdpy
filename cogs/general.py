from discord.ext import commands

import datetime


class General(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.start_time = datetime.datetime.utcnow()

	@commands.command(description='Shows the bot’s ping to Discord')
	async def ping(self, ctx):
		await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

	@commands.command(description='Shows Drgrumble\'s game list', aliases=['games'])
	async def gamelist(self, ctx):
		await ctx.send('Drgrumble\'s mobile game list: https://tinyurl.com/y8rzwpst')

	@commands.command(description='Shows how long the bot has been online for')
	async def uptime(self, ctx):
		now = datetime.datetime.utcnow()
		delta = now - self.start_time
		hours, remainder = divmod(int(delta.total_seconds()), 3600)
		minutes, seconds = divmod(remainder, 60)
		days, hours = divmod(hours, 24)
		if days:
			time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
		else:
			time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
		uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
		await ctx.send(f'{self.bot.name} has been up for {uptime_stamp}')


def setup(bot):
	bot.add_cog(General(bot))
