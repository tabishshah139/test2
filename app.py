import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
import time
from itertools import cycle
from discord.utils import get
from discord import Game
import os

from discord import Activity, ActivityType


client = commands.Bot(command_prefix='+')
#client = discord.Client()
Clientdiscord = discord.Client()


#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['+help'])

client.remove_command('help')

# this is only for test if bot working
@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

# this lines you can modify  

    if message.content.startswith('+hello'):
        msg = 'Hello python {0.author.mention}'.format(message)
        await message.author.send(msg)


    if message.content.startswith('+invite'):
        await message.author.send("Click To Invite Bot In Your Server https://discordapp.com/api/oauth2/authorize?client_id=619923933109420097&permissions=0&scope=bot")
       


    if message.content.startswith('+spotify'):
        randomlist = ['     ']
        await message.author.send("Note: We have added Little Advertisement.")       
        await message.author.send("You Can Get more than 50 Accounts by seeing advertisement 1 time.")
        await message.author.send("Watch Advertisement and Recieve Alot Accounts Thank You.")
        await message.author.send(":one: ( https://up-to-down.net/41622/spotify1 ) 200x Spotify Accounts list 1.")
        await message.author.send(" :two: ( https://up-to-down.net/41622/Spotify2P ) 200x Spotify Accounts list 2.")
        await message.author.send(":three: ( https://up-to-down.net/41622/spotify3 ) 200x Spotify Accounts list 3.")
        await message.author.send(":four: ( https://up-to-down.net/41622/spotify4 ) 128x Spotify Accounts list 4")
        await message.author.send(" Official Server https://discord.gg/SzffkfK ")
        msg = ' ' + author + '. Spotify Accounts : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+stock'):
        await message.author.send("```Origin: 670 .Hulu: 421 .Spotify: 621 .Fortnite: 1000 .Nordvpn: 444 .Crunchyroll: 272 .Uplay: 300 .Minecraft: 441```")
        await message.author.send("```Available Stocks 17 November```")
        await message.author.send(" Official Server https://discord.gg/SzffkfK ")

                                  

                                  
                                  
                               
                                  
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

@tasks.loop(seconds=5)
async def change_status():
        await client.change_presence(activity=Activity(name=f"{len(client.guilds)} servers!| +help | Members ", 
                                                type=ActivityType.watching))

client.run(os.getenv('BOT_TOKEN'))
