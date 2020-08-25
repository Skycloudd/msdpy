import time
import discord
from discord.ext import commands
import json
from random import randint


class General(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		# sky server, sky
		self.findseed_whitelist = [672045035797348352, 329538915805691905]

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
		#embed.add_field(name="Emojis", value=emojiList, inline=True)
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
	@commands.cooldown(1, 20, commands.BucketType.user)
	async def roll(self, ctx, pool):
		await ctx.send(
			f'You rolled a {randint(0, int(pool))}')

	@roll.error
	async def roll_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"{ctx.author.mention}, you have to wait {round(error.retry_after, 3)} seconds before using this again")

	@commands.command()
	async def emotes(self, ctx):
		emotes = []
		for emote in self.bot.emojis:
			if emote.available:
				emotes.append(str(emote))

		text = ''
		for i in range(len(emotes)):
			if len(text) + len(str(emotes[i])) > 2000:
				await ctx.send(text)
				text = ''
			text += str(emotes[i])
		await ctx.send(text)

	@commands.command(aliases=['nasa', 'apod'])
	async def nasapic(self, ctx):
		apikey = self.bot.config['nasa_apikey']
		url = f'https://api.nasa.gov/planetary/apod?api_key={apikey}'

		async with self.bot.session.get(url) as r:
			response = json.loads(await r.text())

			embed = discord.Embed(
				title=response["title"],
				colour=discord.Colour(discord.colour.Colour.orange().value),
				url=response["hdurl"],
				description=response["explanation"]
			)

			embed.set_image(url=response["hdurl"])
			embed.set_footer(text=f'copyright: {response["copyright"]}')

			await ctx.send(embed=embed)

	@commands.cooldown(1, 20, commands.BucketType.user)
	@commands.command()
	async def findseed(self, ctx):
		portal_frames = 12
		total_eyes = 0
		for i in range(portal_frames):
			if randint(0, 100) < 10:
				total_eyes += 1
		try:
			await ctx.send(f'{str(ctx.message.author.mention)} -> your seed is a {total_eyes} eye')
		except discord.Forbidden:
			await ctx.message.add_reaction('👁️')

	# https://gist.github.com/CapClumsy/6128d89a1e842b4e802b3a077d7f98a5
	@findseed.after_invoke
	async def reset_cooldown(self, ctx):
		for e in self.findseed_whitelist:
			# to whitelist a person:
			if e == ctx.author.id:
				self.findseed.reset_cooldown(ctx)

			# to whitelist a channel:
			if e == ctx.message.channel.id:
				self.findseed.reset_cooldown(ctx)

			# to whitelist a guild/server:
			if e == ctx.message.guild.id:
				self.findseed.reset_cooldown(ctx)

			# to whitelist a role:
			if e in [role.id for role in ctx.author.roles]:
				self.findseed.reset_cooldown(ctx)

	@findseed.error
	async def findseed_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(
				f'{ctx.author.mention}, you have to wait {round(error.retry_after, 3)} seconds before using this again')

	@commands.Cog.listener()
	async def on_message(self, msg):
		if msg.author.bot:
			return
		if not msg.guild:
			return
		if msg.author.id in self.bot.config['blacklist']:
			return
		if "i-" in msg.content.lower():
			try:
				await msg.channel.send(self.bot.get_user(329538915805691905).mention)
			except discord.Forbidden:
				try:
					await msg.add_reaction('😐')
				except discord.Forbidden:
					pass
		if "pog" in msg.content.lower():
			pog_emote = await msg.guild.fetch_emoji(int(self.bot.config[str(msg.guild.id)]["pog_emote_id"]))
			try:
				await msg.channel.send(pog_emote)
			except discord.Forbidden:
				try:
					await msg.add_reaction(pog_emote)
				except discord.Forbidden:
					pass


def setup(bot):
	bot.add_cog(General(bot))
