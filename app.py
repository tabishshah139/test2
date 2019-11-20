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
status = cycle(['+help', '+stock', '+spotify', '+origin', '+netflix', '+hulu', '+minecraft', '+nitro', '+mailaccess'])

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

    if message.content.startswith('+help'):

        await message.author.send("Introducing TABISH SHAH BOT")
        await message.author.send("You Can Invite This Bot To Your Server +invite")
        await message.author.send("Official Server https://discord.gg/SzffkfK")
        await message.author.send("You Can Check Available Stock In BOT +stock")
        await message.channel.send("```Help Sended In``` **DMs**! :white_check_mark:")
 



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

    if message.content.startswith('+mailaccess'):
        randomlist = ['   ']
        await message.author.send("Note: We have added Little Advertisement.")
        await message.author.send(" You Can Get more than 50 Accounts by seeing advertisement 1 time. ")
        await message.author.send("Watch Advertisement and Recieve Alot Accounts Thank You.")
        await message.author.send(" :one: ( https://link-to.net/41622/mailacc1 ) 100x Mail Access Accounts list 1. ")
        await message.author.send(" :two: ( https://link-to.net/41622/mail2 ) 100x Mail Access Accounts list 2.")
        await message.author.send("  :three: ( https://link-to.net/41622/mailaccu3 ) 150x Mail Access Accounts list 3. ")
        await message.author.send("  :four: ( https://link-to.net/41622/mailaccc4 ) 150x Mail Access Accounts list 4 ")
        await message.author.send(" Join Tabish Gen Official CM** https://discord.gg/SzffkfK ")  
        msg = ' ' + author + '. Mail Access Accounts : '
        await message.author.send(msg + (random.choice(randomlist)))


    if message.content.startswith('+minecraft'):
        randomlist = ['']
        await message.author.send("Note: We have added Little Advertisement.")
        await message.author.send(" You Can Get more than 50 Accounts by seeing advertisement 1 time. ")
        await message.author.send("Watch Advertisement and Recieve Alot Accounts Thank You.")
        await message.author.send(" :one: ( https://up-to-down.net/41622/mineas1 ) 120x Minecraft Accounts list 1. ")
        await message.author.send(":two: ( https://up-to-down.net/41622/minesd2 ) 120x Minecraft Accounts list 2.")
        await message.author.send(" :three: ( https://up-to-down.net/41622/minets3 ) 149x Minecraft Accounts list 3 ")
        await message.author.send(" Join Tabish Gen Official CM** https://discord.gg/SzffkfK ")  
        msg = ' ' + author + '. Minecraft Accounts : '
        await message.author.send(msg + (random.choice(randomlist)))


    if message.content.startswith('+hulu'):
        randomlist = ['']

        await message.author.send("Note: We have added Little Advertisement.")
        await message.author.send(" You Can Get more than 50 Accounts by seeing advertisement 1 time. ")
        await message.author.send("Watch Advertisement and Recieve Alot Accounts Thank You.")
        await message.author.send(" :one: ( https://link-to.net/41622/hulu11 ) 1000x Hulu Accounts list 1. ")
        await message.author.send(":two: ( https://link-to.net/41622/hul2 ) 1000x Hulu Accounts list 2.")
        await message.author.send(" :three: ( https://link-to.net/41622/hulu33 ) 1111x Hulu Accounts list 3 ")        
        await message.author.send(" Official Server https://discord.gg/SzffkfK ")
        msg = ' ' + author + '. Hulu Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+origin'):
        randomlist = ['  ']
        await message.author.send("Note: We have added Little Advertisement.")
        await message.author.send(" You Can Get more more than 50 Accounts by seeing advertisement 1 time. ")
        await message.author.send("Watch Advertisement and Recieve Alot Accounts Thank You.")
        await message.author.send(":one: ( https://up-to-down.net/41622/origin101 ) 74x Origin Accounts list 1. ")   
        await message.author.send(" :two: ( https://link-to.net/41622/origi2 ) 60x Origin Accounts list 2")
        await message.author.send(" Join Tabish Gen Official CM** https://discord.gg/SzffkfK ")        
        msg = ' ' + author + '. Origin Accounts : '
        await message.author.send(msg + (random.choice(randomlist)))



    if message.content.startswith('+nitro'):
        randomlist = [' ']
        await message.author.send("Note: We have added Little Advertisement.")
        await message.author.send("You Can Get more than 50 Accounts by seeing advertisement 1 time.")
        await message.author.send("Watch Advertisement and Recieve Alot Accounts Thank You.")
        await message.author.send(":one: ( https://link-to.net/41622/code1 ) 200x Nitro Codes list 1.")
        await message.author.send(":two: ( https://link-to.net/41622/codes2 ) 200x Nitro Codes list 2.")
        await message.author.send(":three: ( https://link-to.net/41622/coded3 ) 200x Nitro Codes list 3.")
        await message.author.send(":four: ( https://link-to.net/41622/coddes4 ) 240x Nitro Codes list 4")
        await message.author.send(" Join Tabish Gen Official CM** https://discord.gg/SzffkfK ")  
        msg = ' ' + author + '. Nitro Codes : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+crunchyroll'):
        randomlist = [' ']
        await message.author.send("Note: We have added Little Advertisement.")
        await message.author.send("You Can Get more than 50 Accounts by seeing advertisement 1 time .")
        await message.author.send("Watch Advertisement and Recieve Alot Accounts Thank You.")
        await message.author.send(":one: ( https://link-to.net/41622/crunchy1 ). 60x Crunchyroll Accounts list 1")
        await message.author.send(":two: ( https://link-to.net/41622/crunch2 ). 67x Crunchyroll Accounts list 2")
        await message.author.send(" Join Tabish Gen Official CM** https://discord.gg/SzffkfK ") 
        msg = ' ' + author + '. Crunchyroll Accounts : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+netflix'):
        randomlist = ['      ']
        await message.author.send("Note: We have added Little Advertisement.")
        
        await message.author.send("You Can Get more than 50 Accounts by seeing advertisement 1 time.")
        await message.author.send(" Watch Advertisement and Recieve Alot Accounts Thank You.")
        await message.author.send(":one: ( https://link-to.net/41622/netflixe ) 200x Netflix Accounts list 1.")
        await message.author.send(":two: ( https://link-to.net/41622/netfl2 ) 200x Netflix Accounts list 2.")
        await message.author.send(":three: ( https://link-to.net/41622/netfli3 ) 200x Netflix Accounts list 3.")
        await message.author.send(":four: ( https://link-to.net/41622/netfliee4 ) 260x Netflix Accounts list 4.")
        await message.author.send(":five: ( https://link-to.net/41622/nefliexx5 ) 303x Netflix Accounts list 5")
        await message.author.send(" Official Server https://discord.gg/SzffkfK ")
        msg = ' ' + author + '. Netflix Accounts : '
        await message.author.send(msg + (random.choice(randomlist)))




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
