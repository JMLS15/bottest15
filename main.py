import random
import asyncio
import aiohttp
import json
import discord
from discord.ext.commands import Bot
from discord.ext import commands
BOT_PREFIX= ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)
global Channel
Channel = client.get_channel(703853970346737715)
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
  Text3 = "Reacciona para obtener un rol."
  Channel = client.get_channel(703853970346737715)
  await Channel.send(Text2)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="TEST"))
  message = await Channel.send(Text3)
  up = '\N{THUMBS UP SIGN}'
  down = '\N{THUMBS DOWN SIGN}'
  await message.add_reaction(up)
  await message.add_reaction(down)
  role = discord.utils.get(Channel.server.roles, name="Azul")
  role2 = discord.utils.get(Channel.server.roles, name="Rojo")
  while True:
    reaction = await message.wait_for_reaction(emoji=up, message=message)
    await message.add_roles(reaction, role)
  while True:
    reaction2 = await message.wait_for_reaction(emoji=down, message=message)
    await message.add_roles(reaction2, role2)
@client.command()
async def resta(ctx, n1: float, n2: float):
 await ctx.send(n1-n2)
@client.command()
async def multiplicacion(ctx, n1: float, n2: float):
 await ctx.send(n1*n2)
@client.command()
async def division(ctx, n1: float, n2: float):
 await ctx.send(n1/n2)
client.run('NzU0MTM4ODgwNjkyOTc3NzY1.X1wYkA.GWOur_tL1PWngEq3_DQYyivXrOs')