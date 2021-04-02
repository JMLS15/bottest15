import aiohttp
import json
import discord
import os
import asyncio
from discord.ext.commands import Bot
BOT_PREFIX =("?")
client = Bot(command_prefix=BOT_PREFIX)
Channel2 = client.get_channel(428654179217571842)
@client.event
async def on_member_update(before, after):
    n=after.nick
    if n:
        if n.lower().count("jmls15") > 0:
            await after.edit(nick="Hola")
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
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
        await message.add_reaction('👍')
    if message.content=="¿El fernando es pelon?":
        await message.channel.send("sies")
        await message.channel.send('<:okpelon:819468764637954099>')
    if message.content=="El fernando es pelon":
        await message.channel.send("sies")
        await message.channel.send('<:okpelon:819468764637954099>')
    if message.content.startswith('<:AdminPuto:748378662063046688>'):
        await message.add_reaction(okpelon)
        await message.add_reaction('⭕')
        await message.add_reaction('🇰')
        await message.add_reaction('🇵')
        await message.add_reaction('🇪')
        await message.add_reaction('🇮')
        await message.add_reaction(manute)
        await message.add_reaction('🇳')
    await client.process_commands(message)
@client.listen()
async def on_message(message):
    okpelon='<:okpelon:819468764637954099>'
    manute='<:Manute:813289655666606091>'
    if message.author.id==435607040812122122:
        await message.author.edit(nick="Pelon Pelonete Peloncio")
        await message.add_reaction(okpelon)
        await message.add_reaction('⭕')
        await message.add_reaction('🇰')
        await message.add_reaction('🇵')
        await message.add_reaction('🇪')
        await message.add_reaction('🇮')
        await message.add_reaction(manute)
        await message.add_reaction('🇳')
@client.command()
async def shutdown(ctx):
    id=str(ctx.author.id)
    if id == '238762286922072064':
        await ctx.send('Shutting down the bot!')
        await ctx.bot.logout()
    else:
        await ctx.send("You dont have sufficient permmisions to perform this action!")
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
@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
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
async def clear(ctx, amount=None):
    amount2 = int(amount)
    amount2 = amount2+1
    if amount is None:
        await ctx.channel.purge(limit=5)
    elif amount == "all":
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=amount2)
client.run(os.environ['BOT_TOKEN'])
