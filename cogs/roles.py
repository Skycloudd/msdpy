from discord.ext import commands


class Roles(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(description='Gives the iOS Guide role')
	async def iosguide(self, ctx):
		user = ctx.author
		msd_guild = self.bot.get_guild(377268230646923265)

		iosguide_id = 680299245982449686

		role = msd_guild.get_role(iosguide_id)

		if role in user.roles:
			await user.remove_roles(role)
			await ctx.send('You are no longer an iOS Guide')
		else:
			await user.add_roles(role)
			await ctx.send("You are now an iOS Guide")

	@commands.command(description='Gives the Android Guide role')
	async def androidguide(self, ctx):
		user = ctx.author
		msd_guild = self.bot.get_guild(377268230646923265)

		androidguide_id = 680298568841560085

		role = msd_guild.get_role(androidguide_id)

		if role in user.roles:
			await user.remove_roles(role)
			await ctx.send('You are no longer an Android Guide')
		else:
			await user.add_roles(role)
			await ctx.send("You are now an Android Guide")

	@commands.command(description='Gives the streamer role')
	async def streamer(self, ctx):
		user = ctx.author
		msd_guild = self.bot.get_guild(377268230646923265)

		streamer_id = 680474671480569974

		role = msd_guild.get_role(streamer_id)

		if role in user.roles:
			await user.remove_roles(role)
			await ctx.send('You are no longer a streamer')
		else:
			await user.add_roles(role)
			await ctx.send("You are now a streamer")

	@commands.command(description='Gives the developer role')
	async def developer(self, ctx):
		user = ctx.author
		msd_guild = self.bot.get_guild(377268230646923265)

		developer_id = 723564210042437662

		role = msd_guild.get_role(developer_id)

		if role in user.roles:
			await user.remove_roles(role)
			await ctx.send('You are no longer a developer')
		else:
			await user.add_roles(role)
			await ctx.send("You are now a developer")


def setup(bot):
	bot.add_cog(Roles(bot))
