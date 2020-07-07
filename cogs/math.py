from discord.ext import commands
import math


class Math(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(description='Calculates the sine of an angle in radians or degrees')
	async def sin(self, ctx, x, rad_deg):
		try:
			x = float(x)
		except ValueError:
			return ctx.send(f'{x} is not a number')

		if rad_deg == 'rad':
			return ctx.send(f'sin({x}) = {math.sin(x)}')
		elif rad_deg == 'deg':
			return ctx.send(f'sin({x}) = {math.degrees(math.sin(x))}')

		elif rad_deg != 'rad' and rad_deg != 'deg':
			return ctx.send('second argument must be either \'rad\' or \'deg\'')


def setup(bot):
	bot.add_cog(Math(bot))
