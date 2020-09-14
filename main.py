import random
import asyncio
import aiohttp
import json
import discord
from discord.ext.commands import Bot
from discord.ext import commands
BOT_PREFIX= ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)
@client.command()
async def USD(ctx):
    async with aiohttp.ClientSession() as session:
        html = await session.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
        html2 = await html.text()
        html2 = json.loads(html2)
        await ctx.send("Bitcoin price is: $"+ html2['bpi']['USD']['rate'])
@client.command()
async def JPY(ctx):
    async with aiohttp.ClientSession() as session:
        html = await session.get('https://api.coindesk.com/v1/bpi/currentprice/JPY.json')
        html2 = await html.text()
        html2 = json.loads(html2)
        await ctx.send("Bitcoin price is: ¥"+ html2['bpi']['JPY']['rate'])
@client.command()
async def Time(ctx):
    async with aiohttp.ClientSession() as session:
        html = await session.get('http://worldtimeapi.org/api/ip.json')
        html_2= await html.text()
        html_2= json.loads(html_2)
        await ctx.send(html_2['datetime'])
@client.command()
async def suma(ctx, n1: float, n2: float):
  await ctx.send(n1+n2)
@client.event
async def on_ready():
  Text2 = "Bot en linea."
  Channel = client.get_channel(428654179217571842)
  message = await Channel.send(Text2)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="TEST"))
  up = '\N{THUMBS UP SIGN}'
  await message.add_reaction(up)
@client.command()
async def resta(ctx, n1: float, n2: float):
 await ctx.send(n1-n2)
@client.command()
async def multiplicacion(ctx, n1: float, n2: float):
 await ctx.send(n1*n2)
@client.command()
async def division(ctx, n1: float, n2: float):
 await ctx.send(n1/n2)
@client.command(pass_context=True)
async def a(ctx):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name="Clase A")
  await discord.Member.add_roles(user, role)
@client.command(pass_context=True)
async def c(ctx):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name="Clase C")
  await discord.Member.add_roles(user, role)
@client.command(pass_context=True)
async def cr(ctx):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name="Clase C")
  await discord.Member.remove_roles(user, role)
@client.command(pass_context=True)
async def ar(ctx):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name="Clase A")
  await discord.Member.remove_roles(user, role)
@client.command()
async def roles(ctx):
  texto= "Escribe !a para obtener tu Rol de la Clase A. - Escribe !c para obtener tu Rol de la Clase C."
  await ctx.send(texto)
@client.event
async def on_message(message):
  texto= "El alfredo es un cuck"
  Channel = client.get_channel(428654179217571842)
  if message.content.startswith(texto):
    await Channel.send('Quien mas si no el alfredcuck')
client.run('NzU0MTM4ODgwNjkyOTc3NzY1.X1wYkA.GWOur_tL1PWngEq3_DQYyivXrOs')