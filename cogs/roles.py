from discord.ext import commands


class Roles(commands.Cog):
	@commands.command()
	async def iosguide(self, ctx):
		user = ctx.author

		iosguide_id = 680299245982449686

		role = ctx.guild.get_role(iosguide_id)

		if role in user.roles:
			await user.remove_roles(role)
			await ctx.send('You are no longer an iOS Guide')
		else:
			await user.add_roles(role)
			await ctx.send("You are now an iOS Guide")

	@commands.command()
	async def androidguide(self, ctx):
		user = ctx.author

		androidguide_id = 680298568841560085

		role = ctx.guild.get_role(androidguide_id)

		if role in user.roles:
			await user.remove_roles(role)
			await ctx.send('You are no longer an Android Guide')
		else:
			await user.add_roles(role)
			await ctx.send("You are now an Android Guide")

	@commands.command()
	async def streamer(self, ctx):
		user = ctx.author

		streamer_id = 680474671480569974

		role = ctx.guild.get_role(streamer_id)

		if role in user.roles:
			await user.remove_roles(role)
			await ctx.send('You are no longer a streamer')
		else:
			await user.add_roles(role)
			await ctx.send("You are now a streamer")

	@commands.command()
	async def developer(self, ctx):
		user = ctx.author

		developer_id = 723564210042437662

		role = ctx.guild.get_role(developer_id)

		if role in user.roles:
			await user.remove_roles(role)
			await ctx.send('You are no longer a developer')
		else:
			await user.add_roles(role)
			await ctx.send("You are now a developer")


def setup(bot):
	bot.add_cog(Roles(bot))
