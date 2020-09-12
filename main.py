from discord.ext import commands
import discord
import random
import secrets
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='!')
channel = bot.get_channel(754175437550387282)
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
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Alfredcuck"))
    print("Logged in as " + bot.user.name)
@bot.event
async def on_message(message):
    if 'eri god?' in message.content.lower():
        await message.channel.send('Si soy')
@bot.command()
async def commands(ctx):
    msg="Commands available:
    abofetea razon
    suma numero1 numero2
    resta numero1 numero2
    multiplicacion numero1 numero2
    division numero1 numero2
    suma_palabras palabra1 a combinar palabra2 a combinar
    repite sentencia a repetir"
    await ctx.send(msg)
bot.run('NzU0MTM4ODgwNjkyOTc3NzY1.X1wYkA.GWOur_tL1PWngEq3_DQYyivXrOs')
