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
  print("El bot esta listo.")
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="TEST"))
@client.command()
async def resta(ctx, n1: float, n2: float):
 await ctx.send(n1-n2)

@client.command()
async def multiplicacion(ctx, n1: float, n2: float):
 await ctx.send(n1*n2)

@client.command()
async def division(ctx, n1: float, n2: float):
 await ctx.send(n1/n2)
@client.event
async def on_ready():
  Channel = client.get_channel(428654179217571842)
  Text = "!Bot linea!"
  await Channel.send(Text)
@client.event
async def on_reaction_add(reaction, user):
    Channel = client.get_channel('428654179217571842')
    if reaction.message.channel.id != Channel
    return
    if reaction.emoji == "🏃":
      Role = discord.utils.get(user.server.roles, name="Azul")
      await client.add_roles(user, Role)
client.run('NzU0MTM4ODgwNjkyOTc3NzY1.X1wYkA.GWOur_tL1PWngEq3_DQYyivXrOs')