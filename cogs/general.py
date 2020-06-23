import time
import discord
from discord.ext import commands
import json


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

	@commands.command()
	async def userinfo(self, ctx, user: discord.Member=None):
		if not user:
			user = ctx.message.author

		output = ""
		for i in user.roles:
			output += i.mention + " "

		if user.color.value == 0:
			color = 16777210
		else:
			color = user.color

		embed=discord.Embed(title=user.name, description=user.mention, color=color, timestamp=ctx.message.created_at)
		embed.set_thumbnail(url=user.avatar_url_as(format="png"))
		embed.add_field(name="Nickname", value=user.display_name, inline=False)
		embed.add_field(name="Joined on", value=user.joined_at.date(), inline=True)
		embed.add_field(name="Status", value=user.status, inline=True)
		embed.add_field(name="Created account on", value=user.created_at.date(), inline=True)
		embed.add_field(name="Roles", value=output, inline=True)
		embed.set_footer(text=f"ID: {user.id}")
		await ctx.send(embed=embed)

	@commands.command()
	async def serverinfo(self, ctx, guild=None):
		if not guild:
			guild = ctx.message.guild
		else:
			print(type(guild))
			guild = self.bot.get_guild(int(guild))

		if guild.owner.color.value == 0:
			color = 16777210
		else:
			color = guild.owner.color

		emojiList = " "
		for i in guild.emojis:
			emojiList += str(i) + " "

		embed=discord.Embed(title=guild.name, description=guild.description, color=color, timestamp=ctx.message.created_at)
		embed.set_thumbnail(url=guild.icon_url_as(format="png"))
		embed.set_image(url=guild.splash_url_as(format="png"))
		embed.add_field(name="Created on", value=guild.created_at.date(), inline=True)
		embed.add_field(name="Members", value=guild.member_count, inline=True)
		embed.add_field(name="Emojis", value=emojiList, inline=True)
		embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
		embed.set_footer(text=f"ID: {guild.id}")
		await ctx.send(embed=embed)

	@commands.command(aliases=['commands', 'allcommands'])
	async def listcommands(self, ctx):
		with open('custom_commands.json', 'r') as f:
			commands = json.load(f)
			output = '```List of custom commands:\n'
			for key in commands:
				output += f'{key}, '
			output += '```'
			await ctx.send(output)

	@commands.command()
	async def roll(self, ctx, pool):
		await ctx.send(f"You rolled a {randint(0, int(pool))}")

	@commands.Cog.listener()
	async def on_message(self, msg):
		if "i-" in msg.content.lower():
			await ctx.send(self.bot.get_user(329538915805691905).mention)

def setup(bot):
	bot.add_cog(General(bot))
