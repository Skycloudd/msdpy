from discord.ext import commands


class Roles(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(description='Gives the iOS Guide role')
	async def iosguide(self, ctx):
		user = ctx.author
		iosguide_role = ctx.guild.get_role(int(self.bot.config[str(ctx.guild.id)]["iosguide_role"]))

		if iosguide_role in user.roles:
			await user.remove_roles(iosguide_role)
			await ctx.send('You are no longer an iOS Guide')
		else:
			await user.add_roles(iosguide_role)
			await ctx.send("You are now an iOS Guide")

	@commands.command(description='Gives the Android Guide role')
	async def androidguide(self, ctx):
		user = ctx.author
		androidguide_role = ctx.guild.get_role(int(self.bot.config[str(ctx.guild.id)]["androidguide_role"]))

		if androidguide_role in user.roles:
			await user.remove_roles(androidguide_role)
			await ctx.send('You are no longer an Android Guide')
		else:
			await user.add_roles(androidguide_role)
			await ctx.send("You are now an Android Guide")

	@commands.command(description='Gives the streamer role')
	async def streamer(self, ctx):
		user = ctx.author
		streamer_role = ctx.guild.get_role(int(self.bot.config[str(ctx.guild.id)]["streamer_role"]))

		if streamer_role in user.roles:
			await user.remove_roles(streamer_role)
			await ctx.send('You are no longer a streamer')
		else:
			await user.add_roles(streamer_role)
			await ctx.send("You are now a streamer")

	@commands.command(description='Gives the developer role')
	async def developer(self, ctx):
		user = ctx.author
		dev_role = ctx.guild.get_role(int(self.bot.config[str(ctx.guild.id)]["dev_role"]))

		if dev_role in user.roles:
			await user.remove_roles(dev_role)
			await ctx.send('You are no longer a developer')
		else:
			await user.add_roles(dev_role)
			await ctx.send("You are now a developer")


def setup(bot):
	bot.add_cog(Roles(bot))
