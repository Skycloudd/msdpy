import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

client = commands.Bot(command_prefix='.')

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

logchannel_id = 712939118560018442
server_id = 377268230646923265


@client.event
async def on_ready():
	print(f'logged in as {client.user}')


@client.event
async def on_message(msg):
	if msg.author.bot:
		return
	if not msg.author.guild:
		return
	await client.process_commands(msg)


@client.command(description='Shows the bot’s ping to Discord')
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(description='Shows Drgrumble\'s game list', aliases=['gamelist'])
async def games(ctx):
	await ctx.send('Drgrumble\'s mobile game list: https://tinyurl.com/y8rzwpst')


@client.event
async def on_message_delete(msg):
	#   if msg.guild.id != server_id:
	#       return

	channel = client.get_channel(logchannel_id)

	embed = discord.Embed(
		title='Deleted Message',
		color=16777210,
		timestamp=msg.created_at
	)
	embed.add_field(name='User', value=msg.author.mention, inline=True)
	embed.add_field(name='Channel', value=msg.channel.mention, inline=True)
	embed.add_field(name='Message', value=msg.content, inline=False)

	await channel.send(embed=embed)


@client.event
async def on_message_edit(before, after):
	#   if msg.guild.id != server_id:
	#       return

	channel = client.get_channel(logchannel_id)

	# weird TypeError here with the timestamp
	try:
		embed = discord.Embed(
			title='Edited Message',
			color=16777210,
			timestamp=after.edited_at
		)
		embed.add_field(name='User', value=before.author.mention, inline=True)
		embed.add_field(name='Channel', value=before.channel.mention, inline=True)
		embed.add_field(name='Original Message', value=before.content, inline=False)
		embed.add_field(name='New Message', value=after.content, inline=False)

		await channel.send(embed=embed)

	except TypeError:
		print("TypeError in logging")


client.run(token)
