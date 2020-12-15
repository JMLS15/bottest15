import asyncio
import aiohttp
import json
import discord
import datetime as dt
from discord.ext.commands import Bot
from discord.ext import commands
BOT_PREFIX= ("?")
client = Bot(command_prefix=BOT_PREFIX)
Channel2 = client.get_channel(428654179217571842)
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Bot prefix is ?"))
  Text2 = "Bot en linea."
  print("Bot en linea.")
  Channel = client.get_channel(754175437550387282)
  message = await Channel.send(Text2)
  up = '\N{THUMBS UP SIGN}'
  await message.add_reaction(up)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content=="HolaF":
        await message.channel.send("Hola!!!")
    await client.process_commands(message)
@client.listen()
async def on_message(message):
    up1='\N{THUMBS UP SIGN}'
    if message.content=="Hola":
        await message.add_reaction(up1)
    if message.content=="El alfredo es un coke":
        await message.add_reaction(up1)
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
async def suma(ctx, n1: int, n2: int):
  await ctx.send(n1+n2)
@client.command()
async def operacion(ctx):
  operaciones=str(eval(ctx))
  await ctx.send("El resultado de las operaciones es: "+operaciones)
@client.command(pass_context=True)
async def a(ctx):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name="Clase A")
  await discord.Member.add_roles(user, role)
  await ctx.send(ctx.message.author.mention+" se te ha asignado a la Clase A Satisfatoriamente.")
@client.command(pass_context=True)
async def c(ctx):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name="Clase C")
  await discord.Member.add_roles(user, role)
  await ctx.send(ctx.message.author.mention+" se te ha asignado a la Clase C Satisfatoriamente.")
@client.command(pass_context=True)
async def cr(ctx):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name="Clase C")
  await discord.Member.remove_roles(user, role)
  await ctx.send(ctx.message.author.mention+" se te ha removido de la Clase C Satisfatoriamente.")
@client.command(pass_context=True)
async def ar(ctx):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name="Clase A")
  await discord.Member.remove_roles(user, role)
  await ctx.send(ctx.message.author.mention+" se te ha removido de la Clase A Satisfatoriamente.")
@client.command()
async def roles(ctx):
  texto= "Escribe !a para obtener tu Rol de la Clase A. - Escribe !c para obtener tu Rol de la Clase C."
  await ctx.send(texto)
client.run('NzU0MTM4ODgwNjkyOTc3NzY1.X1wYkA.y4RLdZIcpCLmxYcgaDWD240NOmk')
