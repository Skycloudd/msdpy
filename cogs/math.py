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

	@commands.command(description='Converts degrees to radians')
	async def degtorad(self, ctx, x):
		try:
			x = float(x)
		except ValueError:
			return await ctx.send(f'{x} is not a number')

		await ctx.send(f'```360 degrees = 2*pi radians\ndegrees: {x}\nradians: {math.radians(x)}```')

	@commands.command(description='Converts radians to degrees')
	async def radtodeg(self, ctx, x):
		try:
			x = float(x)
		except ValueError:
			return await ctx.send(f'{x} is not a number')

		await ctx.send(f'```pi radians = 180 degrees\nradians: {x}\ndegrees: {math.degrees(x)}```')


def setup(bot):
	bot.add_cog(Math(bot))
