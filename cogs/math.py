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
			return await ctx.send(f'{x} is not a number')

		if rad_deg == 'rad':
			return await ctx.send(f'sin({x}) = {math.sin(x)} in radians')
		elif rad_deg == 'deg':
			return await ctx.send(f'sin({x}) = {math.degrees(math.sin(x))} in degrees')

		elif rad_deg != 'rad' and rad_deg != 'deg':
			return await ctx.send('second argument must be either \'rad\' or \'deg\'')

	@commands.command(description='Calculates the cosine of an angle in radians or degrees')
	async def cos(self, ctx, x, rad_deg):
		try:
			x = float(x)
		except ValueError:
			return await ctx.send(f'{x} is not a number')

		if rad_deg == 'rad':
			return await ctx.send(f'cos({x}) = {math.cos(x)} in radians')
		elif rad_deg == 'deg':
			return await ctx.send(f'cos({x}) = {math.degrees(math.cos(x))} in degrees')

		elif rad_deg != 'rad' and rad_deg != 'deg':
			return await ctx.send('second argument must be either \'rad\' or \'deg\'')

	@commands.command(description='Calculates the tangent of an angle in radians or degrees')
	async def tan(self, ctx, x, rad_deg):
		try:
			x = float(x)
		except ValueError:
			return await ctx.send(f'{x} is not a number')

		if rad_deg == 'rad':
			return await ctx.send(f'tan({x}) = {math.tan(x)} in radians')
		elif rad_deg == 'deg':
			return await ctx.send(f'tan({x}) = {math.degrees(math.tan(x))} in degrees')

		elif rad_deg != 'rad' and rad_deg != 'deg':
			return await ctx.send('second argument must be either \'rad\' or \'deg\'')


def setup(bot):
	bot.add_cog(Math(bot))
