import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '$')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'yooo thank for joining')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='With People'))
    print('Ready, Freddy') 


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx , user : discord.Member):
    author = ctx.message.author
    Server = ctx.message.server
    await client.ban(user)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx , user : discord.Member):
    author = ctx.message.author
    Server = ctx.message.server
    await client.kick(user)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx , user : discord.Member):
    author = ctx.message.author
    Server = ctx.message.server
    await client.unban(user)



@client.event
async def on_message(message):
    if message.content == '$invite':
        await client.send_message(message.channel,' <@%s> https://discordapp.com/api/oauth2/authorize?client_id=493529797130059798&permissions=8&scope=bot')
    
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('$help'):
        await client.send_message(message.channel,'<@%s> Help is Not A Command Yes Due to delevoper working on me')  
    



@client.event
async def on_message(message):
    if ('heck') in message.content:
       await client.delete_message(message)
    if message.content == 'heck':
        await client.send_message(message.channel,'NO SWEARING ITS A CHRISTIAN SERVER!!!')
    if message.content.startswith('%scoinflip' %(prefix)):'$'
    randomlist = ['heads','tails',]
    await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('%sdiceroll' %(prefix)):'$'
    randomlist = ['1','2','3','4','5','6',]
    await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == prefix +'your_mum_gay':
        await client.send_message(message.channel,' Dude your_mum_gay')
    if message.content == prefix +'creator':
        await client.send_message(message.channel,'I Am Created By Developer: Aj#1636.')
    if message.content == prefix +'hi':
        await client.send_message(message.channel)
    ('hello')
    if message.content == prefix +'help':
        await client.send_message(message.channel,'hey dude my predix is `$`.')    



@client.event
async def on_message(message):
    if message.content == '$ping':
        await client.send_message(message.channel,'pong')
    if message.content == '$img':
        em = discord.Embed(description='Anime cat girl lol')
        em.set_image(url='https://cdn.discordapp.com/attachments/436300751711633410/494223717853822996/tenor.gif')
        await client.send_message(message.channel, embed=em)
    if ('Hello') in message.content:
       await client.delete_message(message)
    if message.content == '$say no u':
        await client.send_message(message.channel,'no u')
    if message.content == '$say aj amzing':
        await client.send_message(message.channel,'aj amzing')
    if message.content == '$say lol':
        await client.send_message(message.channel,'lol')
    if message.content == '$no_u':
        await client.send_message(message.channel,'no u')
    if message.content.startswith('$'):
        randomlist = ["is back", "returns", "is amazing"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('$twlljoke'):
        randomlist = ["your mum is gay", "your dad is lesbian", "your sister mister", "your brother mother"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '$info':
        await client.send_message(message.channel,'idk why you here lol  just kys,,,, type "$help" for some help :) xD')
    if message.content == '$help2':
        await client.send_message(message.channel,'commands are: "$ping", "$img", "$your_mum_gay", "$no_u", "$sovietrussia", "$twlljoke", "$info", "$help"')




client.run('NDk2MDg2NjI2NDUyMzczNTY0.DpgXEQ.eSFmx8kwxav4j0PdOLZL8ooPsZU')
# Starts the bot.

