import discord
from discord.ext import commands


class Logs(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message_delete(self, msg):

		channel = self.bot.get_channel(712939118560018442)

		embed = discord.Embed(
			title='Deleted Message',
			color=16777210,
			timestamp=msg.created_at
		)
		embed.add_field(name='User', value=msg.author.mention, inline=True)
		embed.add_field(name='Channel', value=msg.channel.mention, inline=True)
		embed.add_field(name='Message', value=msg.content, inline=False)

		await channel.send(embed=embed)

	@commands.Cog.listener()
	async def on_message_edit(self, before, after):

		channel = self.bot.get_channel(712939118560018442)

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


def setup(bot):
	bot.add_cog(Logs(bot))
