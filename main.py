from discord.ext import commands
import discord
import random
bot = discord.Client()
bot = commands.Bot(command_prefix='!')

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.channel.members)
        return '{0.author} ha abofeteado a {1} por *{2}*'.format(ctx, to_slap, argument)
@bot.command()
async def abofetea(ctx, *, reason: Slapper):
    await ctx.send(reason)
@bot.command()
async def suma(ctx, n1: float, n2: float):
    await ctx.send(n1+n2)

@bot.command()
async def resta(ctx, n1: float, n2: float):
    await ctx.send(n1-n2)

@bot.command()
async def multiplicacion(ctx, n1: float, n2: float):
    await ctx.send(n1*n2)

@bot.command()
async def division(ctx, n1: float, n2: float):
    await ctx.send(n1/n2)
@bot.command()
async def repite(ctx, arg):
    await ctx.send(arg)
@bot.command()
async def suma_palabras(ctx, n1, n2):
    await ctx.send(n1+n2)
bot.run('NzU0MTM4ODgwNjkyOTc3NzY1.X1wYkA.GWOur_tL1PWngEq3_DQYyivXrOs')
