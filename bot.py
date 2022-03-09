import imp
from multiprocessing.sharedctypes import Value
from pydoc import cli
from tokenize import blank_re
from turtle import color
from typing import Any
import discord
from discord import member
from discord import Client
from discord import message
from django.http import response
from matplotlib.pyplot import title
import requests
import asyncio
import calendar
import json
import datetime
import random
import os
from io import BytesIO
import pyjokes
import randfacts
from time import sleep
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, context
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.commands import Bot
from datetime import date
from googlesearch import search
from torch import rand
import wikipedia
from covid import *
from translate import Translator
from pywikihow import search_wikihow
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math 
from requests import get
import pypokedex
import akinator
import time
import urllib.request
import re
import threading
import aiohttp
from os import getcwd, name
from discord import Intents
from urllib.request import urlopen
from urllib import parse
from urllib import request
import requests
from pyqrcode import QRCode
import pyqrcode
import png

TOKEN="ODk0ODY4NTM2OTA2ODc0OTAw.YVwRRQ.0_Dbg8yIkmU28i7X-GuAL-bu2y8"


intents = Intents.default()
intents.members = True

client = commands.Bot(command_prefix="$", intents=intents)
bot=commands.Bot(command_prefix="!")


   
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json. loads(response.text)
    quote = json_data[0]['q'] +" -" + json_data[0]["a"]
    return(quote)


happy = ["Nice <a:handclap:913756072181891083>", "😀","https://external-preview.redd.it/9U6lgpcvrI9Wj7PRwjPQI2976xQdBLRsSMm2T3n7rp8.gif?s=b273906c7a8393f4c4988cbc328f146fab4e423d"]

bye = ["Bye Bye See you again","👋","https://media1.giphy.com/media/l3V0bpnfbQ3Ygpup2/200.gif"]

lols = ["Ok I am Laughing Master😂",'<a:toohappy:913753294692831243>',"https://c.tenor.com/rXuSDs9lS7IAAAAM/lol.gif"]
                
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

thanks = ['Thanks Master <a:doggodance:913684404788932650>','https://latex-beamer.com/wp-content/uploads/2021/08/Thanks.gif', '🤗']

bruh = ['<a:bruh:913797728453132392>', '<a:bruh:913797728453132392>', 'https://c.tenor.com/FXOSfHN8VCQAAAAM/bruh.gif'
]

kill = ['ok you are dead...RIP <a:devil:913754619992227860>', '☠ Dead', 'https://c.tenor.com/-Xzi-nDUfaEAAAAM/the-dark-knight-heath-ledger.gif']

wassup = ['nothing much <a:sadcry:913755347196448799>', '😎Excellent Going', 'https://c.tenor.com/xNJsCp6sT-oAAAAM/wonderful-jack-donaghy.gif'
]

starter_encouragements = [
  "Cheer up! <a:handclap:913756072181891083>",
  "Hang in there. <a:handclap:913756072181891083>",
  "You are a great person BRO! <a:handclap:913756072181891083>"
]

present = ['https://i.pinimg.com/originals/33/0a/40/330a40815bcac1887d26422a81acf04d.gif', 'Yes I am here', 'Yes Master I am Present 🔥?']

hello = ["Hello! Master <a:goose:913669312395481118>", '😀Hello Master', 'https://user-images.githubusercontent.com/51138087/93663951-39922d00-fa20-11ea-952b-48da7a6e5381.gif']

sorry = ['No Problem <a:handclap:913756072181891083>', 'No problem Master🤗', 'https://c.tenor.com/2fK5bMUEc0UAAAAC/michael-scott-wink.gif']

bad = ['Hey!! Never under-estimate the power of a common chatbot <a:devil:913754619992227860>', '😈Never Under-estimate my power', 'https://c.tenor.com/OpB96eMGV-UAAAAC/anakin-starwars.gif']

what = ['Nothing Sir <a:verified:913758031194521631>','😶Nothing','https://i.pinimg.com/originals/53/fc/2b/53fc2b61e0dc6157543753dd4545c8ae.gif']

cool = ['Excellent <a:handclap:913756072181891083>', '😎','https://media2.giphy.com/media/SVH9y2LQUVVCRcqD7o/giphy.gif']

yay = ['🎉🎊','https://c.tenor.com/Jw0RZGetgwIAAAAC/minions-yay.gif'
]

stop = ['😶Ok😅', '🧐🧐', 'https://c.tenor.com/Fa5GKCxVw3QAAAAC/stop-it-get-some-help.gif']

riddle = [' I’m tall when I’m young, and I’m short when I’m old. What am I?(BUT I WILL NOT REPLY TO WRONG ANSWER ONLY CORRECT ANSWER)', 'What is full of holes but still holds water?(BUT I WILL NOT REPLY TO WRONG ANSWER ONLY CORRECT ANSWER)', 'What can you break, even if you never pick it up or touch it?(BUT I WILL NOT REPLY TO WRONG ANSWER ONLY CORRECT ANSWER)', 'What has many keys but can’t open a single lock?(BUT I WILL NOT REPLY TO WRONG ANSWER ONLY CORRECT ANSWER)']

roast = ['You cant Photoshop Your Ugly Personality🔥','I tried to put myself in your shoes but they were cheap and ugly, just like you', 'https://i.pinimg.com/236x/15/ac/3c/15ac3c82d862e601733e120c32f5ab6d.jpg']

meme = ['https://img.delicious.com.au/WqbvXLhs/del/2016/06/more-the-merrier-31380-2.jpg', 'https://static.mommypoppins.com/styles/image300x250/s3/school_meme_3_0.jpg', 'https://thumbor.granitemedia.com/img/6oz5ttHNU4_zDXBVQHY0AnTYleI=/800x570/filters:format(webp):quality(80)/granite-web-prod/5d/ef/5def5cafcf3243bdab9be14d8427291e.jpeg', 'https://s18670.pcdn.co/wp-content/uploads/When-You-Think-Back-On-This-Last-Semeseter-800x734.png', 'https://bestlifeonline.com/wp-content/uploads/sites/3/2019/07/back-to-school-meme-funny-3.jpg?quality=82&strip=all', 'https://static.abplive.com/wp-content/uploads/sites/2/2021/02/02170724/budget-memes.jpg?impolicy=abp_cdn&imwidth=640', 'https://s4.scoopwhoop.com/anj/feat/941432013.jpg', 'https://static.langimg.com/thumb/msid-67609704,width-680,resizemode-3/viral-meme.jpg', 'https://www.ohyaaro.com/wp-content/uploads/2020/09/exam-funny-memes.png', 'https://pbs.twimg.com/media/Egg-PIVU4AA08xg.png', 'https://meaninginhindi.net/wp-content/uploads/2020/03/funny-memes.jpg']

random2 = ["text or call", "sea or mountain", "online  school or offline school", "Pizza or Burger", "Sports or Study", "Fake or Real", "Friends or Parents", "Brother or Sister", "Whatsapp or Discord","guitar or piano", "train or airplane" ]

wow = ['yup', '😏','https://c.tenor.com/SxBAqOYtH6YAAAAM/amazing-minion.gif']

killed = ["was walking on a road and got hitted by a truck then dead body was found in ocean 'cuz he was on a highway near to ocean lol xD", "was eating a sandwich  and died because there were peanuts in it and he was allergic to it and had no brain so 'he dont know what he was eating lol xD", "was happy with her new cycle which her parents gave her (actually he/she wanted to tease his/her friends with the cycle because his/her friends everyday bring something new to school and become oversmart ,but when he/she showed his/her cycle to his/her friends and tried to be cool ,his/her biggest enemy got a bike there and she died 'cuz the truth is he/ she never can be smart RIP lol xD and that enemy was saaim"]

jokeone = ["Q: What kind of math do owls like? A: Owlgebra", "Q: What type of market should you NEVER take your dog? A: A flea market!", "Q. What do you get when you cross a centipede with a parrot? A. A walkie-talkie!", "Hippo 1: You look like you’re gaining weight. Hippo 2: That’s very hippo-critical of you.", "Q: Why did the baby elephant need a new suitcase for her vacation? A: She only had a little trunk.", "Q. Why are fish so good at watching their weight? A. Because they have lots of scales!", "You would think that taking off a snail's shell would make it move faster, but it actually just makes it more sluggish.", "There's a guy in town who walks around talking to himself using only figurative language. We call him the Village Idiom.", "Headline from the Seattle PostIntelligencer: “Mom Warns Son to ‘Watch Out for Idiots,’ Rear‑Ends His Motorcycle.”", "Guy staring at an ambulance in front of Whole Foods: “Somebody must have accidentally eaten gluten.”"]

stickers = ["aaah.jpg", "ab ayega maza.jpg", "chill maar.jpg", "cryyyyyy.jpg", "good morning.jpg", "good night.jpg", "hah.jpg", "hahahaha.jpg", "hahahaha2.jpg", "happy birthday.jpg", "hmm.jpg", "khali time pass on the phone.jpg", "kiabo ko aag laga de.jpg", "kon mai.jpg", "kya bola beyy.jpg", "lets go.jpg", "maa ki mamta.jpg", "mujhe to ab chakkar aane lage hai.jpg", "namaste.jpg", "om om.jpg", "phoonk.jpg", "really.jpg", "still working.jpg", "thodi hawa aane dey.jpg", "we did it.jpg", "ye kya boldiya.jpg"]

avengers = ['spidey.png', 'spidey2.jpg', 'spidey3.jpg', 'spidey4.jpg', 'spidey5.jpg', 'spidey6.jpg']

def gfg():
    with open(f"not.txt","w") as f:
      f.write(str(f""))

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


@client.command()
async def stats(message):
    embed = discord.Embed(
          title=f"My Stats-",
          description="Info About Myself-",
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="1. Servers.-",value=f"{len(client.guilds)}",inline=True)
    embed.add_field(name="2. Users.-",value=f"{len(client.users)}",inline=False)
    embed.add_field(name="3. Owner-",value=f"SuperSaaim#1731",inline=False)
    embed.add_field(name="4. Coding Language-",value=f"Python!",inline=True)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

@client.command()
async def info(ctx, message, to: discord.Member=None):
    async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
    rlist = []
    count = 1
    for role in to.roles:
        if role.name != "@everyone":
            rlist.append(f"{count}. {role.name}")
            count = count + 1
    b = "\n".join(rlist)
    embed = discord.Embed(
          title=f"Here is the Info on {to}-",
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="1. Name.-",value=f"```{to.display_name}```",inline=True)
    embed.add_field(name="2. Tag.-",value=f"```#{to.discriminator}```",inline=True)
    embed.add_field(name="3. ID-",value=f"```{to.id}```",inline=False)
    embed.add_field(name="4. Account Created At-",value=f"```{to.created_at.__format__('%A, %d. %B %Y at %I:%M %p')}```",inline=False)
    embed.add_field(name=f"5. Joined {message.guild.name} At-",value=f"```{to.joined_at.strftime('%A, %b %d, %Y at %I:%M %p')}```",inline=False)
    embed.add_field(name=f'Roles({len(rlist)})', value=f"```{''.join([b])}```", inline=False)
    embed.add_field(name=f"6. Top Role-",value=f"```{to.roles[-1]}```",inline=False)
    embed.add_field(name="Useful Links", value="**<:pointgun:913685484436340776> [Invite me](https://discord.com/api/oauth2/authorize?client_id=894868536906874900&permissions=8&scope=bot) | <:pointgun:913685484436340776> [Support Server](https://discord.gg/w4rTPMjkWy)**")
    embed.set_thumbnail(url=to.avatar_url)
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

@client.command()
async def cheat(ctx, slap_to: discord.Member=None):
  async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
  if slap_to == None:
    asset = client.user.avatar_url_as(size=128)
    asset1 = ctx.message.author.avatar_url_as(size=128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    data1 = BytesIO(await asset1.read())
    pfp1 = Image.open(data1)

    slap = Image.open(f"cheating.png")

    pfp = pfp.resize((200, 202))

    slap.paste(pfp, (350, 70))

    pfp1 = pfp1.resize((224, 222))

    slap.paste(pfp1, (579, 259))

    slap.save(f"cheat.jpg")
    await ctx.message.reply(file=discord.File(f"cheat.jpg"))
    os.remove(f"cheat.jpg")
  else:
    asset = ctx.message.author.avatar_url_as(size=128)
    asset1 = slap_to.avatar_url_as(size=128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    data1 = BytesIO(await asset1.read())
    pfp1 = Image.open(data1)

    slap = Image.open(f"cheating.png")

    pfp = pfp.resize((89, 90))

    slap.paste(pfp, (10, 40))

    pfp1 = pfp1.resize((224, 222))

    slap.paste(pfp1, (850, 360))

    slap.save(f"cheat.jpg")
    await ctx.message.reply(file=discord.File(f"cheat.jpg"))
    os.remove(f"cheat.jpg")

@client.command()
async def rip(ctx, user: discord.Member = None):
  async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
  if user == None:
    user = ctx.message.author
  r = random.randint(25, 75)
  age = f"{datetime.date.today().year - r} - {datetime.date.today().year}"
  rip = Image.open(f"rip.png")
  title_font = ImageFont.truetype('arialbd.ttf', 22)
  title_font1 = ImageFont.truetype('arialbd.ttf', 16)
  asset = user.avatar_url_as(size=128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((130, 110))
  rip.paste(pfp, (90, 175))
  image_editable = ImageDraw.Draw(rip)
  image_editable.text((100, 300), f"{user.display_name}", (0, 0, 0), font=title_font)
  image_editable.text((100, 330), f"{age}", (0, 0, 0), font=title_font1)
  rip.save(f"{user.name} rip.png")
  await ctx.message.reply(file=discord.File(f"{user.name} rip.png"))
  os.remove(f"{user.name} rip.png")

@client.command()
async def ping(ctx):
    async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
    s = time.time()
    msg = await ctx.send(f"Pong! \n***{round(client.latency * 1000)} ms***")
    e = time.time()
    await msg.edit(
    content=f"Pong! \nBot latency ***{round(client.latency * 1000)} ms***\nMy Message Sending speed  ***{round((e - s) * 1000)} ms***")

@client.command()
async def pet(ctx, slap_to: discord.Member=None):
  async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
  if slap_to==None:
    clientProfilePicture = ctx.author.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/premium/petpet?avatar={clientProfilePicture}&key=oq1pzwMMN5iYc2OEOYi0YHEbW", 'gfg.gif')
    await ctx.channel.send(file=discord.File('gfg.gif'))
  else:
    clientProfilePicture = slap_to.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/premium/petpet?avatar={clientProfilePicture}&key=oq1pzwMMN5iYc2OEOYi0YHEbW", 'gfg.gif')
    await ctx.channel.send(file=discord.File('gfg.gif'))

@client.command()
async def simcard(ctx, slap_to: discord.Member=None):
  async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
  if slap_to==None:
    clientProfilePicture = ctx.author.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/simpcard?avatar={clientProfilePicture}", 'gfg.png')
    await ctx.channel.send(file=discord.File('gfg.png'))
  else:
    clientProfilePicture = slap_to.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/simpcard?avatar={clientProfilePicture}", 'gfg.png')
    await ctx.channel.send(file=discord.File('gfg.png'))

@client.command()
async def jail(ctx, slap_to: discord.Member=None):
  async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
  if slap_to==None:
    clientProfilePicture = ctx.author.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/jail?avatar={clientProfilePicture}", 'gfg.png')
    await ctx.channel.send(file=discord.File('gfg.png'))
  else:
    clientProfilePicture = slap_to.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/jail?avatar={clientProfilePicture}", 'gfg.png')
    await ctx.channel.send(file=discord.File('gfg.png'))

@client.command()
async def police(ctx, slap_to: discord.Member=None):
  async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
  if slap_to==None:
    clientProfilePicture = ctx.author.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/lolice?avatar={clientProfilePicture}", 'gfg.png')
    await ctx.channel.send(file=discord.File('gfg.png'))
  else:
    clientProfilePicture = slap_to.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/lolice?avatar={clientProfilePicture}", 'gfg.png')
    await ctx.channel.send(file=discord.File('gfg.png'))

@client.command()
async def mission(ctx, slap_to: discord.Member=None):
  async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
  if slap_to==None:
    from PIL import Image
    clientProfilePicture = ctx.author.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/passed?avatar={clientProfilePicture}", 'gfg.gif')
    await ctx.channel.send(file=discord.File('gfg.gif'))
  else:
    from PIL import Image
    clientProfilePicture = slap_to.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/passed?avatar={clientProfilePicture}", 'gfg.gif')
    await ctx.channel.send(file=discord.File('gfg.gif'))

@client.command()
async def wasted(ctx, slap_to: discord.Member=None):
  if slap_to == None:
    from PIL import Image
    clientProfilePicture = ctx.author.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/wasted?avatar={clientProfilePicture}", 'gfg.gif')
    await ctx.channel.send(file=discord.File('gfg.gif'))
  else:
    from PIL import Image
    clientProfilePicture = slap_to.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/wasted?avatar={clientProfilePicture}", 'gfg.gif')
    await ctx.message.reply(file=discord.File('gfg.gif'))

@client.command()
async def triggered(ctx, slap_to: discord.Member=None):
  async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
  if slap_to == None:
    from PIL import Image
    clientProfilePicture = ctx.author.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/triggered?avatar={clientProfilePicture}", 'gfg.gif')
    await ctx.message.reply(file=discord.File('gfg.gif'))
  else:
    from PIL import Image
    clientProfilePicture = slap_to.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/triggered?avatar={clientProfilePicture}", 'gfg.gif')
    await ctx.message.reply(file=discord.File('gfg.gif'))


@client.command()
async def slap(ctx, slap_to: discord.Member=None):
  async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
  if slap_to == None:
    asset = client.user.avatar_url_as(size=128)
    asset1 = ctx.message.author.avatar_url_as(size=128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    data1 = BytesIO(await asset1.read())
    pfp1 = Image.open(data1)

    slap = Image.open(f"slap.png")

    pfp = pfp.resize((200, 202))

    slap.paste(pfp, (350, 70))

    pfp1 = pfp1.resize((224, 222))

    slap.paste(pfp1, (579, 259))

    slap.save(f"{client.user} slapped {ctx.message.author.name}.jpg")
    await ctx.message.reply(file=discord.File(f"{client.user} slapped {ctx.message.author.name}.jpg"))
    os.remove(f"{client.user} slapped {ctx.message.author.name}.jpg")
  else:
    asset = ctx.message.author.avatar_url_as(size=128)
    asset1 = slap_to.avatar_url_as(size=128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    data1 = BytesIO(await asset1.read())
    pfp1 = Image.open(data1)

    slap = Image.open(f"slap.png")

    pfp = pfp.resize((200, 202))

    slap.paste(pfp, (500, 130))

    pfp1 = pfp1.resize((224, 222))

    slap.paste(pfp1, (850, 360))

    slap.save(f"{ctx.message.author.name} slapped {slap_to.name}.jpg")
    await ctx.message.reply(file=discord.File(f"{ctx.message.author.name} slapped {slap_to.name}.jpg"))
    os.remove(f"{ctx.message.author.name} slapped {slap_to.name}.jpg")

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
  try:
    if ctx.message.author.server_permissions.administrator:
        if reason==None:
          reason="no reason provided"
        await message.guild.kick(member)
        embed = discord.Embed(
            title=f"Kick Info!-",
            description=f"{member} was kicked by {message.author} and Reason - {reason}",
            timestamp=message.created_at,
            color=discord.Color.dark_blue()
        )
        embed.set_footer(text=f"Master- {message.author}")
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await ctx.channel.send(embed=embed)
    else:
      await ctx.channel.send("Hehe trying to be owner it wont work on Me! Only owners of server can do this command")
  except Exception:
    await ctx.channel.send(f'<@{message.author.id}> I dont have perms of it sorry!')

    
@client.command()
async def ban(message, member : discord.Member, *, reason=None):
    try:
      if message.author==message.guild.owner:
          if reason==None:
            reason="no reason provided"
          await message.guild.ban(member)
          embed = discord.Embed(
              title=f"Ban Info!-",
              description=f"{member} was banned by {message.author} and Reason - {reason}",
              timestamp=message.created_at,
              color=discord.Color.dark_blue()
          )
          embed.set_footer(text=f"Master- {message.author}")
          embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
          await message.channel.send(embed=embed)
      else:
        await message.channel.send("Hehe trying to be owner it wont work on Me! Only owners of server can do this command")
    except Exception:
      await message.channel.send(f'<@{message.author.id}> I dont have perms of it sorry!')

@client.command()
async def avatar(ctx, member: discord.Member=None):
    async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
    if member is None:
        member = ctx.author

    favatar = discord.Embed(title=f"Avatar of {member}", color=0x000000)
    favatar.set_footer(text=f"Master {ctx.author.name}#{ctx.author.discriminator}")
    favatar.set_image(url='{}'.format(member.avatar_url))

    await ctx.send(embed = favatar)

@client.command()
async def taru(ctx):
    guild_id = 701342127447212093
    await client.get_guild(int(guild_id)).leave()
    await ctx.send(f"I left: {guild_id}")

   
@client.command()
async def calendars(ctx, message, year='2017'):
    async with ctx.typing():
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
    with open(f"calendar of {year}", 'w+') as f:
        f.write(calendar.calendar(int(year)))
    await message.channel.send(file=discord.File(f'calendar of {year}'))

@client.command()
async def university(ctx, *, country):
    em = discord.Embed(title=f"Universities of {country.capitalize()}",
                       description=f"After fetching the Universities of **{country.capitalize()}**, 10 Universities of {country.capitalize()} will appear here within a moment..",
                       timestamp=ctx.message.created_at, color=discord.Color.red()).set_footer(text=bot.user.name)
    m = await ctx.message.reply(embed=em)
    res = requests.get(f"http://universities.hipolabs.com/search?country={country}").json()
    embed = discord.Embed(title=f"Universities of {country.capitalize()}", timestamp=ctx.message.created_at, color=discord.Color.red()).set_footer(text=bot.user.name)
    for i in range(10):
        embed.add_field(name=f"{i + 1}. {res['name']}", value=f"Website:  {res['web_pages'][0]}\nDomain :  {res['domains'][0]}", inline=False)
    await m.edit(embed=embed)
  
@client.event
async def on_ready():
   await client.wait_until_ready()
   print("We have logged in as {0.user} BY SUPER SAAIM".format(client))
   statuses =  [f"on {len(client.guilds)} servers | &help","Hello world","Cubex.gg"]
   Music = ["Music","no one"]
   watch = ["Youtube","Anime"]
   while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game(type=discord.ActivityType.playing, name=status))
        await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type = discord.ActivityType.listening, name = Music))
        await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type = discord.ActivityType.watching, name = watch))
        await asyncio.sleep(1)
   client.loop.create_task(on_ready())


@client.event
async def on_member_join(member):
  if member.guild.id==894409573765640193:
    clientProfilePicture = member.avatar_url_as(format="png")
    listt=['stars','stars2','rainbowgradient','rainbow','sunset','night','blobday','blobnight','space','gaming1','gaming3','gaming2','gaming4']
    ram=random.choice(listt)
    col=['red','blue','green','yellow','white']
    colors=random.choice(col)
    URL = f"https://some-random-api.ml/welcome/img/1/{ram}?key=oq1pzwMMN5iYc2OEOYi0YHEbW&discriminator={member.discriminator}&memberCount={member.guild.member_count}&guildName=SuperLearners&textcolor={colors}&type=join&username={member.display_name}&avatar={clientProfilePicture}"
    resp = get(URL)
    if resp.status_code == 200:
      open('image.png', 'wb').write(resp.content)
      print(f'File saved in {getcwd()}')
      idd=893474007624585216
      join=member.id
      channel = client.get_channel(894413149376249897)
      chan=914769263892516896
      channe=918535769688252446
      await channel.send(f"Hey <@{join}>, Welcome to **Super Learners!**\n\nTake Your Roles in <#{chan}>\nFor Chatting with Members go in <#{channe}>\nThis server is a very good knowledge and helping center with a lots of Fun with own custom bot made by owner of this server <@{idd}>  by **Coding**\n, Thanks")
      await channel.send(file=discord.File('image.png'))
    elif resp.status_code != 200:
      jsonresp = resp.json()
      print(resp.status_code)
      print(jsonresp) 
  else:
    return


@client.event
async def on_member_remove(member):
  if member.guild.id==894409573765640193:
    clientProfilePicture = member.avatar_url_as(format="png")
    listt=['stars','stars2','rainbowgradient','rainbow','sunset','night','blobday','blobnight','space','gaming1','gaming3','gaming2','gaming4']
    ram=random.choice(listt)
    col=['red','blue','green','yellow','white']
    colors=random.choice(col)
    URL = f"https://some-random-api.ml/welcome/img/1/{ram}?key=oq1pzwMMN5iYc2OEOYi0YHEbW&discriminator={member.discriminator}&memberCount={member.guild.member_count}&guildName=SuperLearners&textcolor={colors}&type=leave&username={member.display_name}&avatar={clientProfilePicture}"
    resp = get(URL)
    if resp.status_code == 200:
      open('image.png', 'wb').write(resp.content)
      print(f'File saved in {getcwd()}')
      idd=893474007624585216
      join=member.id
      channel = client.get_channel(895320477441069176)
      chan=904010921037414452
      channe=894409573765640198
      await channel.send(file=discord.File('image.png'))
      await channel.send("He just left the server 😔")
    elif resp.status_code != 200:
      jsonresp = resp.json()
      print(resp.status_code)
      print(jsonresp) 
  else:
    return

@client.command(aliases = ["bal"])
async def balance(ctx):
  await open_account(ctx.author)
  users = await get_bank_data()
  user = ctx.author
  wallet_amt = users[str(user.id)]['wallet']
  bank_amt = users[str(user.id)]['bank']
  em = discord.Embed(title=f"{ctx.author.name}'s balance", color=discord.Color.red())
  em.add_field(name='Wallet Balance', value= wallet_amt)
  em.add_field(name='Bank Balance', value= bank_amt)
  await ctx.send(embed=em)

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def beg(ctx):
  await open_account(ctx.author)
  users = await get_bank_data()
  user = ctx.author
  earnings = random.randrange(101)
  await ctx.send(f"Someone gave you {earnings} coins!!")
  users[str(user.id)]['wallet'] += earnings
  with open("mainbank.json","w") as f:
    json.dump(users,f)


@client.command(aliases = ["with"])
async def withdraw(ctx, amount=None):
  await open_account(ctx.author)
  if amount==None:
    await ctx.send("Pls enter the amount bruh!")
    return
  
  bal = await update_bank(ctx.author)
  amount = int(amount)
  if amount>bal[1]:
    await ctx.send("You don't Have MUCH Money NOOOB")
    return
  if amount<0:
    await ctx.send("Amount Must Be Positive!")
    return
  await update_bank(ctx.author, amount)
  await update_bank(ctx.author,-1*amount, "bank")
  await ctx.send(f"You withdrew {amount} coins! hehe")

@client.command(aliases = ["dep"])
async def deposit(ctx, amount=None):
  await open_account(ctx.author)
  if amount==None:
    await ctx.send("Pls enter the amount bruh!")
    return
  
  bal = await update_bank(ctx.author)
  amount = int(amount)
  if amount>bal[0]:
    await ctx.send("You don't Have MUCH Money NOOOB")
    return
  if amount<0:
    await ctx.send("Amount Must Be Positive!")
    return
  await update_bank(ctx.author,-1*amount)
  await update_bank(ctx.author,amount, "bank")
  await ctx.send(f"You deposited {amount} coins! hehe")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def send(ctx,member:discord.Member, amount=None):
  await open_account(ctx.author)
  await open_account(member)

  if amount==None:
    await ctx.send("Pls enter the amount bruh!")
    return
  
  bal = await update_bank(ctx.author)
  amount = int(amount)
  if amount>bal[0]:
    await ctx.send("You don't Have MUCH Money NOOOB")
    return
  if amount<0:
    await ctx.send("Amount Must Be Positive!")
    return

  await update_bank(ctx.author,-1*amount,"wallet")
  await update_bank(member,amount,"wallet")
  await ctx.send(f"You Gave {amount} coins to {member}! hehe")


@client.command(aliases = ["rob"])
@commands.cooldown(1, 15, commands.BucketType.user)
async def steal(ctx,member:discord.Member, amount=None):
  await open_account(ctx.author)
  await open_account(member)
  
  bal = await update_bank(ctx.author)
  if bal[0]<100:
    await ctx.send("Poor Kid! Send Something More Than 100")
    return

  earnings=random.randrange(0, bal[0])
  await update_bank(ctx.author,earnings)
  await update_bank(member,-1*earnings)
  await ctx.send(f"GG <@{ctx.author.id}> You Robbed And Got {earnings} Coins!")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def slots(ctx, amount=None):
  await open_account(ctx.author)
  if amount==None:
    await ctx.send("Pls enter the amount bruh!")
    return
  
  bal = await update_bank(ctx.author)
  amount = int(amount)
  if amount>bal[0]:
    await ctx.send("You don't Have MUCH Money NOOOB")
    return
  if amount<0:
    await ctx.send("Amount Must Be Positive!")
    return
  final = []
  for i in range(3):
    a = random.choice(['X','O','Q'])
    final.append(a)
  await ctx.send(str(final))
  if final[0] == final[1] == final[2]:
    await update_bank(ctx.author,2*amount)
    await ctx.send("You Won ,GG KID")
  else:
    await update_bank(ctx.author,-1*amount)
    await ctx.send("You LOSE ,NOOB")
  
@client.command(aliases = ["lb"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def leaderboard(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)


mainshop = [{"name":"Watch","price":"100","description":"Time!","emoji":":watch:"},
            {"name":"Laptop","price":"1000","description":"Work!","emoji":":computer:"},
            {"name":"PC","price":"10000","description":"Gaming!","emoji":":computer:"}]

@client.command()
async def shop(ctx):
  em = discord.Embed(title = "Shop-")
  for item in mainshop:
    name=item['name']
    price=item['price']
    desc=item['description']
    emoji=item['emoji']
    em.add_field(name=f"{emoji} {name}", value=f"{price}$ | {desc}")
  await ctx.send(embed=em)

@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")


@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    
    em = discord.Embed(title = f"{ctx.author}'s Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]
        em.add_field(name = f"{name}", value = amount)    

    await ctx.send(embed = em)   

@client.command()
async def sell(ctx,amount: int, * ,item):
    with open("mainbank.json", "r") as f:
        e = json.load(f)
    
    if amount <= e[str(ctx.message.author.id)]['bag'][1]['item']['amount']:
        money =  10 * amount
        with open('maibank.json', 'r') as f:
            e = json.load(f)

            e[str(ctx.message.author.id)]['wallet'] += money
            e[str(ctx.message.author.id)]['bag'][str(item).title()]['amount'] -= amount

            with open('mainbank.json', "w") as f:
                json.dump(e, f, indent=4)
            await ctx.message.reply(
            embed=discord.Embed(title=f"Sold Item", description=f"You just sold {amount} {str(item).title()} and got :AssistantCurrency: {money}.",
                                timestamp=ctx.message.created_at, color=discord.Color.red()).set_footer(
                text=bot.user.name))
    else:
        await ctx.message.reply(
            embed=discord.Embed(title=f"Something went wrong @#%$!",
                                description=f"You don't have enough amount of {str(item).title()} in your inventory!",
                                timestamp=ctx.message.created_at, color=discord.Color.red()).set_footer(
                text=bot.user.name))
   

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]
    
async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    costt = price*amount
    cost = int(costt)
    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

async def open_account(user):
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]['wallet'] = 0
    users[str(user.id)]['bank'] = 0
  
  with open("mainbank.json","w") as f:
    json.dump(users,f)
  return True

async def get_bank_data():
  with open("mainbank.json","r") as f:
    users = json.load(f)
  return users

async def update_bank(user, change=0, mode='wallet'):
  users = await get_bank_data()
  users[str(user.id)][mode] += change
  with open("mainbank.json","w") as f:
    json.dump(users,f)
  bal = [users[str(user.id)]['wallet'],users[str(user.id)]['bank']]
  return bal

@client.event
async def on_message(message):
  if message.author == client.user:
      return
  
  elif message.content.startswith("$truth"):
    url=requests.get("https://gist.githubusercontent.com/deepakshrma/9498a19a3ed460fc662c536d138c29b1/raw/f29d323b9b3f0a82f66ed58c7117fb9b599fb8d5/truth-n-dare.json")
    res=url.json()
    truth_list=[
      item
      for item in res
      if item["type"]=="Truth"
    ]
    ran=random.randint(0, len(truth_list)-1)
    truth=truth_list[ran]['summary']
    levels=truth_list[ran]['level']
    level=int(levels)
    if level<3:
      embed = discord.Embed(
            title=f"Truth - ",
            description=f"**{truth}**",
            timestamp=message.created_at,
            color=discord.Color.dark_blue()
      )
      embed.set_footer(text=f"ID- {truth_list[ran]['id']} | Level- {truth_list[ran]['level']}")
      embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)
    else:
      if level<3:
        embed = discord.Embed(
              title=f"Truth - ",
              description=f"**{truth}**",
              timestamp=message.created_at,
              color=discord.Color.dark_blue()
        )
        embed.set_footer(text=f"ID- {truth_list[ran]['id']} | Level- {truth_list[ran]['level']}")
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
      else:
        embed = discord.Embed(
              title=f"Truth - ",
              description=f"**{truth}**",
              timestamp=message.created_at,
              color=discord.Color.dark_blue()
        )
        embed.set_footer(text=f"ID- {truth_list[ran]['id']} | Level- {truth_list[ran]['level']}")
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

  
  elif message.content.startswith("$dare"):
    url=requests.get("https://gist.githubusercontent.com/deepakshrma/9498a19a3ed460fc662c536d138c29b1/raw/f29d323b9b3f0a82f66ed58c7117fb9b599fb8d5/truth-n-dare.json")
    res=url.json()
    truth_list=[
      item
      for item in res
      if item["type"]=="Dare"
    ]
    ran=random.randint(0, len(truth_list)-1)
    truth=truth_list[ran]['summary']
    levels=truth_list[ran]['level']
    level=int(levels)
    if level<3:
      embed = discord.Embed(
            title=f"Dare - ",
            description=f"**{truth}**",
            timestamp=message.created_at,
            color=discord.Color.dark_blue()
      )
      embed.set_footer(text=f"ID- {truth_list[ran]['id']} | Level- {truth_list[ran]['level']}")
      embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)
    else:
      if level<3:
        embed = discord.Embed(
              title=f"Dare - ",
              description=f"**{truth}**",
              timestamp=message.created_at,
              color=discord.Color.dark_blue()
        )
        embed.set_footer(text=f"ID- {truth_list[ran]['id']} | Level- {truth_list[ran]['level']}")
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
      else:
        embed = discord.Embed(
              title=f"Dare - ",
              description=f"**{truth}**",
              timestamp=message.created_at,
              color=discord.Color.dark_blue()
        )
        embed.set_footer(text=f"ID- {truth_list[ran]['id']} | Level- {truth_list[ran]['level']}")
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

  elif message.content.startswith("$university"):
    country = message.content.replace("$university ","")
    em = discord.Embed(title=f"Universities of {country.capitalize()}",
                       description=f"After fetching the Universities of **{country.capitalize()}**, 10 Universities of {country.capitalize()} will appear here within a moment..",
                       color=discord.Color.red()).set_footer(text=bot.user.name)
    m = await message.reply(embed=em)
    ree = requests.get(f"http://universities.hipolabs.com/search?country={country}")
    res = ree.json()
    embed = discord.Embed(title=f"Universities of {country.capitalize()}", color=discord.Color.red()).set_footer(text=bot.user.name)
    for i in range(10):
        embed.add_field(name=f"{i + 1}. {res['name']}", value=f"Website:  {res['web_pages'][0]}\nDomain :  {res['domains'][0]}", inline=False)
    await m.edit(embed=embed)

  elif message.content.startswith("$cal"):
    try:
      year = message.content.replace("$cal ","")
      with open(f"calendar of {year}.txt", 'w+') as f:
        f.write(calendar.calendar(int(year)))
      await message.channel.send(f"Here is a Calendar of `{year}`") 
      await message.channel.send(file=discord.File(f'calendar of {year}.txt'))
      os.remove(f"calendar of {year}.txt")
    except:
      await message.channel.send("**Oh Man! Something Went Wrong!**")

  elif message.content.startswith("$qrcode"):
    msg = message.content.replace("$qrcode ","")
    url = pyqrcode.create(msg)
    url.png('myqr.png', scale = 6)
    await message.channel.send(file=discord.File('myqr.png'))
    os.remove("myqr.png")

  elif message.content.startswith("$sct info"):
    dat=requests.get(f"http://api.open-notify.org/astros.json")
    da=dat.json()
    rlist = []
    count = 1
    for name in da['people']:
      rlist.append(f"{count}. {name['name']} at  -{name['craft']}")
      count = count + 1
    b = "\n".join(rlist)
    data=requests.get(f"http://api.open-notify.org/iss-now.json")
    dat=data.json()
    embed = discord.Embed(
          title=f"International Space Station (ISS) current information",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="Location-",value=f"```Latitude: {dat['iss_position']['latitude']}\nLongitude: {dat['iss_position']['longitude']}```View Location in [Google Maps](https://www.google.com/maps/place/{dat['iss_position']['latitude']},{dat['iss_position']['longitude']})",inline=False)
    embed.add_field(name=f"Astronauts ({da['number']})-",value=f"```{''.join([b])}```",inline=False)
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$help all"):
    embed=discord.Embed(title="Hello, I am JARVIS A bot who will might make a smile on your face or something like that or something, urgh i am too bad at this\n(～￣(OO)￣)ブ", description=f"```(0)I can Read Your Mind for that write, - '$mind read'\n\n(1)Write 'fact' for getting random facts\n\n(2)Write 'joke' for getting random jokes\n\n(3)Write 'inspire' for getting random inspire statements\n\n(4)Write 'memes' for getting random memes\n\n(5)If you are feeling bored and want something to do write $activity\n\n(6)Write 'marks' for checking my marks\n\n(7)If you wanna info of anyone in this server write - $dict @(name of person)\n\n(8)I am also having dictionary, just type '$meaning of (word)' to get meaning of your word\n\n(9)Write 'story' if you want a story\n\n(10)If u want me to leave for 1 or 2 minute write 'jarvis leave for 1/2 minute'\n\n(11)If u want me to exit from chat write 'jarvis exit'\n\n(12)If u want me to roast you write '$roast'\n\n(13)If u want me to ask you random questions write 'random'\n\n(14)If u want me to ask riddles to you write 'riddles'\n\n(15)I have a translator also if u want me to translate english write - '!translate english (your statement here)'\n\n(16)If u wanna see my intro write 'intro jarvis'\n\n(17)If u wanna know the date write- 'date'\n\n(18)Hey i also have 4 games in me which u can play and earn coins ,for playing each game choose write - '$word', '$rps', '$dice', '$guess', '$poke' And more to come\n\n(19)I told u that you can earn coins, but you can also shop with them for shopping write- '$shop'\n\n(20)To check how many coins you have write- '$coins'\n\n(21)If you want me to kill someone write- '$kill'\n\n(22)If u want me to search something write- '$search (the thing you wanna search)'\n\n(23)If you wanna give someone some coins of yours write- '$giveaway'\n\n(24)If u wanna ask me square root/cube root of any number then ask me\n\n(25)You can ask me about 'who is ...' or 'what is ....' type questions\n\n(26)If u wanna know the covid cases write- 'covid cases'\n\n(27)I am also having How-to-do function, for using it write - how to (thing u wanna know)\n\n(28)If u wanna know avatar of anyone in server write- '$avatar @(member name)'\n\n(29)If u wanna know your id write- 'my id'\n\n(30)If u wanna apply filters write - '$filter'\n\n(31)If u wanna use a cool feature of mine write - '$cool'\n\n(32)If u want me to remember something write - '$rm (the thing you want me to remember)' and if u wanna check your to-do list write - 'to do'\n\n(33)For checking your typing speed wright '$speed check'\n\n(34)For try something like hacking write - '$hack (name)'\n\n(35)If u wanna check membercount of your server write - '$membercount'\n\n(36)You can also search Youtube videos with me , for doing it write - '$yt (name of thing u wanna search)'\n\n(37)Hey, You can also Rob  others coins that they have earned but there is also a risk you can be caught by police (Do it on your own risk)\n\n(38)Hey if u wanna play games and they arent working You have to make your profile ,for making it write - $profile\n\n(39)You can also get images of DOGS, CATS, BIRDS, PANDAS, FOX, KOALA and beautiful , informative Facts of them also; How to use -\n\nFor getting images and facts of Dog , write - $dog\nFor getting images and facts of Cat , write - $cat\nFor getting images and facts of Birds , write - $bird\nFor getting images and facts of Pandas , write - $panda\nFor getting images and facts of Fox , write - $fox\nFor getting images and facts of Koala , write - $koala\n\n(40)Hey i can also give lyrics of many songs just write - $lyrics (name of song)\n\n(41)I do have some cool features like avatar of triggered,wasted, mission passed,police,jail,simcard you should try write-\nFor triggered avatar - $triggered\nFor wasted avatar - $wasted\nFor mission passed avatar - $mission\nFor police avatar - $police\nFor jail avatar- $jail\nFor simcard avatar- $simcard\n\n(42)Hey are you feeling lonely, if it is so write - $talk\n\n(43)I can also tell Tables of any number just ask me, write - $table of (number)\n\n(44)If you want me to join a vc channel just join a channel and write $join and if you want me to leave your voice channel in which you are write $leave```", color=0xFF5733)
    await message.channel.send(embed=embed)
    embe=discord.Embed(title="Part-2", description="```(45)If you want to clear a massive amount of messages in a particular channel, write-$clear (number for amount of messages you want to be deleted), example-$clear 5\n\n(46)If you wanna know full info of the server in which you are write - $serverinfo\n\n(47)If you want a fake comment of yt of yours write - $fake yt (comment you wanna write in your fake comment)\n\n(48)There are also 2 cool gif maker like pet gif,amongus gif write- $pet, $amongus\n\n(49)If you want to slap or rip someone here in server write $slap @(member name) or $rip @(member name)\n\n(50)If you want to have some information about someone in server write - $info (mention)\n\n(51)If you want to check my latency and speed so write $ping\n\n(52)If you want to have info about International space system write - $sct info\n\n(53)If you want to check weather of your location write - $weather (you city name)\n\n(54)If you want to emojify some text write - $emojify (text you wanna emojify)\n\n(55)If you want to ask a question to 8ball write - $8ball (your question about urself)\n\n(56)If you wanna know any table of any number write - $table of (number)```", color=0xFF5733)
    await message.channel.send(embed=embe)

  elif message.content.startswith("$help admin"):
    embed = discord.Embed(
          title=f"Here is help on my admin commands-",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="1. Clear channel messages-",value=f"```$clear (amount you wanna clear)```",inline=False)
    embed.add_field(name="2. Kick Someone in Server-",value=f"```$kick (mention someone to kick)```",inline=False)
    embed.add_field(name="2. Ban Someone in Server-",value=f"```$ban (mention someone to ban)```",inline=False)
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$help commands"):
    embed = discord.Embed(
          title=f"Here is help on my commands-",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="Commands That Only Owner Can Use-",value=f"```$help admin```",inline=False)
    embed.add_field(name="Commands That Are For All Users-",value=f"```$help all```",inline=False)
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)
    
  

  elif message.content.startswith("$report"):
    feedback=message.content.replace("$report ","")
    embed = discord.Embed(
          title=f"Report-",
          description=f"{message.author} just given a report to you master for bot @JARVIS. Details are down below!!!",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="Report-",value=f"{feedback}\n\n**------ Information --------**",inline=False)
    embed.add_field(name="Name-",value=f"{message.author}",inline=False)
    embed.add_field(name="ID-",value=f"{message.author.id}",inline=False)
    embed.add_field(name="Server", value=f"{message.guild.name}")
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    user = client.get_user(893474007624585216)
    await user.send(embed=embed)
    await message.channel.send(f"Thanks for your report <@{message.author.id}>\nReport **{feedback}** is Successfully sent to the Owner of JARVIS\nI guess he will try his heart,brain,soul,hand,legs to solve this ")
  
  elif message.content.startswith("$suggestion"):
    feedback=message.content.replace("$suggestion ","")
    embed = discord.Embed(
          title=f"Suggestion-",
          description=f"{message.author} just given a suggestion to you master for bot @JARVIS. Details are down below!!!",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="Suggestion-",value=f"{feedback}\n\n**------ Information --------**",inline=False)
    embed.add_field(name="Name-",value=f"{message.author}",inline=False)
    embed.add_field(name="ID-",value=f"{message.author.id}",inline=False)
    embed.add_field(name="Server", value=f"{message.guild.name}")
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    user = client.get_user(893474007624585216)
    await user.send(embed=embed)
    await message.channel.send(f"Thanks for your suggestion <@{message.author.id}>\nIt means a lot to me!")
    
  elif message.content.startswith("$feedback"):
    feedback=message.content.replace("$feedback ","")
    embed = discord.Embed(
          title=f"Feedback-",
          description=f"{message.author} just given a feedback to you master for bot @JARVIS. Details are down below!!!",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="Feedback-",value=f"{feedback}\n\n**------ Information --------**",inline=False)
    embed.add_field(name="Name-",value=f"{message.author}",inline=False)
    embed.add_field(name="ID-",value=f"{message.author.id}",inline=False)
    embed.add_field(name="Server", value=f"{message.guild.name}")
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    user = client.get_user(893474007624585216)
    await user.send(embed=embed)
    await message.channel.send(f"Thanks for your feedback <@{message.author.id}>\nIt means a lot to me!")
    
  elif message.content.startswith("$jarvisinfo"):
    embed = discord.Embed(
          title=f"JARVIS Information-",
          description=f"Hello, I am JARVIS A bot who will might make a smile on your face or something like that or something, urgh i am too bad at this\n(～￣(OO)￣)ブ",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="1. Prefix-",value=f"```$```",inline=False)
    embed.add_field(name="2. Invite Me-",value=f"<:pointgun:913685484436340776> [Invite me](https://discord.com/api/oauth2/authorize?client_id=894868536906874900&permissions=8&scope=bot)",inline=False)
    embed.add_field(name="4. Server who supports-",value=f"<:pointgun:913685484436340776> [Support Server](https://discord.gg/w4rTPMjkWy)",inline=False)
    embed.add_field(name="5. Owner who made me-",value=f"<:donald:913675037108731905> SuperSaaim#1731",inline=False)
    embed.add_field(name="Useful Links", value="**<:pointgun:913685484436340776> [Invite me](https://discord.com/api/oauth2/authorize?client_id=894868536906874900&permissions=8&scope=bot) | <:pointgun:913685484436340776> [Support Server](https://discord.gg/w4rTPMjkWy)**")
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$sqrt"):
    math1=message.content.replace("$sqrt ","")
    hmmm=int(math1)
    await message.channel.send(f"The root of {hmmm} is <a:hehe:914740567848656987>" )
    await message.channel.send(math.sqrt(hmmm))

  elif message.content.startswith("$cbrt"):
    math2=message.content.replace("$cbrt ","")
    hmmm1=int(math2)
    x = hmmm1
    cr = x ** (1./3.)
    await message.channel.send(f"The Cube root of {x} is {cr} <a:hehe:914740567848656987>")
    await message.channel.send(f"The rounded off form of cube root of {x} is {round(cr)}")

  elif message.content.startswith("$help math"):
    embed = discord.Embed(
          title=f"Here is the Help on Math dude-",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="1. Find Square root.-",value=f"```$sqrt (number)```",inline=False)
    embed.add_field(name="2. Find Cube root.-",value=f"```$cbrt (number)```",inline=False)
    embed.add_field(name="Useful Links", value="**<:pointgun:913685484436340776> [Invite me](https://discord.com/api/oauth2/authorize?client_id=894868536906874900&permissions=8&scope=bot) | <:pointgun:913685484436340776> [Support Server](https://discord.gg/w4rTPMjkWy)**")
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$help others"):
    embed = discord.Embed(
          title=f"Here is the Help on others dude-",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="1. Check my latency and typing speed.-",value=f"```$ping```",inline=False)
    embed.add_field(name="2. Take some user info.-",value=f"```$info (mention someone)```",inline=False)
    embed.add_field(name="Useful Links", value="**<:pointgun:913685484436340776> [Invite me](https://discord.com/api/oauth2/authorize?client_id=894868536906874900&permissions=8&scope=bot) | <:pointgun:913685484436340776> [Support Server](https://discord.gg/w4rTPMjkWy)**")
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$help info"):
    embed = discord.Embed(
          title=f"Here is the Help on info dude-",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="1. About Myself (J.A.R.V.I.S#1731).-",value=f"```$jarvisinfo```",inline=False)
    embed.add_field(name="2. GiveMe Some feedback bruh...-",value=f"```$feedback (Your feedback About Me)```",inline=False)
    embed.add_field(name="3. And Also GiveMe Some Suggestion On A Command-",value=f"```$suggestion (Your Suggestion About Me)```",inline=False)
    embed.add_field(name="4. AAH! If You found Any Error In Me Pls Report-",value=f"```$report (issue you have)```",inline=False)
    embed.add_field(name="Useful Links", value="**<:pointgun:913685484436340776> [Invite me](https://discord.com/api/oauth2/authorize?client_id=894868536906874900&permissions=8&scope=bot) | <:pointgun:913685484436340776> [Support Server](https://discord.gg/w4rTPMjkWy)**")
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$help"):
    embed = discord.Embed(
          title=f"Here is help on My features-",
          timestamp=message.created_at,
          color=discord.Color.dark_blue()
    )
    embed.add_field(name="My prefix-",value=f"```$\n(But some features dont use this)```",inline=False)
    embed.add_field(name="All Commands-",value=f"```$help commands```",inline=False)
    embed.add_field(name="Info-",value=f"```$help info```",inline=True)
    embed.add_field(name="Math-",value=f"```$help math```",inline=True)
    embed.add_field(name="Others-",value=f"```$help others```",inline=False)
    embed.add_field(name="Useful Links", value="**<:pointgun:913685484436340776> [Invite me](https://discord.com/api/oauth2/authorize?client_id=894868536906874900&permissions=8&scope=bot) | <:pointgun:913685484436340776> [Support Server](https://discord.gg/w4rTPMjkWy)**")
    embed.set_footer(text=f"Master- {message.author}")
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$meaning of"):
    if message.channel.id==915263140923592744:
      return
    else:
      emoji = "📜"
      await message.add_reaction(emoji)
      try:
        try:
          try:
            from PyDictionary import PyDictionary
            namm=message.content.replace('$meaning of ',"")
            embed = discord.Embed(
                  title=f"Meaning of {namm}",
                  timestamp=message.created_at,
                  color=discord.Color.red()
            )
            dict = PyDictionary()
            meaning = dict.meaning(namm)
            embed.add_field(name="Noun-",value=f"•`{meaning['Noun']}`",inline=False)
            embed.add_field(name="Verb-",value=f"•`{meaning['Verb']}`",inline=False)
            embed.set_footer(text=f"Master- {message.author}")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
          except Exception:
            from PyDictionary import PyDictionary
            namm=message.content.replace('$meaning of ',"")
            embed = discord.Embed(
                  title=f"Meaning of {namm}",
                  timestamp=message.created_at,
                  color=discord.Color.red()
            )
            dict = PyDictionary()
            meaning = dict.meaning(namm)
            embed.add_field(name="Noun-",value=f"•`{meaning['Noun']}`",inline=False)
            embed.set_footer(text=f"Master- {message.author}")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
        except Exception:
            from PyDictionary import PyDictionary
            namm=message.content.replace('$meaning of ',"")
            embed = discord.Embed(
                  title=f"Meaning of {namm}",
                  timestamp=message.created_at,
                  color=discord.Color.red()
            )
            dict = PyDictionary()
            meaning = dict.meaning(namm)
            embed.add_field(name="Verb-",value=f"•`{meaning['Verb']}`",inline=False)
            embed.set_footer(text=f"Master- {message.author}")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
      except Exception:
        embed = discord.Embed(
          title=f"An error occurred !%&",
          description=f"Sorry @{message.author} I dont have this word in my dictionary",
          timestamp=message.created_at,
          color=discord.Color.red()
        )
        meaning = dict.meaning(namm)
        embed.set_footer(text=f"Master- {message.author}")
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

  elif message.content.startswith("$weather"):
    try:
      namm=message.content.replace('$weather ',"")
      data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={namm}&appid=ab94a2a9599587acf618c61b8d2a8d66")
      dat=data.json()
      embed = discord.Embed(
          title=f"Weather for {dat['name']}",
          timestamp=message.created_at,
          color=discord.Color.red()
      )
      embed.add_field(name="Location-",value=namm.capitalize(),inline=False)
      temp_city = dat['main']['temp'] - 273.15
      embed.add_field(name="Current Temperature-",value=f'{temp_city}°C', inline=False)
      embed.add_field(name="Current Weather-",value=dat['weather'][0]['main'], inline=False)
      embed.add_field(name="Current Humidity-",value=f"{dat['main']['humidity']}%", inline=False)
      embed.add_field(name="Current Wind speed-",value=f"{dat['wind']['speed']} kmph", inline=False)
      embed.add_field(name="Max/Min Temperature-",value=f"Max Temp- {dat['main']['temp_max'] - 273.15}°C | Min Temp- {dat['main']['temp_min'] - 273.15}°C", inline=False)
      embed.set_footer(text=f"Master- {message.author}")
      embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)
    except Exception:
      await message.channel.send(f"<@{message.author.id}> There is a wrong input write like - $weather california")
  
  elif message.content.startswith("$emojify"):
    try:
      nam=message.content.replace("$emojify ","")
      text=nam
      emojis=[]
      for s in text.lower():
        if s.isdecimal():
          num2emo = {'0':'zero','1':'one','2':'two',
                    '3':'three','4':'four','5':'five',
                    '6':'seven','8':'eight','9':'nine'}
          emojis.append(f':{num2emo.get(s)}:')
        elif s.isalpha():
          emojis.append(f':regional_indicator_{s}:')
        else:
          emojis.append(f"  {s}")
      await message.channel.send(''.join(emojis))
    except Exception as e:
      await message.channel.send("An error occured")

  elif message.content.startswith("ja.add"):
    if message.channel.id == 923464698752561152:
      await message.channel.send(f"Sure {message.author}! We will look forward to this, You will get a DM message regarding your bot is accepted or rejcted 🤗")
      user = message.guild.owner
      await user.send(f"Master, A new invitation to add by {message.author}-")
      await user.send(message.content)
      def check(msg):
          return msg.author == user
      msg = await client.wait_for("message", check=check)
      if msg.content == "accept":
        await message.author.send("Hey your bot is accepted in SuperLearners server pls check him,Thanks")
      else:
        await message.author.send("Hey your bot is rejected in SuperLearners server pls ask the owner of that server that why your bot was not accepted,Thanks")
    else:
      return

  elif message.content.startswith("$8ball"):
    ques=message.content.replace("$8ball ","")
    nma=get(f"https://8ball.delegator.com/magic/JSON/{ques}")
    nm=nma.json()
    await message.channel.send(f"🎱 Answer: {nm['magic']['answer']}")

  elif message.content.startswith("$table of"):
    nu=message.content.replace("$table of ","")
    num=int(nu)
    for i in range(1,10):
        ans=num*i
        await message.channel.send(f"{num} X {i} = {ans}")
    last=num*10
    await message.channel.send(f"{num} X 10 = {last}")

  elif message.content.startswith("$invite"):
    embed = discord.Embed(
        title=f"Invite Link for Jarvis",
        description=f"https://discord.com/api/oauth2/authorize?client_id=894868536906874900&permissions=137439472704&scope=bot",
        timestamp=message.created_at,
        color=discord.Color.red()
      )
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$play"):
    channelvc = client.get_channel(894409574092791809)
    vc = await channelvc.connect()
    vc.play((discord.FFmpegPCMAudio("C:\\Users\\tosee\\Desktop\\html\\class 8\\stickers png\\iamjarvis.mp3")))
    def check(msg):
          return msg.author == message.author and msg.channel == message.channel
    msg = await client.wait_for("message", check=check)
    if msg.content=="stop":
      vc.stop()
    else:
      return

  elif message.content.startswith("$join"):
    if not message.author.voice:
        await message.channel.send("Bruh! First connect to a voice channel pls")
        return
    else:
        channel = message.author.voice.channel
    await channel.connect()
    await message.channel.send("I joined your voice channel Master!")

  elif message.content.startswith("$leave"):
    try:
      voice_client = message.guild.voice_client
      if voice_client.is_connected():
          await voice_client.disconnect()
          await message.channel.send("I left your voice channel master!")
      else:
          await message.channel.send("Bruh!! Im not in any voice channel, where to disconect?")
    except Exception:
      await message.channel.send("Bruh!! Im not in any voice channel, where to disconect?")

  elif message.content.startswith("$clear"):
    try:
      if message.guild.owner==message.author:
        nmp=message.content.replace("$clear ","")
        nmc=int(nmp)
        nm=nmc+1
        await message.channel.purge(limit=nm)
        await message.channel.send(f"I have cleared {nmc} messages from this channel!")
      else:
        await message.channel.send("Hehe trying to be owner it wont work on Me! Only owners of server can do this command")
    except Exception:
      await message.channel.send("Wrong input!")

  elif message.content.startswith("$roast"):
      icon="https://cdn-icons.flaticon.com/png/128/782/premium/782265.png?token=exp=1638771117~hmac=bd369251dbc8dcb35b59097fff89f1e1"
      nm=message.content.replace("$roast ","")
      pp=get("https://evilinsult.com/generate_insult.php?lang=en&type=json&pg=pg")
      mm=pp.json()
      embed = discord.Embed(
        title=f"Roast -",
        description=f"🔥 ***{nm}- {mm['insult']}***",
        timestamp=message.created_at,
        color=discord.Color.red()
      )
      embed.set_thumbnail(url=icon)
      embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)

  elif message.content.startswith("$activity"):
    icon="https://cdn-icons-png.flaticon.com/256/4593/4593614.png"
    tk=get(f"https://www.boredapi.com/api/activity?type=recreational")
    ppk=tk.json()
    embed = discord.Embed(
        title="You can do-",
        description=f"✅ ***{ppk['activity']}***",
        timestamp=message.created_at,
        color=discord.Color.red()
      )
    embed.set_thumbnail(url=icon)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)
    
  elif message.content.startswith("$serverinfo"):
    try:
      role_count = len(message.guild.roles)
      list_of_bots = [bot.mention for bot in message.guild.members if bot.bot]
      name = str(message.guild.name)
      description = str(message.guild.description)
      owner = str(message.guild.owner)
      id = str(message.guild.id)
      region = str(message.guild.region)
      memberCount = str(message.guild.member_count)
      icon = str(message.guild.icon_url)
      verification=message.guild.verification_level
      dat=message.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')
      total_text_channels = len(message.guild.text_channels)
      total_voice_channels = len(message.guild.voice_channels)
      total_channels = total_text_channels  + total_voice_channels 
      embed = discord.Embed(
          title=name + " Server Information",
          description=f"**Description**: {description}",
          timestamp=message.created_at,
          color=discord.Color.blue()
        )
      embed.set_thumbnail(url=icon)
      embed.add_field(name="Owner", value=owner, inline=True)
      embed.add_field(name="Server ID", value=id, inline=True)
      embed.add_field(name="Region", value=region, inline=True)
      embed.add_field(name="Member Count", value=memberCount, inline=True)
      embed.add_field(name="Verification Level", value=verification, inline=True)
      embed.add_field(name="Created At", value=dat, inline=True)
      embed.add_field(name='Number of roles', value=str(role_count), inline=True)
      embed.add_field(name='Bots', value=(', '.join(list_of_bots)))
      embed.add_field(name="Server Channels: ", value=total_channels )
      embed.add_field(name="Server Text Channels: ", value=total_text_channels )
      embed.add_field(name="Server Voice Channels: ", value=total_voice_channels )
      embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)
    except Exception:
      role_count = len(message.guild.roles)
      list_of_bots = [bot.mention for bot in message.guild.members if bot.bot]
      name = str(message.guild.name)
      description = str(message.guild.description)
      owner = str(message.guild.owner)
      id = str(message.guild.id)
      region = str(message.guild.region)
      memberCount = str(message.guild.member_count)
      icon = str(message.guild.icon_url)
      verification=message.guild.verification_level
      dat=message.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')
      total_text_channels = len(message.guild.text_channels)
      total_voice_channels = len(message.guild.voice_channels)
      total_channels = total_text_channels  + total_voice_channels 
      embed = discord.Embed(
          title=name + " Server Information",
          description=f"**Description**: {description}",
          timestamp=message.created_at,
          color=discord.Color.blue()
        )
      embed.set_thumbnail(url=icon)
      embed.add_field(name="Owner", value=owner, inline=True)
      embed.add_field(name="Server ID", value=id, inline=True)
      embed.add_field(name="Region", value=region, inline=True)
      embed.add_field(name="Member Count", value=memberCount, inline=True)
      embed.add_field(name="Verification Level", value=verification, inline=True)
      embed.add_field(name="Created At", value=dat, inline=True)
      embed.add_field(name='Number of roles', value=str(role_count), inline=True)
      embed.add_field(name="Server Channels: ", value=total_channels )
      embed.add_field(name="Server Text Channels: ", value=total_text_channels )
      embed.add_field(name="Server Voice Channels: ", value=total_voice_channels )
      embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)

  elif message.content.startswith("$dict"):
    nm=message.content.replace("$dict ","")
    age=random.randint(1,200)
    locations=['california','texas','india','canada','san francisco','No-where','North Pole','South Pole']
    location=random.choice(locations)
    occup=['Lame doctor', 'Bored engineer', 'UN-creatful Artist', 'Loser player', 'Fighting lawyer','UN-occupied','Crazy pilot','Not a teacher']
    occ=random.choice(occup)
    hobby=['Coding','Sleeping', 'Listening songs', 'Playing video games continuosly', 'Thinking what is my Hobby', 'Weak foortballer','Pretending to be reading books','Telling lies']
    urls=['https://cdn-icons-png.flaticon.com/128/480/480016.png','https://cdn-icons-png.flaticon.com/128/742/742836.png','https://cdn-icons-png.flaticon.com/128/60/60068.png','https://cdn-icons-png.flaticon.com/128/5849/5849266.png','https://cdn-icons-png.flaticon.com/128/5219/5219061.png']
    url=random.choice(urls)
    hob=random.choice(hobby)
    embed=discord.Embed(title="<a:hecker:913757233911848980> `Information Found!!`", url="https://discord.gg/w4rTPMjkWy", description=f"✅ Name: **{nm}**\n✅ Age: **{age}**\n✅ Location: **{location}**\n✅ Occupation: **{occ}**\n✅ Hobby: **{hob}**", color=0xFF5733)
    embed.set_author(name="J.A.R.V.I.S", url="https://discord.gg/w4rTPMjkWy", icon_url="https://static.wikia.nocookie.net/marvelmovies/images/0/06/J.A.R.V.I.S..jpg/revision/latest?cb=20130421191808")
    embed.set_thumbnail(url=url)
    await message.channel.send(embed=embed)


  elif message.content.startswith("$fake yt"):
    mssge=message.content.replace("$fake yt ","")
    mssg=mssge.replace(" ","%20")
    clientProfilePicture = message.author.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/youtube-comment?avatar={clientProfilePicture}&comment={mssg}&username={message.author}", 'gfg.png')
    await message.channel.send(file=discord.File('gfg.png'))

  elif message.content.startswith("$amongus"):
    clientProfilePicture = message.author.avatar_url_as(format="png")
    urllib.request.urlretrieve(f"https://some-random-api.ml/premium/amongus?avatar={clientProfilePicture}&key=oq1pzwMMN5iYc2OEOYi0YHEbW&username={message.author}", 'gfg.gif')
    await message.channel.send(file=discord.File('gfg.gif'))
  
  elif message.content.startswith("$mc"):
    try:
      user=message.content.replace("$mc ","")
      pl=get(f"https://some-random-api.ml/mc?username={user}")
      js=pl.json()
      embed = discord.Embed(title=f"{js['username']}!", description=f"***UUID: {js['uuid']}***",color=discord.Color.blue())
      await message.channel.send(embed=embed)
    except Exception:
      await message.channel.send("No such character")


  elif message.content.startswith("$talk"):
    try:
      await message.channel.send(f"Hi {message.author} Lets talk! If u wanna stop talking write - finish")
      while True:
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel
        msg = await client.wait_for("message", check=check)
        if msg.content=="finish":
          await message.channel.send("Ok thanks for talking")
          break
        elif msg.content=="who made you":
          await message.channel.send("I was made by master saaim")
        elif msg.content=="who created you":
          await message.channel.send("I was made by master saaim")
        elif msg.content=="say saaim is a good girl":
          await message.channel.send("Im not ur assistant monkey")
        elif msg.content=="say saaim is a girl":
          await message.channel.send("Im not ur assistant monkey")
        else:
          pk=get(f"https://some-random-api.ml/chatbot?message={msg.content}&key=oq1pzwMMN5iYc2OEOYi0YHEbW")
          i=pk.json()
          await message.channel.send(i['response'])
    except Exception:
      await message.channel.send(f"Not in mood right now ! {message.author}")


  elif message.content.startswith("$lyrics"):
    try:
      lyrics=message.content.replace("$lyrics ","")
      ly=get(f"https://some-random-api.ml/lyrics?title={lyrics}")
      l=ly.json()
      embed = discord.Embed(
        title=f"Lyrics for {lyrics}",
        description=f"{l['lyrics']}",
        timestamp=message.created_at,
        color=discord.Color.red()
      )
      embed.set_thumbnail(url=client.user.avatar_url)
      embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)
    except Exception:
      await message.channel.send("Sorry this song lyrics are very long") 

  
  elif message.content.startswith("$koala"):
      request = get("https://some-random-api.ml/img/koala")
      dogjson = request.json()
      request2 = get('https://some-random-api.ml/facts/koala')
      factjson = request2.json()
      embed = discord.Embed(title="Koala!", color=discord.Color.purple())
      embed.set_image(url=dogjson['link'])
      embed.set_footer(text=factjson['fact'])
      await message.channel.send(embed=embed) 

  elif message.content.startswith("$fox"):
      request = get("https://some-random-api.ml/img/fox")
      dogjson = request.json()
      request2 = get('https://some-random-api.ml/facts/fox')
      factjson = request2.json()
      embed = discord.Embed(title="Fox!", color=discord.Color.purple())
      embed.set_image(url=dogjson['link'])
      embed.set_footer(text=factjson['fact'])
      await message.channel.send(embed=embed) 
  
  elif message.content.startswith("$panda"):
      request = get("https://some-random-api.ml/img/panda")
      dogjson = request.json()
      request2 = get('https://some-random-api.ml/facts/panda')
      factjson = request2.json()
      embed = discord.Embed(title="Pandas!", color=discord.Color.purple())
      embed.set_image(url=dogjson['link'])
      embed.set_footer(text=factjson['fact'])
      await message.channel.send(embed=embed) 

  elif message.content.startswith("$bird"):
      request = get("https://some-random-api.ml/img/bird")
      dogjson = request.json()
      request2 = get('https://some-random-api.ml/facts/bird')
      factjson = request2.json()
      embed = discord.Embed(title="Birds!", color=discord.Color.purple())
      embed.set_image(url=dogjson['link'])
      embed.set_footer(text=factjson['fact'])
      await message.channel.send(embed=embed) 

  elif message.content.startswith("$dog"):
      request = get("https://some-random-api.ml/img/dog")
      dogjson = request.json()
      request2 = get('https://some-random-api.ml/facts/dog')
      factjson = request2.json()
      embed = discord.Embed(title="Doggo!", color=discord.Color.purple())
      embed.set_image(url=dogjson['link'])
      embed.set_footer(text=factjson['fact'])
      await message.channel.send(embed=embed)

  elif message.content.startswith("$cat"):
      request = get("https://some-random-api.ml/img/cat")
      dogjson = request.json()
      request2 = get('https://some-random-api.ml/facts/cat')
      factjson = request2.json()
      embed = discord.Embed(title="Cats!", color=discord.Color.purple())
      embed.set_image(url=dogjson['link'])
      embed.set_footer(text=factjson['fact'])
      await message.channel.send(embed=embed)

  elif message.content.startswith("$profile"):
    await message.channel.send('For making your profile for JARVIS games, coins, shopping, robbing and other names feature; You have to tell your name in DM-')
    await message.author.send('Whats your name - ')
    def check(msg):
            return msg.author == message.author 
    msg = await client.wait_for("message", check=check)
    await message.author.send(f'Remember whenever i ask you your name for some of my functions you have to tell - {msg.content}')
    channel = client.get_channel(904010921037414452)
    await channel.send(f'@SuperSaaim#1731 ; New User - {msg.content}')
    await message.author.send(f'**For sometime might be it take a bit long You will not be able to use the features in which name will ask because it will take a bit time for your name to be processes; Thanks**')
    with open(f"db.txt","r") as f:
      add = str(f.read())
    with open(f"db.txt","w") as f:
      f.write(str(f"{add}, {msg.content}"))
    f= open(f"{msg.content}.txt","w+")
    f.write("0")
    f.close()
    p= open(f"{msg.content}p.txt","w+")
    p.write("")
    p.close()
    

  elif message.content.startswith("$pri"):
    channel = client.get_channel(904010921037414452)
    await channel.send('hello')


  elif message.content.startswith("$join"):
    channel = message.author.voice.channel
    await channel.connect()
  
  elif message.content.startswith("$leave"):
    await message.voice_client.disconnect()

  
  elif message.content.startswith("$membercount"):
      a=message.guild.member_count
      b=discord.Embed(title=f"Members in {message.guild.name}",description=f"**{a}**",color=discord.Color((0xffff00)))
      await message.channel.send(embed=b)

  elif message.content.startswith("$yt"):
      videos = message.content.replace("$yt ","")
      video=videos.replace(" ","+")
      search_keyword=video
      html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
      video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
      await message.channel.send("https://www.youtube.com/watch?v=" + video_ids[0])

  elif message.content.startswith("super learner"):
      await message.channel.send(file=discord.File('SuperLearners-logos.jpeg'))

  elif message.content.startswith("$hack"):
    msg = message.content.replace("$hack","")
    message = await message.channel.send(f"**[08%]**Getting The intellectual IP adress array of {msg}.... <a:hecker:913757233911848980>")
    sleep(4)
    await message.edit(content="**[14.19%]**Founded IP adress - (12K.A.442K.A1) <a:hecker:913757233911848980>")
    sleep(4)
    await message.edit(content="**[26.49%]**Finding All the passwords on his loser cheap device..... <a:hecker:913757233911848980>")
    sleep(4)
    await message.edit(content="**[38.33%]**Getting his Discord Noob profile login and password..... <a:hecker:913757233911848980>")
    sleep(4)
    await message.edit(content=f"**[46.88%]**WOO!! Founded -\nUsername - {msg} the noob\nPassword - I am loser <a:hecker:913757233911848980>")
    sleep(4)
    await message.edit(content=f"**[58.69%]**Ahh!!! I caught his last photo clicked-")
    gif = await message.channel.send("https://previews.123rf.com/images/lokki007/lokki0071711/lokki007171101154/90617254-small-donkey-on-a-country-farm.jpg")
    sleep(4)
    await gif.delete()
    await message.edit(content=f"**[65.11%]**Injecting corona virus(computer one) in to his computer.... <a:hecker:913757233911848980>")
    sleep(4)
    await message.edit(content=f"**[74.32%]**All apps are damaged including his GTA for which he gave 40000$; lol....... <a:hecker:913757233911848980>")
    sleep(4)
    await message.edit(content=f"**[86.56%]**Taking his all discord nitro emotes,his money is drowning lol <a:hecker:913757233911848980>")
    sleep(4)
    await message.edit(content=f"**[94.12%]**Posting this hacking to the internet,lol {msg} will be shocked <a:hecker:913757233911848980>")
    sleep(4)
    await message.edit(content=f"**[99.99%]**I have hacked noob {msg} <a:verified:913758031194521631>")
    sleep(3)
    await message.edit(content=f"**[100.00%]**The total,blastful,hackful,playful,cheatful,pizzafull Hacking of noob {msg} is done 😎")

  elif message.content.startswith("$speed check"):
    from PIL import Image
    words=['hero is hero', 'game is good', 'just play games', 'you might study', 'cream ice cream', 'go play basketball', 'who is best bro', 'some people eats', 'dhoni is kohli', 'never eats sweets', 'you are mad', 'have some chocolates', 'discord is great', 'mrbeast is best', 'hehe hehe hehe', 'pikabu im hero']
    word=random.choice(words)
    img = Image.open("tech.jpg")
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype("arial.ttf", 70)
    I1.text((230, 300), f"Type - {word}", fill ="white", align ="left", font=myFont)
    img.save("techy.png")
    await message.channel.send(file=discord.File('techy.png'))
    begin=time.time()
    def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in [word]
    msg = await client.wait_for("message", check=check)
    end=time.time()
    timetaken=float(end-begin)
    embed=discord.Embed(title=f"The Time taken is {timetaken} Seconds",description=f"Good you have sucessfully written '{word}' {message.author}", color=0x0000FF)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$mind read"):
    try:
      aki = akinator.Akinator()
      q = aki.start_game()
      while aki.progression <= 80:
          embed=discord.Embed(title=q + "\n(y/n/i)", color=0x00FF00) 
          await message.channel.send(embed=embed)
          def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["y", "n", "yes", "no", "i"]
          msg = await client.wait_for("message", check=check)  
          a = msg.content
          if a == "b":
              try:
                  q = aki.back()
              except akinator.CantGoBackAnyFurther:
                  pass
          else:
              q = aki.answer(a)
      aki.win()
      embed=discord.Embed(title=f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct? (y/n)", color=0x00FF00) 
      await message.channel.send("<a:ohhh:913799017090142218>")
      await message.channel.send(embed=embed)
      await message.channel.send(f"\n{aki.first_guess['absolute_picture_path']}\n\t")
      def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["y", "n"]
      msg = await client.wait_for("message", check=check)
      if msg.content=="y":
          await message.channel.send("Yay, Thanks for using me")
      else:
          await message.channel.send("Oof Sorry, Try it again later")
    except Exception:
      await message.channel.send("Oof I cant found it I loser , u win <a:bruh:913797728453132392>")

    
  elif message.content.startswith("$rm"):
    dex=message.content.replace("$rm ","")
    await message.channel.send(f"Done I will remember that; To check Your to-do list write 'to do'")
    await message.author.send(f"You have to do: {dex}")

  elif message.content.startswith("to do"):
    await message.channel.send(f"Check Your DM Master")
    await message.author.send(f"To-do 👆")
 

  elif message.content.startswith("$dex"):
    try:
      dex=message.content.replace("$dex ","")
      request = get(f"https://some-random-api.ml/pokedex?pokemon={dex}")
      do= request.json()
      icon=do['sprites']["animated"]
      meme = discord.Embed(title=f"{do['name'].capitalize()} ID: {do['id']}", description=f"**Type: {do['type']}\n\nSpecies: {do['species']}\n\nAbilities: {do['abilities']}\n\nGender: {do['gender']}\n\nHeight: {do['height']}\n\nWeight: {do['weight']}\n\nStats:\n HP - {do['stats']['hp']}\n Attack - {do['stats']['attack']}\n Defense - {do['stats']['defense']}\n Special Attack - {do['stats']['sp_atk']}\n Special Defense - {do['stats']['sp_def']}\n Speed - {do['stats']['speed']}\n Total Stats - {do['stats']['total']}\n\nEvolution line: {do['family']['evolutionLine']}\n\nDescription: {do['description']}**", Color = discord.Color.random())
      meme.set_thumbnail(url=icon)
      await message.channel.send(embed=meme)
    except Exception:
      await message.channel.send("Wrong pokemon! <a:shocked:914737685489401878>")


  elif message.content.startswith("$giveaway"):
      await message.channel.send('Whats Your name For Giveaway?')
      with open(f"db.txt","r") as f:
        nem = str(f.read())
      x = nem.split(", ")
      def check(msg):
        return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
      msg = await client.wait_for("message", check=check)
      with open(f"{msg.content}.txt","r") as f:
        coins = int(f.read())
      await message.channel.send('How many coins do u wanna give? Maximum Limit is of 50$')
      def check(msg):
        return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"]
      num = await client.wait_for("message", check=check)
      await message.channel.send('Whom do you wanna Give the coins?')
      with open(f"db.txt","r") as f:
        nem = str(f.read())
      x = nem.split(", ")
      def check(msg):
        return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
      msge = await client.wait_for("message", check=check)
      with open(f"{msge.content}.txt","r") as f:
        coins = int(f.read())
        coins+=int(num.content)
      with open(f"{msge.content}.txt","w") as f:
            f.write(str(coins))
      with open(f"{msg.content}.txt","r") as f:
          coins = int(f.read())
          coins-=int(num.content)
      with open(f"{msg.content}.txt","w") as f:
            f.write(str(coins))
      await message.channel.send(f"Done I have deposited {num.content} coins to {msge.content} ,Thanks <a:verified:913758031194521631>")
      await message.channel.send(f"{msg.content} have deposited {num.content} coins to {msge.content}")
      
        
      
  elif message.content.startswith("$cool"):
      from PIL import Image
      avenge=random.choice(avengers)
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel
      await message.channel.send("I will give a cool pitcure with the text you say to me over it, So tell me Your The text you want over it:")
      msg = await client.wait_for("message", check=check)
      await message.channel.send("Which colour do you want for text")
      msge = await client.wait_for("message", check=check)
      img = Image.open(avenge)
      I1 = ImageDraw.Draw(img)
      myFont = ImageFont.truetype("arial.ttf", 40)
      I1.text((10, 10), msg.content, fill =msge.content, align ="left", font=myFont)
      img.save("saaim.png")
      await message.channel.send('Here is Your Pitcure <a:redfire:913801056700489778>-')
      await message.channel.send(file=discord.File('saaim.png'))

  elif message.content.startswith("$filter"):
    await message.channel.send('Which Filter You wann apply- (1)Greyscale (2)Invert (3)Brightness (4)Threshold (5)Sepia (6)Red (7)Green (8)Blue (9)Blurpe')
    def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    await message.channel.send("Write The filter Number")
    msg = await client.wait_for("message", check=check)
    if msg.content == "1":
      from PIL import Image
      clientProfilePicture = message.author.avatar_url_as(format="png")
      urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/greyscale?avatar={clientProfilePicture}", 'filter.png')
      await message.channel.send(file=discord.File('filter.png'))
    elif msg.content == "2":
      from PIL import Image
      clientProfilePicture = message.author.avatar_url_as(format="png")
      urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/invert?avatar={clientProfilePicture}", 'filter.png')
      await message.channel.send(file=discord.File('filter.png'))
    elif msg.content == "3":
      from PIL import Image
      clientProfilePicture = message.author.avatar_url_as(format="png")
      urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/brightness?avatar={clientProfilePicture}", 'filter.png')
      await message.channel.send(file=discord.File('filter.png'))
    elif msg.content == "4":
      from PIL import Image
      clientProfilePicture = message.author.avatar_url_as(format="png")
      urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/threshold?avatar={clientProfilePicture}", 'filter.png')
      await message.channel.send(file=discord.File('filter.png'))
    elif msg.content == "5":
      from PIL import Image
      clientProfilePicture = message.author.avatar_url_as(format="png")
      urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/sepia?avatar={clientProfilePicture}", 'filter.png')
      await message.channel.send(file=discord.File('filter.png'))
    elif msg.content == "6":
      from PIL import Image
      clientProfilePicture = message.author.avatar_url_as(format="png")
      urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/red?avatar={clientProfilePicture}", 'filter.png')
      await message.channel.send(file=discord.File('filter.png'))
    elif msg.content == "7":
      from PIL import Image
      clientProfilePicture = message.author.avatar_url_as(format="png")
      urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/green?avatar={clientProfilePicture}", 'filter.png')
      await message.channel.send(file=discord.File('filter.png'))
    elif msg.content == "8":
      from PIL import Image
      clientProfilePicture = message.author.avatar_url_as(format="png")
      urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/blue?avatar={clientProfilePicture}", 'filter.png')
      await message.channel.send(file=discord.File('filter.png'))
    elif msg.content == "9":
      from PIL import Image
      clientProfilePicture = message.author.avatar_url_as(format="png")
      urllib.request.urlretrieve(f"https://some-random-api.ml/canvas/blurple?avatar={clientProfilePicture}", 'filter.png')
      await message.channel.send(file=discord.File('filter.png'))


  elif message.content.startswith("my id"):
    id = message.author.id
    await message.channel.send("Your ID is: "+str(id))
    emoji = "😂"
    await message.add_reaction(emoji)

  elif message.content.startswith("tuk"):
    clientProfilePicture = message.author.avatar_url

  elif message.content.startswith("my avatar"):
    clientProfilePicture = message.author.avatar_url
    emoji = "😎"
    await message.add_reaction(emoji)
    meme = discord.Embed(title=f"Avatar of {message.author}", Color = discord.Color.random()).set_image(url=clientProfilePicture)
    await message.channel.send(embed=meme)

  elif message.content.startswith("av"):
    clientProfilePicture = message.author.avatar_url_as(format="png")
    print(clientProfilePicture)
  
  elif message.content.startswith("https://tenor.com/view/please-leave-akhandanand-tripathi-kaleen-bhaiya-pankaj-tripathi-mirzapur-s2-gif-19139381"):
    if message.guild.id == 894409573765640193:
      await message.delete()
    else:
      return

  elif message.content.startswith("how to"):
      try:
          await message.channel.send("Getting information......")
          max_results = 1
          how_to = search_wikihow(message.content, max_results)
          assert len(how_to) == 1
          await message.channel.send(how_to[0].summary)
      
      except Exception:
          print("Sorry master nothing was there related to this search <a:sadcry:913755347196448799>")

  elif message.content.startswith("$test"):
      await message.channel.send('Are you having your starter pokemon?')
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["yes", "no"]
      msg = await client.wait_for("message", check=check)
      
      if msg.content == "no":
        await message.channel.send('Whats Your name Write P in last of your name?')
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["saaimp", "akulp", "gunishkap", "atharvp", "akp", "aimbotp", "pantherp", "tanmoyp", "arep", "dragonwizardhunterp", "harshitkp", "SAAIMp", "AKULp", "GUNISHKAp", "ATHARVp", "AKp", "AIMBOTp", "PANTHERp", "TANMOYp", "AREp", "DRAGONWIZARDHUNTERp", "HARSHITKp", "Saaimp", "Akulp", "Gunishkap", "Atharvp", "Akp", "Aimbotp", "Pantherp", "Tanmoyp", "Arep", "Dragonwizardhunterp", "Harshitkp", "sAaImp", "AkUlp", "GuNiShKap", "AtHaRvp", "Akp", "AiMbOtp", "PaNtHeRp", "tAnMoYp", "aRep", "DrAgOnWiZaRdHuNtErp", "HaRsHiTkp", "sAAIMp", "aKULp", "gUNISHKAp", "aTHARVp", "aKp", "aIMBOTp", "pANTHERp", "tANMOYp", "aREp", "dRAGONWIZARDHUNTERp", "hARSHITKp", "𝕾𝖚𝖕𝖊𝖗𝕾𝖆𝖆𝖎𝖒p", "~✯≼✯~ 𝔸𝕢𝕦𝕒𝕣𝕚𝕦𝕤 ~✯≽✯~p", "BZ• AKATSUKI SLAYERp", "⪓𝔗𝔤𝔱𝔞𝔪𝔞𝔫𝔤𝔞𝔪𝔢𝔯⪔p", "병호p", "! Awaitingp", "killerbhugodp", "Tejasaceprop", "tejasaceprop", "TEJASACEPROp", "tEjAsAcEpRop", "TeJaSaCePrOp", "tejasp", "TEJASp", "Tejasp", "ArmouredScorpiop", "armouredscorpiop", "EREN YEAGERp", "eren yeagerp", "rajivp", "RAJIVp", "Aditip","aditip", "ADITIp", "everyonep", "akshitp", "joyp", "tarushp", "shauryap", "bearyp", "adityap", "avikp", "paulp", "hiteshp", "navyap", "arnavp", "kiyoship", "sakshamp", "siddhantp"
            , "amazerzp", "artip", "Crimson_Clawp"]
        msge = await client.wait_for("message", check=check)
        await message.channel.send('What will you choose as Your starter Pokemon (1)Snivy (2)Charmender (3)Froakie')
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["snivy", "charmender", "froakie"]
        pokemon = await client.wait_for("message", check=check)
        with open(f"{msge.content}.txt","w") as f:
            f.write(str(pokemon.content))
        await message.channel.send(f'Ok your starter pokemon is {pokemon.content}')
        await message.channel.send("Write $pokemon again for playing")
      else:
        await message.channel.send('Whats Your name Write P in last of your name?')
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["saaimp", "akulp", "gunishkap", "atharvp", "akp", "aimbotp", "pantherp", "tanmoyp", "arep", "dragonwizardhunterp", "harshitkp", "SAAIMp", "AKULp", "GUNISHKAp", "ATHARVp", "AKp", "AIMBOTp", "PANTHERp", "TANMOYp", "AREp", "DRAGONWIZARDHUNTERp", "HARSHITKp", "Saaimp", "Akulp", "Gunishkap", "Atharvp", "Akp", "Aimbotp", "Pantherp", "Tanmoyp", "Arep", "Dragonwizardhunterp", "Harshitkp", "sAaImp", "AkUlp", "GuNiShKap", "AtHaRvp", "Akp", "AiMbOtp", "PaNtHeRp", "tAnMoYp", "aRep", "DrAgOnWiZaRdHuNtErp", "HaRsHiTkp", "sAAIMp", "aKULp", "gUNISHKAp", "aTHARVp", "aKp", "aIMBOTp", "pANTHERp", "tANMOYp", "aREp", "dRAGONWIZARDHUNTERp", "hARSHITKp", "𝕾𝖚𝖕𝖊𝖗𝕾𝖆𝖆𝖎𝖒p", "~✯≼✯~ 𝔸𝕢𝕦𝕒𝕣𝕚𝕦𝕤 ~✯≽✯~p", "BZ• AKATSUKI SLAYERp", "⪓𝔗𝔤𝔱𝔞𝔪𝔞𝔫𝔤𝔞𝔪𝔢𝔯⪔p", "병호p", "! Awaitingp", "killerbhugodp", "Tejasaceprop", "tejasaceprop", "TEJASACEPROp", "tEjAsAcEpRop", "TeJaSaCePrOp", "tejasp", "TEJASp", "Tejasp", "ArmouredScorpiop", "armouredscorpiop", "EREN YEAGERp", "eren yeagerp", "rajivp", "RAJIVp", "Aditip","aditip", "ADITIp", "everyonep", "akshitp", "joyp", "bearyp", "paulp", "hiteshp", "navyap", "arnavp", "kiyoship", "sakshamp", "siddhantp"
            , "amazerzp", "MrGoodManp"]
        msg = await client.wait_for("message", check=check)
        with open(f"{msg.content}.txt","r") as f:
          pokemon = str(f.read())
        await message.channel.send(f"So your pokemons are {pokemon}")
        await message.channel.send(f"Write $adventure for adventure")
        await message.channel.send(f"Write $battle for battle with pokemon")
        await message.channel.send(f"Write $pokeball for checking your pokeball")
        if pokemon == "snivy":
          await message.channel.send(f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/495.png")
        elif pokemon == "charmender":
          await message.channel.send("https://w7.pngwing.com/pngs/156/686/png-transparent-pokemon-go-pokemon-x-and-y-ash-ketchum-charmander-pokemon-background-orange-cartoon-fictional-character.png")
        else:
          await message.channel.send("https://occ-0-2433-2705.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABUjeMEsCfsePysdTZMUdb02byabGwzr7jXId1W1f6QMVYfj3bu4MqSVVilKCS36uhN-EpcrjEBMHy9QHGnNk-3Ne6Fsx.jpg?r=2dd")
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["$adventure", "$battle", "$pokeball"]
        game = await client.wait_for("message", check=check)
        if game.content == "$adventure":
          while True:
            pokemons = ["tepig", "pidgeotto", "snorlax", "sylveon", "garchomp", "hoopa", "alakazam", "ekans"]
            pk = random.choice(pokemons)
            if pk == "tepig":
              await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/498.png")
              await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
              def check(msg):
                return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["tepig", "idk", "exit"]
              tepig = await client.wait_for("message", check=check)
              if tepig.content == "tepig":
                await message.channel.send("Correct! You got this, he is tepig now tepig is added to your pokemon list")
                with open(f"{msg.content}.txt", 'a') as file1:
                  file1.write("\ntepig")
                sleep(3)
              elif tepig.content == "idk":
                await message.channel.send("Oh no! Sorry that pokemon was tepig And you couldn't gave the correct answer, You lose him, But he will come back")
                sleep(3)
              elif tepig.content == "exit":
                await message.channel.send("Ok play later")
                break
                sleep(3)

            elif pk == "pidgeotto":
              await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/017.png")
              await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
              def check(msg):
                return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["pidgeotto", "idk"]
              tepig = await client.wait_for("message", check=check)
              if tepig.content == "pidgeotto":
                await message.channel.send("Correct! You got this, he is pidgeotto now he is added to your pokemon list")
                with open(f"{msg.content}.txt", 'a') as file1:
                  file1.write("\npidgeotto")
                sleep(3)
               
              elif tepig.content == "idk":
                await message.channel.send("Oh no! Sorry that pokemon was pidgeotto And you couldn't gave the correct answer, You lose him, But he will come back")
                sleep(3)
              elif tepig.content == "exit":
                await message.channel.send("Ok play later")
                break
                sleep(3)

            elif pk == "snorlax":
              await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/143.png")
              await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
              def check(msg):
                return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["snorlax", "idk"]
              tepig = await client.wait_for("message", check=check)
              if tepig.content == "snorlax":
                await message.channel.send("Correct! You got this, he is snorlax now he is added to your pokemon list")
                with open(f"{msg.content}.txt", 'a') as file1:
                  file1.write("\nsnorlax")
                sleep(3)

              elif tepig.content == "idk":
                await message.channel.send("Oh no! Sorry that pokemon was snorlax And you couldn't gave the correct answer, You lose him, But he will come back")
                sleep(3)
              elif tepig.content == "exit":
                await message.channel.send("Ok play later")
                break
                sleep(3)
              
            elif pk == "sylveon":
              await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/700.png")
              await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
              def check(msg):
                return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["sylveon", "idk"]
              tepig = await client.wait_for("message", check=check)
              if tepig.content == "sylveon":
                await message.channel.send("Correct! You got this, he is sylveon now he is added to your pokemon list")
                with open(f"{msg.content}.txt", 'a') as file1:
                  file1.write("\nsylveon")
                sleep(3)

              elif tepig.content == "idk":
                await message.channel.send("Oh no! Sorry that pokemon was sylveon And you couldn't gave the correct answer, You lose him, But he will come back")
                sleep(3)
              elif tepig.content == "exit":
                await message.channel.send("Ok play later")
                break
                sleep(3)

            elif pk == "garchomp":
              await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/detail/445.png")
              await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
              def check(msg):
                return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["garchomp", "idk"]
              tepig = await client.wait_for("message", check=check)
              if tepig.content == "garchomp":
                await message.channel.send("Correct! You got this, he is garchomp now he is added to your pokemon list")
                with open(f"{msg.content}.txt", 'a') as file1:
                  file1.write("\ngarchomp")
                sleep(3)

              elif tepig.content == "idk":
                await message.channel.send("Oh no! Sorry that pokemon was garchomp And you couldn't gave the correct answer, You lose him, But he will come back")
                sleep(3)
              elif tepig.content == "exit":
                await message.channel.send("Ok play later")
                break
                sleep(3)

            elif pk == "hoopa":
              await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/720.png")
              await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
              def check(msg):
                return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["hoopa", "idk"]
              tepig = await client.wait_for("message", check=check)
              if tepig.content == "hoopa":
                await message.channel.send("Correct! You got this, he is hoopa now he is added to your pokemon list")
                with open(f"{msg.content}.txt", 'a') as file1:
                  file1.write("\nhoopa")
                sleep(3)

              elif tepig.content == "idk":
                await message.channel.send("Oh no! Sorry that pokemon was hoopa And you couldn't gave the correct answer, You lose him, But he will come back")
                sleep(3)
              
              elif tepig.content == "exit":
                await message.channel.send("Ok play later")
                break
                sleep(3)

            elif pk == "alakazam":
              await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/065.png")
              await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
              def check(msg):
                return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["alakazam", "idk"]
              tepig = await client.wait_for("message", check=check)
              if tepig.content == "alakazam":
                await message.channel.send("Correct! You got this, he is alakazam now he is added to your pokemon list")
                with open(f"{msg.content}.txt", 'a') as file1:
                  file1.write("\nalakazam")
                sleep(3)

              elif tepig.content == "idk":
                await message.channel.send("Oh no! Sorry that pokemon was alakazam And you couldn't gave the correct answer, You lose him, But he will come back")
                sleep(3)
              
              elif tepig.content == "exit":
                await message.channel.send("Ok play later")
                break
                sleep(3)

            elif pk == "ekans":
              await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/023.png")
              await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
              def check(msg):
                return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["ekans", "idk"]
              tepig = await client.wait_for("message", check=check)
              if tepig.content == "ekans":
                await message.channel.send("Correct! You got this, he is ekans now he is added to your pokemon list")
                with open(f"{msg.content}.txt", 'a') as file1:
                  file1.write("\nekans")
                sleep(3)

              elif tepig.content == "idk":
                await message.channel.send("Oh no! Sorry that pokemon was ekans And you couldn't gave the correct answer, You lose him, But he will come back")
                sleep(3)
              
              elif tepig.content == "exit":
                await message.channel.send("Ok play later")
                break
                sleep(3)

            else:
                await message.channel.send("Workk")

        elif game.content == "$battle":
            await message.channel.send('Whats Your name Write P in last of your name?')
            def check(msg):
              return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["saaimp", "akulp", "gunishkap", "atharvp", "akp", "aimbotp", "pantherp", "tanmoyp", "arep", "dragonwizardhunterp", "harshitkp", "SAAIMp", "AKULp", "GUNISHKAp", "ATHARVp", "AKp", "AIMBOTp", "PANTHERp", "TANMOYp", "AREp", "DRAGONWIZARDHUNTERp", "HARSHITKp", "Saaimp", "Akulp", "Gunishkap", "Atharvp", "Akp", "Aimbotp", "Pantherp", "Tanmoyp", "Arep", "Dragonwizardhunterp", "Harshitkp", "sAaImp", "AkUlp", "GuNiShKap", "AtHaRvp", "Akp", "AiMbOtp", "PaNtHeRp", "tAnMoYp", "aRep", "DrAgOnWiZaRdHuNtErp", "HaRsHiTkp", "sAAIMp", "aKULp", "gUNISHKAp", "aTHARVp", "aKp", "aIMBOTp", "pANTHERp", "tANMOYp", "aREp", "dRAGONWIZARDHUNTERp", "hARSHITKp", "𝕾𝖚𝖕𝖊𝖗𝕾𝖆𝖆𝖎𝖒p", "~✯≼✯~ 𝔸𝕢𝕦𝕒𝕣𝕚𝕦𝕤 ~✯≽✯~p", "BZ• AKATSUKI SLAYERp", "⪓𝔗𝔤𝔱𝔞𝔪𝔞𝔫𝔤𝔞𝔪𝔢𝔯⪔p", "병호p", "! Awaitingp", "killerbhugodp", "Tejasaceprop", "tejasaceprop", "TEJASACEPROp", "tEjAsAcEpRop", "TeJaSaCePrOp", "tejasp", "TEJASp", "Tejasp", "ArmouredScorpiop", "armouredscorpiop", "EREN YEAGERp", "eren yeagerp", "rajivp", "RAJIVp", "Aditip","aditip", "ADITIp", "everyonep", "akshitp", "joyp", "bearyp", "paulp", "navyap", "arnavp", "kiyoship", "sakshamp", "siddhantp"]
            msg = await client.wait_for("message", check=check)
            with open(f"{msg.content}.txt","r") as f:
              pokemon = str(f.read())
            await message.channel.send('Choose One of Your pokemons to battle with-')
            await message.channel.send(pokemon)
            def check(msg):
              return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["tepig", "pidgeotto", "snorlax", "sylveon", "garchomp", "hoopa", "alakazam", "ekans"]
            msge = await client.wait_for("message", check=check)
            await message.channel.send('Ok')
            if msge.content == "tepig":
              health=100
              pokemons = ["pikachu"]
              pk = random.choice(pokemons)
              if pk == "pikachu":
                await message.channel.send('The Pokemon You have to battle with is pikachu')
                while True:
                  await message.channel.send('Choose on of these attacks- tackle, ember, flame charge, smog')
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["tackle", "ember", "flame charge", "smog"]
                  phd = await client.wait_for("message", check=check)
                  if phd.content == "tackle":
                    attacks = ["electric shock", "electric ball", "iron tail", "thunder punch", "mega kick"]
                    attack=random.choice(attacks)
                    if attack == "electric shock":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used electric shock')
                      await message.channel.send(f'Electric Shock was too effectfull tackle fainted')
                      health-=30
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "electric ball":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used electric ball')
                      await message.channel.send(f'Electric ball was too effectfull tackle fainted')
                      health-=10
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "iron tail":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used Iron tail')
                      await message.channel.send(f'Iron tail was too effectfull tackle fainted')
                      health-=2
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "thunder punch":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used Thunder punch')
                      await message.channel.send(f'Thunder punch was too effectfull tackle fainted')
                      health-=19
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "mega kick":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used mega kick')
                      await message.channel.send(f'Mega kick and Tackle were resulted in no result both were equal')
                      health-=0
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
            
                  elif phd.content == "ember":
                    
                    attacks = ["electric shock", "electric ball", "iron tail", "thunder punch", "mega kick"]
                    attack=random.choice(attacks)
                    if attack == "electric shock":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used electric shock')
                      await message.channel.send(f'Ember was a good attack it affected pikachu')
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "electric ball":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used electric ball')
                      await message.channel.send(f'Electric ball was too effectfull tackle fainted')
                      health-=10
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                      
                    elif attack == "iron tail":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used Iron tail')
                      await message.channel.send(f'Iron tail was too effectfull tackle fainted')
                      health-=2
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "thunder punch":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used Thunder punch')
                      await message.channel.send(f'Thunder punch was too effectfull tackle fainted')
                      health-=5
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "mega kick":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used mega kick')
                      await message.channel.send(f'Mega kick and Tackle were resulted in no result both were equal')
                      health-=0
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                  
                  
                  elif phd.content == "flame charge":
                    
                    attacks = ["electric shock", "electric ball", "iron tail", "thunder punch", "mega kick"]
                    attack=random.choice(attacks)
                    if attack == "electric shock":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used electric shock')
                      await message.channel.send(f'Flame Charge was a effectful attack on pikachu')
                      health-=0
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                      else:
                        continue
                        
                    elif attack == "electric ball":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used electric ball')
                      await message.channel.send(f'It was a tie No one effected')
                      health-=0
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                      
                    elif attack == "iron tail":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used Iron tail')
                      await message.channel.send(f'Iron tail blocked Flame charge was not effectfull')
                      health-=15
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "thunder punch":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used Thunder punch')
                      await message.channel.send(f'Flame Charge was effectful Thunder punch not good')
                      health-=0
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "mega kick":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used mega kick')
                      await message.channel.send(f'Mega kick blocked flame charge it was a good attack')
                      health-=0
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
              
                  elif phd.content == "smog":
                    attacks = ["electric shock", "electric ball", "iron tail", "thunder punch", "mega kick"]
                    attack=random.choice(attacks)
                    if attack == "electric shock":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used electric shock')
                      await message.channel.send(f'Smog blocked electric shock it was not a good aim, Smog was succesfull')
                      health-=0
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "electric ball":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used electric ball')
                      await message.channel.send(f'Electric ball affected smog , tepig was hurted')
                      health-=10
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                      
                    elif attack == "iron tail":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used Iron tail')
                      await message.channel.send(f'It was a tie')
                      health-=5
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "thunder punch":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used Thunder punch')
                      await message.channel.send(f'smog was effectful Thunder punch not good')
                      health-=0
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                        
                    elif attack == "mega kick":
                      await message.channel.send(f'Tepig used {phd.content} and Pikachu used mega kick')
                      await message.channel.send(f'Smog didnt affected a bit pikachu did a mega kick')
                      health-=10
                      if health == 0:
                        await message.channel.send(f'Sorry tepig lose, You lost the match')
                  
                      
                  
                  







  elif message.content.startswith("my pokemon"):
      await message.channel.send('Whats Your name Write P in last of your name?')
      def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["saaimp", "akulp", "gunishkap", "atharvp", "akp", "aimbotp", "pantherp", "tanmoyp", "arep", "dragonwizardhunterp", "harshitkp", "SAAIMp", "AKULp", "GUNISHKAp", "ATHARVp", "AKp", "AIMBOTp", "PANTHERp", "TANMOYp", "AREp", "DRAGONWIZARDHUNTERp", "HARSHITKp", "Saaimp", "Akulp", "Gunishkap", "Atharvp", "Akp", "Aimbotp", "Pantherp", "Tanmoyp", "Arep", "Dragonwizardhunterp", "Harshitkp", "sAaImp", "AkUlp", "GuNiShKap", "AtHaRvp", "Akp", "AiMbOtp", "PaNtHeRp", "tAnMoYp", "aRep", "DrAgOnWiZaRdHuNtErp", "HaRsHiTkp", "sAAIMp", "aKULp", "gUNISHKAp", "aTHARVp", "aKp", "aIMBOTp", "pANTHERp", "tANMOYp", "aREp", "dRAGONWIZARDHUNTERp", "hARSHITKp", "𝕾𝖚𝖕𝖊𝖗𝕾𝖆𝖆𝖎𝖒p", "~✯≼✯~ 𝔸𝕢𝕦𝕒𝕣𝕚𝕦𝕤 ~✯≽✯~p", "BZ• AKATSUKI SLAYERp", "⪓𝔗𝔤𝔱𝔞𝔪𝔞𝔫𝔤𝔞𝔪𝔢𝔯⪔p", "병호p", "! Awaitingp", "killerbhugodp", "Tejasaceprop", "tejasaceprop", "TEJASACEPROp", "tEjAsAcEpRop", "TeJaSaCePrOp", "tejasp", "TEJASp", "Tejasp", "ArmouredScorpiop", "armouredscorpiop", "EREN YEAGERp", "eren yeagerp", "rajivp", "RAJIVp", "Aditip","aditip", "ADITIp", "everyonep", "akshitp", "joyp", "tarushp", "shauryap", "avikp", "adityap", "paulp", "navyap", "kiyoship", "sakshamp", "siddhantp"
            , "amazerzp", "artip", "Crimson_Clawp"]
      msge = await client.wait_for("message", check=check)
      with open(f"{msge.content}.txt", "r+") as file1:
        file=file1.read()
        res = len(file.split())
        embed=discord.Embed(title=f"Your Pokemons are {str(res)}-", description=f"{file}", color=0xFF5733)
        await message.channel.send(embed=embed)
     
  elif message.content.startswith("covid cases"):
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["India", "US", "Brazil", "Russia", "France", "Spain", "United Kingdom", "Turkey", "Iran", "Argentina", "Colombia", "Germany", "Indonesia", "Mexico", "Poland", "Ukraine", "South Africa", "Philippines", "Malaysia", "Peru", "Netherlands", "Iraq", "Thailand", "Czechia", "Chile", "Japan", "Canada", "Romania", "Bangladesh", "Belgium", "Israel", "Pakistan", "Sweden", "Serbia", "Portugal", "Kazakhstan", "Cuba", "Morocco", "Vietnam", "Switzerland", "Jordan", "Hungary", "Nepal", "Austria", "United Arab Emirates", "Greece", "Tunisia", "Georgia", "Lebanon", "Guatemala", "Belarus", "Bulgaria", "Costa Rica"]

      await message.channel.send("For Which Country (Write First letter of Each word in Capital)")
      
      msg = await client.wait_for("message", check=check)
      covid=Covid()
      countries = covid.list_countries()
      print(countries)

      await message.channel.send(covid.get_status_by_country_name(msg.content))

  elif message.content.startswith("what is"):
    if message.channel.id==915263140923592744:
      return
    else:
      try:
        await message.channel.send("searching...")
        answer = wikipedia.summary(message.content, sentences=2)
        await message.channel.send(answer)
      except:
        await message.channel.send("Sorry Couldnt found something related to this Master <a:sadcry:913755347196448799>")

  elif message.content.startswith("who is"):
    if message.channel.id==915263140923592744:
      return
    else:
      try:
        await message.channel.send("searching...")
        answer = wikipedia.summary(message.content, sentences=2)
        await message.channel.send(answer)
      except:
        await message.channel.send("Sorry Couldnt found something related to this Master <a:sadcry:913755347196448799>")

  elif message.content.startswith("square root of"):
    math1=message.content.replace("square root of","")
    hmmm=int(math1)
    await message.channel.send(f"The root of {hmmm} is <a:hehe:914740567848656987>" )
    await message.channel.send(math.sqrt(hmmm))

  elif message.content.startswith("cube root of"):
    math2=message.content.replace("cube root of","")
    hmmm1=int(math2)
    x = hmmm1
    cr = x ** (1./3.)
    await message.channel.send(f"The Cube root of {x} is {cr} <a:hehe:914740567848656987>")
    await message.channel.send(f"The rounded off form of cube root of {x} is {round(cr)}")


  elif message.content.startswith("$word"):
    with open(f"db.txt","r") as f:
       nem = str(f.read())
    x = nem.split(", ")
    await message.channel.send('Whats Your name?(Write in small letters)')
    def check(msg):
        return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
    msg = await client.wait_for("message", check=check)
    await message.channel.send(f"Good Luck ! {msg.content} ")
    with open(f"{msg.content}.txt","r") as f:
        coins = int(f.read())
    wordss = ['rain', "maths", "science", "computer", "apples", "giraffe", "india", "america"]
    
    word = random.choice(wordss)
    await message.channel.send("Guess the characters")
    guesses = ''
    turns = 8
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                await message.channel.send(char)
                coins+=1
            else:
                await message.channel.send("_")
                coins-=1
                failed += 1
        if failed == 0:
            await message.channel.send("You Win")
            await message.channel.send(f"The word is: {word}")
            coins+=10
            await message.channel.send('Whats Your name?(Write in small letters)')
            def check(msg):
                return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["saaim", "akul", "gunishka", "atharv", "ak", "aimbot", "panther", "tanmay", "are", "dragonwizardhunter", "harshitk", "SAAIM", "AKUL", "GUNISHKA", "ATHARV", "AK", "AIMBOT", "PANTHER", "TANMAY", "ARE", "DRAGONWIZARDHUNTER", "HARSHITK", "Saaim", "Akul", "Gunishka", "Atharv", "Ak", "Aimbot", "Panther", "tanmay", "Are", "Dragonwizardhunter", "Harshitk", "sAaIm", "AkUl", "GuNiShKa", "AtHaRv", "Ak", "AiMbOt", "PaNtHeR", "tAnMoY", "aRe", "DrAgOnWiZaRdHuNtEr", "HaRsHiTk", "sAAIM", "aKUL", "gUNISHKA", "aTHARV", "aK", "aIMBOT", "pANTHER", "tANMOY", "aRE", "dRAGONWIZARDHUNTER", "hARSHITK", "𝕾𝖚𝖕𝖊𝖗𝕾𝖆𝖆𝖎𝖒", "~✯≼✯~ 𝔸𝕢𝕦𝕒𝕣𝕚𝕦𝕤 ~✯≽✯~", "BZ• AKATSUKI SLAYER", "⪓𝔗𝔤𝔱𝔞𝔪𝔞𝔫𝔤𝔞𝔪𝔢𝔯⪔", "병호", "! Awaiting", "killerbhugod", "Tejasacepro", "tejasacepro", "TEJASACEPRO", "tEjAsAcEpRo", "TeJaSaCePrO", "tejas", "TEJAS", "Tejas", "ArmouredScorpio", "armouredscorpio", "EREN YEAGER", "eren yeager", "rajiv", "RAJIV", "Aditi","aditi", "ADITI", "everyone", "akshit", "joy", "shaurya", "tarush", "nirmay", "beary", "aditya", "avik", "paul", "hitesh", "navya", "arnav", "kiyoshi", "saksham", "siddhant"
                , "amazerz", "arti"]
            msg = await client.wait_for("message", check=check)
            await message.channel.send("Ok, Just asking.....")
            with open(f"{msg.content}.txt","w") as f:
              f.write(str(coins))
            break
        
        guess = await message.channel.send("guess a character:")
        def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        msg = await client.wait_for("message", check=check)
        guesses += msg.content 
        if msg.content not in word:
            
            turns -= 1
            await message.channel.send("Wrong")
            await message.channel.send(f"You have {turns} more guesses")
         
            if turns == 0:
                await message.channel.send("You Loose")
                
  
  elif message.content.startswith("$kill"):
    icon="https://cdn-icons.flaticon.com/png/128/782/premium/782265.png?token=exp=1638771117~hmac=bd369251dbc8dcb35b59097fff89f1e1"
    nm=message.content.replace("$kill ","")
    hehe = random.choice(killed)
    embed = discord.Embed(
      title=f"Here it is -",
      description=f"<a:fight:913759059646222346> {nm} {hehe}",
      timestamp=message.created_at,
      color=discord.Color.red()
    )
    embed.set_thumbnail(url=icon)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

  elif message.content.startswith("$ill"):
    with open(f"db.txt","r") as f:
       nem = str(f.read())
    x = nem.split(", ")
    await message.channel.send('Whom To kill Master?')
    def check(msg):
        return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
    msg = await client.wait_for("message", check=check)
    hehe = random.choice(killed)
    await message.channel.send(f"<a:fight:913759059646222346> {msg.content} {hehe}")

      
  elif message.content.startswith("$search"):
      try:
          from googlesearch import search
      except ImportError:
          print("No module named 'google' found")
      for j in search(message.content, tld="co.in", num=5, stop=5, pause=1):
        await message.channel.send(j)

  elif message.content.startswith("$poke"):
      await message.channel.send('Are you having your starter pokemon?')
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["yes", "no"]
      msg = await client.wait_for("message", check=check)
      
      if msg.content == "no":
        await message.channel.send('Whats Your name Write P in last of your name?')
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["saaimp", "akulp", "gunishkap", "atharvp", "akp", "aimbotp", "pantherp", "tanmoyp", "arep", "dragonwizardhunterp", "harshitkp", "SAAIMp", "AKULp", "GUNISHKAp", "ATHARVp", "AKp", "AIMBOTp", "PANTHERp", "TANMOYp", "AREp", "DRAGONWIZARDHUNTERp", "HARSHITKp", "Saaimp", "Akulp", "Gunishkap", "Atharvp", "Akp", "Aimbotp", "Pantherp", "Tanmoyp", "Arep", "Dragonwizardhunterp", "Harshitkp", "sAaImp", "AkUlp", "GuNiShKap", "AtHaRvp", "Akp", "AiMbOtp", "PaNtHeRp", "tAnMoYp", "aRep", "DrAgOnWiZaRdHuNtErp", "HaRsHiTkp", "sAAIMp", "aKULp", "gUNISHKAp", "aTHARVp", "aKp", "aIMBOTp", "pANTHERp", "tANMOYp", "aREp", "dRAGONWIZARDHUNTERp", "hARSHITKp", "𝕾𝖚𝖕𝖊𝖗𝕾𝖆𝖆𝖎𝖒p", "~✯≼✯~ 𝔸𝕢𝕦𝕒𝕣𝕚𝕦𝕤 ~✯≽✯~p", "BZ• AKATSUKI SLAYERp", "⪓𝔗𝔤𝔱𝔞𝔪𝔞𝔫𝔤𝔞𝔪𝔢𝔯⪔p", "병호p", "! Awaitingp", "killerbhugodp", "Tejasaceprop", "tejasaceprop", "TEJASACEPROp", "tEjAsAcEpRop", "TeJaSaCePrOp", "tejasp", "TEJASp", "Tejasp", "ArmouredScorpiop", "armouredscorpiop", "EREN YEAGERp", "eren yeagerp", "rajivp", "RAJIVp", "Aditip","aditip", "ADITIp", "everyonep", "akshitp", "joyp", "tarushp", "shauryap", "bearyp", "adityap", "avikp", "paulp", "hiteshp", "navyap", "arnavp", "kiyoship", "sakshamp", "siddhantp"
            , "amazerzp", "artip", "Crimson_Clawp", "Anmol Ranap"]
        msge = await client.wait_for("message", check=check)
        await message.channel.send('What will you choose as Your starter Pokemon (1)Snivy (2)Charmender (3)Froakie')
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["snivy", "charmender", "froakie"]
        pokemon = await client.wait_for("message", check=check)
        with open(f"{msge.content}.txt","w") as f:
            f.write(str(pokemon.content))
        await message.channel.send(f'Ok your starter pokemon is {pokemon.content}')
        await message.channel.send("Write $pokemon again for playing")
      else:
        await message.channel.send('Whats Your name?')
        with open(f"db.txt","r") as f:
          nem = str(f.read())
        x = nem.split(", ")
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
        name = await client.wait_for("message", check=check)
        with open(f"{name.content}.txt","r") as f:
          coins = int(f.read())
        await message.channel.send('Whats Your name Write P in last of your name?')
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["saaimp", "akulp", "gunishkap", "atharvp", "akp", "aimbotp", "pantherp", "tanmoyp", "arep", "dragonwizardhunterp", "harshitkp", "SAAIMp", "AKULp", "GUNISHKAp", "ATHARVp", "AKp", "AIMBOTp", "PANTHERp", "TANMOYp", "AREp", "DRAGONWIZARDHUNTERp", "HARSHITKp", "Saaimp", "Akulp", "Gunishkap", "Atharvp", "Akp", "Aimbotp", "Pantherp", "Tanmoyp", "Arep", "Dragonwizardhunterp", "Harshitkp", "sAaImp", "AkUlp", "GuNiShKap", "AtHaRvp", "Akp", "AiMbOtp", "PaNtHeRp", "tAnMoYp", "aRep", "DrAgOnWiZaRdHuNtErp", "HaRsHiTkp", "sAAIMp", "aKULp", "gUNISHKAp", "aTHARVp", "aKp", "aIMBOTp", "pANTHERp", "tANMOYp", "aREp", "dRAGONWIZARDHUNTERp", "hARSHITKp", "𝕾𝖚𝖕𝖊𝖗𝕾𝖆𝖆𝖎𝖒p", "~✯≼✯~ 𝔸𝕢𝕦𝕒𝕣𝕚𝕦𝕤 ~✯≽✯~p", "BZ• AKATSUKI SLAYERp", "⪓𝔗𝔤𝔱𝔞𝔪𝔞𝔫𝔤𝔞𝔪𝔢𝔯⪔p", "병호p", "! Awaitingp", "killerbhugodp", "Tejasaceprop", "tejasaceprop", "TEJASACEPROp", "tEjAsAcEpRop", "TeJaSaCePrOp", "tejasp", "TEJASp", "Tejasp", "ArmouredScorpiop", "armouredscorpiop", "EREN YEAGERp", "eren yeagerp", "rajivp", "RAJIVp", "Aditip","aditip", "ADITIp", "everyonep", "akshitp", "joyp", "bearyp", "adityap", "avikp", "paulp", "hiteshp", "navyap", "arnavp", "kiyoship", "sakshamp", "siddhantp"
            , "amazerzp", "artip", "Crimson_Clawp", "Anmol Ranap"]
        msg = await client.wait_for("message", check=check)
        with open(f"{msg.content}.txt","r") as f:
          pokemon = str(f.read())
        await message.channel.send(f"So your pokemons are {pokemon}")
        await message.channel.send(f"So Many types of Pokemon will appear in front of you and You have to tell correct name of that Pokemon ,if Told You get it,")
        if pokemon == "snivy":
          await message.channel.send(f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/495.png")
        elif pokemon == "charmender":
          await message.channel.send("https://w7.pngwing.com/pngs/156/686/png-transparent-pokemon-go-pokemon-x-and-y-ash-ketchum-charmander-pokemon-background-orange-cartoon-fictional-character.png")
        else:
          await message.channel.send("https://occ-0-2433-2705.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABUjeMEsCfsePysdTZMUdb02byabGwzr7jXId1W1f6QMVYfj3bu4MqSVVilKCS36uhN-EpcrjEBMHy9QHGnNk-3Ne6Fsx.jpg?r=2dd")
        await message.channel.send("You will be given infinite chances and you have to guess the pokemon and if u dont know write - 'idk' and if u dont wanna play write - 'exit'")
        await message.channel.send("Are You Ready(yes/no)")
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["yes", "no"]
        check=await client.wait_for("message", check=check)
        if check.content=="yes":
          while True:
              kk=random.randint(1,100)
              if kk<90:
                num=random.randint(1,700)
                c=pypokedex.get(dex=num)
                with open(f"db.txt","r") as f:
                  nem = str(f.read())
                with open(f"{name.content}.txt","r") as f:
                  coins = int(f.read())
                bk=get(f"https://some-random-api.ml/pokedex?pokemon={c.name}")
                b=bk.json()
                meme = discord.Embed(title=f"Name This Pokemon! (If u dont know write - idk and if u dont wanna play write - exit)", Color = discord.Color.random()).set_image(url=b['sprites']['animated'])
                await message.channel.send(embed=meme)
                def check(msg):
                  return msg.author == message.author and msg.channel == message.channel and (msg.content) in (b['name'], "idk", "exit")
                tepig = await client.wait_for("message", check=check)
                if tepig.content == b['name']:
                  await message.channel.send(f"Correct! You got this, he is {b['name']} now he is added to your pokemon list")
                  p=pypokedex.get(name=b['name'])
                  embed=discord.Embed(title=f"Info For {b['name']}-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                  await message.channel.send(embed=embed)
                  coins+=3
                  with open(f"{name.content}.txt","w") as f:
                    f.write(str(coins))
                  with open(f"{msg.content}.txt", 'a') as file1:
                    file1.write(f"\n{b['name']}")
                elif tepig.content == "idk":
                  await message.channel.send(f"Oh no! Sorry that pokemon was {b['name']} And you couldn't gave the correct answer, You lose him, But he will come back")
                elif tepig.content == "exit":
                  await message.channel.send("Ok play later")
                  break
              else:
                pokemons = ["tepig", "pidgeotto", "snorlax", "sylveon", "garchomp", "hoopa", "alakazam", "ekans", "floette", "spritzee", "trapinch", "ledian", "klang", "scraggy", "onix", "slugma", "rockruff", "mankey", "glalie", "shroomish", "gabite", "shiftry", "geodude"]
                pk = random.choice(pokemons)
                if pk == "geodude":
                  num=random.randint(1,800)
                  c=pypokedex.get(dex=num)
                  with open(f"db.txt","r") as f:
                    nem = str(f.read())
                  with open(f"{name.content}.txt","r") as f:
                    coins = int(f.read())
                  bk=get(f"https://some-random-api.ml/pokedex?pokemon={c.name}")
                  b=bk.json()
                  meme = discord.Embed(title=f"Name This Pokemon!", Color = discord.Color.random()).set_image(url=b['sprites']['animated'])
                  await message.channel.send(embed=meme)
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in (b['name'], "idk", "exit")
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == b['name']:
                    await message.channel.send(f"Correct! You got this, he is {b['name']} now he is added to your pokemon list")
                    p=pypokedex.get(name=b['name'])
                    embed=discord.Embed(title=f"Info For {b['name']}-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write(f"\n{b['name']}")
                  elif tepig.content == "idk":
                    await message.channel.send(f"Oh no! Sorry that pokemon was {b['name']} And you couldn't gave the correct answer, You lose him, But he will come back")
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                elif pk == "geodude":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/074.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["geodude", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "geodude":
                    await message.channel.send("Correct! You got this, he is geodude now geodude is added to your pokemon list")
                    p=pypokedex.get(name="geodude")
                    embed=discord.Embed(title="Info For geodude-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\ngeodude")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was geodude And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "shiftry":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/275.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["shiftry", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "shiftry":
                    await message.channel.send("Correct! You got this, he is shiftry now shiftry is added to your pokemon list")
                    p=pypokedex.get(name="shiftry")
                    embed=discord.Embed(title="Info For shiftry-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nshiftry")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was shiftry And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "gabite":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/444.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["gabite", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "gabite":
                    await message.channel.send("Correct! You got this, he is gabite now gabite is added to your pokemon list")
                    p=pypokedex.get(name="gabite")
                    embed=discord.Embed(title="Info For gabite-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\ngabite")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was gabite And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "shroomish":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/285.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["shroomish", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "shroomish":
                    await message.channel.send("Correct! You got this, he is shroomish now shroomish is added to your pokemon list")
                    p=pypokedex.get(name="shroomish")
                    embed=discord.Embed(title="Info For shroomish-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nshroomish")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was shroomish And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "glalie":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/362.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["glalie", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "glalie":
                    await message.channel.send("Correct! You got this, he is glalie now glalie is added to your pokemon list")
                    p=pypokedex.get(name="glalie")
                    embed=discord.Embed(title="Info For glalie-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nglalie")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was glalie And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "mankey":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/056.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["mankey", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "mankey":
                    await message.channel.send("Correct! You got this, he is mankey now mankey is added to your pokemon list")
                    p=pypokedex.get(name="mankey")
                    embed=discord.Embed(title="Info For mankey-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nmankey")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was mankey And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "rockruff":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/744.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["rockruff", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "rockruff":
                    await message.channel.send("Correct! You got this, he is rockruff now rockruff is added to your pokemon list")
                    p=pypokedex.get(name="rockruff")
                    embed=discord.Embed(title="Info For rockruff-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nrockruff")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was rockruff And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "slugma":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/218.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["slugma", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "slugma":
                    await message.channel.send("Correct! You got this, he is slugma now slugma is added to your pokemon list")
                    p=pypokedex.get(name="slugma")
                    embed=discord.Embed(title="Info For slugma-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nslugma")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was slugma And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "onix":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/095.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["onix", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "onix":
                    await message.channel.send("Correct! You got this, he is onix now onix is added to your pokemon list")
                    p=pypokedex.get(name="onix")
                    embed=discord.Embed(title="Info For onix-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nonix")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was onix And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "scraggy":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/559.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["scraggy", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "scraggy":
                    await message.channel.send("Correct! You got this, he is scraggy now scraggy is added to your pokemon list")
                    p=pypokedex.get(name="scraggy")
                    embed=discord.Embed(title="Info For scraggy-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nscraggy")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was scraggy And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "klang":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/600.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["klang", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "klang":
                    await message.channel.send("Correct! You got this, he is klang now klang is added to your pokemon list")
                    p=pypokedex.get(name="klang")
                    embed=discord.Embed(title="Info For Klang-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nklang")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was klang And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "ledian":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/166.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["ledian", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "ledian":
                    await message.channel.send("Correct! You got this, he is ledian now ledian is added to your pokemon list")
                    p=pypokedex.get(name="ledian")
                    embed=discord.Embed(title="Info For ledian-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nledian")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was ledian And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "trapinch":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/328.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["trapinch", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "trapinch":
                    await message.channel.send("Correct! You got this, he is trapinch now trapinch is added to your pokemon list")
                    p=pypokedex.get(name="trapinch")
                    embed=discord.Embed(title="Info For trapinch-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\ntrapinch")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was trapinch And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                elif pk == "spritzee":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/682.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["spritzee", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "spritzee":
                    await message.channel.send("Correct! You got this, he is spritzee now spritzee is added to your pokemon list")
                    p=pypokedex.get(name="spritzee")
                    embed=discord.Embed(title="Info For spritzee-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nspritzee")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was spritzee And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)

                elif pk == "floette":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/670.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["floette", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "floette":
                    await message.channel.send("Correct! You got this, he is floette now floette is added to your pokemon list")
                    p=pypokedex.get(name="floette")
                    embed=discord.Embed(title="Info For floette-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nfloette")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was floette And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)

                elif pk == "tepig":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/498.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["tepig", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "tepig":
                    await message.channel.send("Correct! You got this, he is tepig now tepig is added to your pokemon list")
                    p=pypokedex.get(name="tepig")
                    embed=discord.Embed(title="Info For tepig-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\ntepig")
                    sleep(3)
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was tepig And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)

                elif pk == "pidgeotto":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/017.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["pidgeotto", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "pidgeotto":
                    await message.channel.send("Correct! You got this, he is pidgeotto now he is added to your pokemon list")
                    p=pypokedex.get(name="pidgeotto")
                    embed=discord.Embed(title="Info For pidgeotto-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\npidgeotto")
                    sleep(3)
                  
                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was pidgeotto And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)

                elif pk == "snorlax":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/143.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["snorlax", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "snorlax":
                    await message.channel.send("Correct! You got this, he is snorlax now he is added to your pokemon list")
                    p=pypokedex.get(name="snorlax")
                    embed=discord.Embed(title="Info For snorlax-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nsnorlax")
                    sleep(3)

                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was snorlax And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)
                  
                elif pk == "sylveon":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/700.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["sylveon", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "sylveon":
                    await message.channel.send("Correct! You got this, he is sylveon now he is added to your pokemon list")
                    p=pypokedex.get(name="sylveon")
                    embed=discord.Embed(title="Info For sylveon-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nsylveon")
                    sleep(3)

                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was sylveon And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)

                elif pk == "garchomp":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/detail/445.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["garchomp", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "garchomp":
                    await message.channel.send("Correct! You got this, he is garchomp now he is added to your pokemon list")
                    p=pypokedex.get(name="garchomp")
                    embed=discord.Embed(title="Info For garchomp-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\ngarchomp")
                    sleep(3)

                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was garchomp And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)

                elif pk == "hoopa":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/720.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["hoopa", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "hoopa":
                    await message.channel.send("Correct! You got this, he is hoopa now he is added to your pokemon list")
                    p=pypokedex.get(name="hoopa")
                    embed=discord.Embed(title="Info For hoopa-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nhoopa")
                    sleep(3)

                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was hoopa And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)

                elif pk == "alakazam":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/065.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["alakazam", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "alakazam":
                    await message.channel.send("Correct! You got this, he is alakazam now he is added to your pokemon list")
                    p=pypokedex.get(name="alakazam")
                    embed=discord.Embed(title="Info For alakazam-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nalakazam")
                    sleep(3)

                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was alakazam And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)

                elif pk == "ekans":
                  await message.channel.send("https://assets.pokemon.com/assets/cms2/img/pokedex/full/023.png")
                  await message.channel.send("Hey, a wild pokemon appeared if you tell the name correctly in 1 chance you got it and if you dont know the name write 'idk' or if u wanna dont play write 'exit'")
                  def check(msg):
                    return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["ekans", "idk", "exit"]
                  tepig = await client.wait_for("message", check=check)
                  if tepig.content == "ekans":
                    await message.channel.send("Correct! You got this, he is ekans now he is added to your pokemon list")
                    p=pypokedex.get(name="ekans")
                    embed=discord.Embed(title="Info For ekans-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
                    await message.channel.send(embed=embed)
                    coins+=3
                    with open(f"{name.content}.txt","w") as f:
                      f.write(str(coins))
                    with open(f"{msg.content}.txt", 'a') as file1:
                      file1.write("\nekans")
                    sleep(3)

                  elif tepig.content == "idk":
                    await message.channel.send("Oh no! Sorry that pokemon was ekans And you couldn't gave the correct answer, You lose him, But he will come back")
                    sleep(3)
                  
                  elif tepig.content == "exit":
                    await message.channel.send("Ok play later")
                    break
                    sleep(3)

                else:
                    await message.channel.send("Workk")
          else:
            await message.channel.send("Ok play later")

  elif message.content.startswith("p$clear"):
    await message.channel.send('Are you sure you wanna free all of your pokemons?')
    def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["yes", "no"]
    msg = await client.wait_for("message", check=check)
    if msg.content == "yes":
      await message.channel.send('Whats Your name Write P in last of your name?')
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["saaimp", "akulp", "gunishkap", "atharvp", "akp", "aimbotp", "pantherp", "tanmoyp", "arep", "dragonwizardhunterp", "harshitkp", "SAAIMp", "AKULp", "GUNISHKAp", "ATHARVp", "AKp", "AIMBOTp", "PANTHERp", "TANMOYp", "AREp", "DRAGONWIZARDHUNTERp", "HARSHITKp", "Saaimp", "Akulp", "Gunishkap", "Atharvp", "Akp", "Aimbotp", "Pantherp", "Tanmoyp", "Arep", "Dragonwizardhunterp", "Harshitkp", "sAaImp", "AkUlp", "GuNiShKap", "AtHaRvp", "Akp", "AiMbOtp", "PaNtHeRp", "tAnMoYp", "aRep", "DrAgOnWiZaRdHuNtErp", "HaRsHiTkp", "sAAIMp", "aKULp", "gUNISHKAp", "aTHARVp", "aKp", "aIMBOTp", "pANTHERp", "tANMOYp", "aREp", "dRAGONWIZARDHUNTERp", "hARSHITKp", "𝕾𝖚𝖕𝖊𝖗𝕾𝖆𝖆𝖎𝖒p", "~✯≼✯~ 𝔸𝕢𝕦𝕒𝕣𝕚𝕦𝕤 ~✯≽✯~p", "BZ• AKATSUKI SLAYERp", "⪓𝔗𝔤𝔱𝔞𝔪𝔞𝔫𝔤𝔞𝔪𝔢𝔯⪔p", "병호p", "! Awaitingp", "killerbhugodp", "Tejasaceprop", "tejasaceprop", "TEJASACEPROp", "tEjAsAcEpRop", "TeJaSaCePrOp", "tejasp", "TEJASp", "Tejasp", "ArmouredScorpiop", "armouredscorpiop", "EREN YEAGERp", "eren yeagerp", "rajivp", "RAJIVp", "Aditip","aditip", "ADITIp", "everyonep", "akshitp", "joyp", "tarushp", "shauryap", "bearyp", "adityap", "avikp", "paulp", "hiteshp", "navyap", "arnavp", "kiyoship", "sakshamp", "siddhantp"
          , "amazerzp", "artip"]
      msge = await client.wait_for("message", check=check)
      with open(f"{msge.content}.txt","w") as f:
        f.write(str(""))
        await message.channel.send('OK Now your pokemon list is empty now, Thanks')
    else:
      await message.channel.send('OK your choice man!')
    
    
  elif message.content.startswith("$rps"):
      with open(f"db.txt","r") as f:
        nem = str(f.read())
      x = nem.split(", ")
      await message.channel.send('Whats Your name?(Write in small letters)')
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
      msg = await client.wait_for("message", check=check)
      score=0
      totalq=5
      with open(f"{msg.content}.txt","r") as f:
        coins = int(f.read())
      
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["rock", "paper", "scissors"]
      await message.channel.send("Enter a choice (rock, paper, scissors): ")
      msg = await client.wait_for("message", check=check)

      possible_actions = ["rock", "paper", "scissors"]
      computer_action = random.choice(possible_actions)

      if msg.content == computer_action:
        await message.channel.send(f"Player Selected {computer_action} and J.A.R.V.I.S selected {computer_action}🧨")
        sleep(1)
        await message.channel.send(f"Both players selected {msg.content}. It's a tie!")
        score+=1
        coins+=2

      elif msg.content == "rock":
        if computer_action == "scissors":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You lose.")
          coins-=2 
      
      elif msg.content == "paper":
        if computer_action == "rock":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You lose.")
          coins-=2    
      
      elif msg.content == "scissors":
        if computer_action == "paper":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You lose.")
          coins-=2          

  #2nd question 
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["rock", "paper", "scissors"]
          
      await message.channel.send("Enter a choice (rock, paper, scissors): ")
      msg = await client.wait_for("message", check=check)

      possible_actions = ["rock", "paper", "scissors"]
      computer_action = random.choice(possible_actions)

      if msg.content == computer_action:
        await message.channel.send(f"Player Selected {computer_action} and J.A.R.V.I.S selected {computer_action}🧨")
        sleep(1)
        await message.channel.send(f"Both players selected {msg.content}. It's a tie!")
        score+=1
        coins+=2
     
     
      elif msg.content == "rock":
        if computer_action == "scissors":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You lose.")
      
      elif msg.content == "paper":
        if computer_action == "rock":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You lose.")
      
      elif msg.content == "scissors":
        if computer_action == "paper":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You lose.")
          coins-=2
  # 3rd question
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["rock", "paper", "scissors"]
          
      
      await message.channel.send("Enter a choice (rock, paper, scissors): ")
      msg = await client.wait_for("message", check=check)

      possible_actions = ["rock", "paper", "scissors"]
      computer_action = random.choice(possible_actions)

      if msg.content == computer_action:
        await message.channel.send(f"Player Selected {computer_action} and J.A.R.V.I.S selected {computer_action}🧨")
        sleep(1)
        await message.channel.send(f"Both players selected {msg.content}. It's a tie!")
        score+=1
        coins+=2

      elif msg.content == "rock":
        if computer_action == "scissors":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You lose.")
          coins-=2
      
      elif msg.content == "paper":
        if computer_action == "rock":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You lose.")
          coins-=2
      
      elif msg.content == "scissors":
        if computer_action == "paper":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You lose.")
          coins-=2
  #4th question
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["rock", "paper", "scissors"]
          
      
      await message.channel.send("Enter a choice (rock, paper, scissors): ")
      msg = await client.wait_for("message", check=check)

      possible_actions = ["rock", "paper", "scissors"]
      computer_action = random.choice(possible_actions)

      if msg.content == computer_action:
        await message.channel.send(f"Player Selected {computer_action} and J.A.R.V.I.S selected {computer_action}🧨")
        sleep(1)
        await message.channel.send(f"Both players selected {msg.content}. It's a tie!")
        score+=1
        coins+=2

      elif msg.content == "rock":
        if computer_action == "scissors":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You lose.")
          coins-=2
      
      elif msg.content == "paper":
        if computer_action == "rock":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You lose.")
          coins-=2
      
      elif msg.content == "scissors":
        if computer_action == "paper":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You lose.")
          coins-=2
  #5th question

      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["rock", "paper", "scissors"]
          
      
      await message.channel.send("Enter a choice (rock, paper, scissors): ")
      msg = await client.wait_for("message", check=check)

      possible_actions = ["rock", "paper", "scissors"]
      computer_action = random.choice(possible_actions)

      if msg.content == computer_action:
        await message.channel.send(f"Player Selected {computer_action} and J.A.R.V.I.S selected {computer_action}🧨")
        sleep(1)
        await message.channel.send(f"Both players selected {msg.content}. It's a tie!")
        score+=1
        coins+=2

      elif msg.content == "rock":
        if computer_action == "scissors":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You lose.")
          coins-=2
      
      elif msg.content == "paper":
        if computer_action == "rock":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Paper covers rock! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You lose.")
          coins-=2
      
      elif msg.content == "scissors":
        if computer_action == "paper":
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Scissors cuts paper! You win!")
          score+=1
          coins+=3
        else:
          await message.channel.send(f"Player Selected {msg.content} and J.A.R.V.I.S selected {computer_action}🧨")
          sleep(1)
          await message.channel.send("Rock smashes scissors! You lose.")
          coins-=2
      with open(f"db.txt","r") as f:
        nem = str(f.read())
      x = nem.split(", ")
      await message.channel.send('Whats Your name?(Write in small letters)')
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
      msg = await client.wait_for("message", check=check)
      await message.channel.send(f"Thank you for playing. {score} times you have won from J.A.R.V.I.S")
      Mark=(score/totalq)*100
      await message.channel.send(f"Your percentage is:{Mark}")
      with open(f"{msg.content}.txt","w") as f:
          f.write(str(coins))
  

  elif message.content.startswith("$dice"):
      with open(f"db.txt","r") as f:
        nem = str(f.read())
      x = nem.split(", ")
      no = random.randint(1, 6)
      po = random.randint(1, 6)
      jo = random.randint(1, 6)
      jpo = random.randint(1, 6)
      add = (no)+(po)
      addj = (jo)+(jpo)
      await message.channel.send('What is Your name of Discord Player?')
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
      msg = await client.wait_for("message", check=check)
      with open(f"{msg.content}.txt","r") as f:
        coins = int(f.read())
      await message.channel.send(f'@{msg.content} Throws their Dice.......')
      sleep(1)
      await message.channel.send(f'@{msg.content} gets {no} and {po}...')
      sleep(1)
      await message.channel.send(f"Your opponent J.A.R.V.I.S throws their dice... and gets {jo} and {jpo}...")
      
      if add>addj:
         await message.channel.send(f"@{msg.content} You won!!✨But I will defeat You Next time😈")
         coins+=3

      elif add==addj:
         await message.channel.send("Hehe It's a Tie!!✨But I will defeat You Next time😈")
         coins+=2
      else:
         await message.channel.send(f"Haha You Lose from Me @{msg.content}!!!😈")
         coins-=2
      with open(f"{msg.content}.txt","w") as f:
          f.write(str(coins))

  elif message.content.startswith("$roulette"):
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["continue"]
      score = 0
      chosen = random.randint(1, 10)
      given = random.randint(1, 10)
      await message.channel.send("😣🔫Player Risks His life and Pulls the Trigger......")
      
      if chosen > given:
        await message.channel.send("☠Oh The bullet came towards your head ,You are Dead now!!!! You lose🔥")
      
        
      else:
        await message.channel.send("🥵Oh The bullet did'nt came You are Safe!!!! Type continue to again risk your life ")
        score = +1

      msg = await client.wait_for("message",check=check)
      
      if msg.content == "continue":
        while True:
          def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content) in ["continue"]
      
          chosen = random.randint(1, 10)
          given = random.randint(1, 10)
          await message.channel.send("😣🔫Player Risks His life and Pulls the Trigger......")
          
          if chosen > given:
            await message.channel.send("☠Oh The bullet came towards your head ,You are Dead now!!!! You lose🔥")
            break
            
          else:
            await message.channel.send("🥵Oh The bullet did'nt came You are Safe!!!! Type continue to again risk your life ")
            score = +1

          msg = await client.wait_for("message",check=check)
            
  elif message.content.startswith("test"):
    num=random.randint(1,800)
    c=pypokedex.get(dex=num)
    with open(f"db.txt","r") as f:
       nem = str(f.read())
    x = nem.split(", ")
    await message.channel.send('Whats Your name?(Write in small letters)')
    def check(msg):
        return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
    name = await client.wait_for("message", check=check)
    with open(f"{name.content}.txt","r") as f:
      coins = int(f.read())
    bk=get(f"https://some-random-api.ml/pokedex?pokemon={c.name}")
    b=bk.json()
    meme = discord.Embed(title=f"Name This Pokemon!", Color = discord.Color.random()).set_image(url=b['sprites']['animated'])
    await message.channel.send(embed=meme)
    def check(msg):
      return msg.author == message.author and msg.channel == message.channel and (msg.content) in (b['name'], "idk", "exit")
    tepig = await client.wait_for("message", check=check)
    if tepig.content == b['name']:
      await message.channel.send(f"Correct! You got this, he is {b['name']} now he is added to your pokemon list")
      p=pypokedex.get(name=b['name'])
      embed=discord.Embed(title=f"Info For {b['name']}-", description=f"His name is {p.name}\nIts weight is {p.weight} grams\nIts height is {p.height} cm\nIts type is {p.types}\nIts stats are {p.base_stats}", color=0xFF5733)
      await message.channel.send(embed=embed)
      coins+=3
      with open(f"{name.content}.txt","w") as f:
        f.write(str(coins))
    elif tepig.content == "idk":
      await message.channel.send(f"Oh no! Sorry that pokemon was {b['name']} And you couldn't gave the correct answer, You lose him, But he will come back")
    elif tepig.content == "exit":
      await message.channel.send("Ok play later")
    


  elif message.content.startswith("$guess"):
      with open(f"db.txt","r") as f:
       nem = str(f.read())
      x = nem.split(", ")
      await message.channel.send('Whats Your name?(Write in small letters)')
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
      msg = await client.wait_for("message", check=check)
      with open(f"{msg.content}.txt","r") as f:
            coins = int(f.read())
      computer = random.randint(1, 50)
      await message.channel.send('Guess my number from 1 to 50')

      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
      
      guesses = 0
      msg = await client.wait_for("message", check=check)
      guesses += 1
      
      while (msg != computer):
        if int(msg.content) == computer:
            await message.channel.send("Correct")
            await message.channel.send(f"You guessed the number in {guesses} guesses")
            coins+=10
            with open("hiscore.txt","r") as f:
                hiscore = int(f.read())
            if(guesses<hiscore):
                await message.channel.send("YOU HAVE JUST BROKEN THE HIGHSCORE 😎")
                coins+=20
            break
       
        else:
            if(int(msg.content)>computer):
                await message.channel.send("You guessed it wrong! Enter a smaller number")
                msg = await client.wait_for("message", check=check)
                guesses += 1
                sleep(1)
            else:
                await message.channel.send("You guessed it wrong! Enter a larger nmber")
                msg = await client.wait_for("message", check=check)
                guesses += 1
                sleep(1)
      await message.channel.send('Whats Your name?(Write in small letters)')
      with open(f"db.txt","r") as f:
        nem = str(f.read())
      x = nem.split(", ")
      def check(msg):
          return msg.author == message.author and msg.channel == message.channel and (msg.content) in x
      msg = await client.wait_for("message", check=check)
      with open(f"{msg.content}.txt","w") as f:
              f.write(str(coins))
      await message.channel.send("Ok, Just asking...")
  
  elif message.content.startswith("date"):
      today = date.today()
      await message.channel.send(f"It is {today}")
      
      await message.channel.send('Done master')
      

  elif message.content.startswith("intro of jarvis"):
      await message.channel.send(file=discord.File('jarvis hero.mp4'))
      sleep(1)
      await message.channel.send("Watch it in Full-Screen")

  elif message.content.startswith("channel intro"):
      await message.channel.send(file=discord.File('CHANNEL INTRO.mp4'))

  elif message.content.startswith("python"):
      await message.channel.send(file=discord.File('python.png'))

  elif message.content.startswith("java"):
      await message.channel.send("https://www.gcreddy.com/wp-content/uploads/2021/05/Java-Programming-Language.png")
  
  elif message.content.startswith("html and css"):
      await message.channel.send("https://www.lambdatest.com/blog/wp-content/uploads/2018/11/JPG-2.jpg")
  
  
  elif message.content.startswith("rectangle"):
      await message.channel.send("Area of Rectangle is Length X Breadth")
      sleep(1)
      await message.channel.send("Perimeter of Rectangle is 2(length+Breadth)")

  elif message.content.startswith("rank jarvis"):
      await message.channel.send("I am a bot! Bots aren't invited to the super fancy /rank party. So Dont know my Rank")
  

  elif message.content.startswith("$translate english"):
      query=message.content.replace("!translate english","")
      text = Translator(from_lang="english",to_lang="french")
      texttwo = Translator(from_lang="english",to_lang="german")
      textthree = Translator(from_lang="english",to_lang="spanish")
      textfour = Translator(from_lang="english",to_lang="hindi")
      textfive = Translator(from_lang="english",to_lang="portuguese")
      result = text.translate(query)
      resulttwo = texttwo.translate(query)
      resultthree = textthree.translate(query)
      resultfour = textfour.translate(query)
      resultfive = textfive.translate(query)
      await message.channel.send(f"Translating in french - {result}")
      await message.channel.send(f"Translating in german - {resulttwo}")
      await message.channel.send(f"Translating in spanish - {resultthree}")
      await message.channel.send(f"Translating in hindi - {resultfour}")
      await message.channel.send(f"Translating in portuguese - {resultfive}")

  elif message.content.startswith("$translate portuguese"):
      query=message.content.replace("$translate portuguese ","")
      text = Translator(from_lang="portuguese",to_lang="english")
      result = text.translate(query)
      await message.channel.send(f"Translating in english - {result}")

  elif message.content.startswith("$translate hindi"):
      query=message.content.replace("!translate hindi","")
      text = Translator(from_lang="hindi",to_lang="english")
      result = text.translate(query)
      await message.channel.send(f"Translating in english - {result}")

  elif message.content.startswith("$translate spanish"):
      query=message.content.replace("!translate spanish","")
      text = Translator(from_lang="spanish",to_lang="english")
      result = text.translate(query)
      await message.channel.send(f"Translating in english - {result}")

  elif message.content.startswith("$translate german"):
      query=message.content.replace("!translate german","")
      text = Translator(from_lang="german",to_lang="english")
      result = text.translate(query)
      await message.channel.send(f"Translating in english - {result}")
      

  elif message.content.startswith("$translate french"):
      query=message.content.replace("!translate french","")
      text = Translator(from_lang="french", to_lang="english")
      result = text.translate(query)
      await message.channel.send(f"Translating in english - {result}")
      
  
  elif message.content.startswith("square"):
      await message.channel.send("Area of square is SideXSide")
      sleep(1)
      await message.channel.send("Perimeter of Square is 4 X side")
  
   
  elif message.content.startswith("circle"):
      await message.channel.send("Area of circle is πr2")
      sleep(1)
      await message.channel.send("Perimeter of circle is 2πr")

   
  elif message.content.startswith("triangle"):
      await message.channel.send("Area of triangle is Base X height/2")
      sleep(1)
      await message.channel.send("Perimeter of triangle is a+b+c")

  elif message.content.startswith("parallelogram"):
      await message.channel.send("Area of parallelogram is Base X height")
      sleep(1)
      await message.channel.send("Perimeter of parallelogram is 2(a+b)")

  elif message.content.startswith("rhombus"):
      await message.channel.send("Area of rhombus is Diagonal X Diagonal/2")
      sleep(1)
      await message.channel.send("Perimeter of rhombus is 4 X Side")
 
  elif message.content.startswith("random"):
      t6=random.choice(random2)
      await message.channel.send(t6)
      
  elif message.content.startswith("text"):
      await message.channel.send("Ok")
   
  elif message.content.startswith("train"):
      await message.channel.send("Ok")

  elif message.content.startswith("airplane"):
      await message.channel.send("Ok")
 
  elif message.content.startswith("wow"):
      take=random.choice(wow)
      await message.channel.send(take)

  elif message.content.startswith("guitar"):
      await message.channel.send("Ok")

  elif message.content.startswith("piano"):
      await message.channel.send("Ok")


  elif message.content.startswith("call"):
      await message.channel.send("Ok")

  elif message.content.startswith("sea"):
      await message.channel.send("Ok")

  elif message.content.startswith("mountain"):
      await message.channel.send("Ok")

  elif message.content.startswith("online"):
      await message.channel.send("Ok")

  elif message.content.startswith("offline"):
      await message.channel.send("Ok")

  elif message.content.startswith("pizza"):
      await message.channel.send("Ok")

  elif message.content.startswith("burger"):
      await message.channel.send("Ok")

  elif message.content.startswith("sports"):
      await message.channel.send("Ok")

  elif message.content.startswith("study"):
      await message.channel.send("Ok")

  elif message.content.startswith("fake"):
      await message.channel.send("Ok")

  elif message.content.startswith("real"):
      await message.channel.send("Ok")
  
  elif message.content.startswith("freinds"):
      await message.channel.send("Ok")

  elif message.content.startswith("parents"):
      await message.channel.send("Ok")

  elif message.content.startswith("brother"):
      await message.channel.send("Ok")

  elif message.content.startswith("sister"):
      await message.channel.send("Ok")

  elif message.content.startswith("vowels"):
      await message.channel.send("Vowels are A,E,I,O,U")
  
  elif message.content.startswith("whatsapp"):
      await message.channel.send("ok")
      
  elif message.content.startswith("discord"):
      await message.channel.send("ok")
     
  elif message.content.startswith("Murdabaad saaim"):
      await message.delete()
      await message.channel.send(f"Dont send that message @{message.author}")

  elif message.content.startswith("Saaim.  MurdabaadSaaim"):
      await message.delete()
      await message.channel.send(f"Dont send that message @{message.author}")

  elif message.content.startswith("Saaim murdabaad"):
      await message.delete()
      await message.channel.send(f"Dont send that message @{message.author}")

  elif message.content.startswith("phishing"):
      await message.delete()
      await message.channel.send(f"Dont send that message @{message.author}")

   
  elif message.content.startswith("i will hack server"):
    await message.delete()
    await message.channel.send(f"Dont send that message @{message.author}")

  elif message.content.startswith("i will hack you"):
    await message.delete()
    await message.channel.send(f"Dont send that message @{message.author}")
 
  elif message.content.startswith("i will hack this server"):
    await message.delete()
    await message.channel.send(f"Dont send that message @{message.author}")

  elif message.content.startswith("punish"):
      await message.channel.send("Hey you friend of master saaim do not dare to trouble my master Otherwise 😡 Peace is the key to the unity of world So do not fight please")
      
  
  elif message.content.startswith("trapezium"):
      await message.channel.send("Area of trapezium is (1/2) X height X (Parallel side + Parallel side)")
      sleep(1)
      await message.channel.send("Perimeter of trapezium is a+b+c+d")

  elif message.content.startswith("general quadrilateral"):
      await message.channel.send("Area of general quadrialateral is (½) × diagonal length × sum of the length of the perpendiculars drawn from the remaining two vertices")

  elif message.content.startswith("cube"):
      await message.channel.send("Lateral Surface Area of cube is 4 X side^2")
      sleep(1)
      await message.channel.send("Total Surface Area of cube is 6 X side^2")
 
  elif message.content.startswith("cuboid"):
      await message.channel.send("Lateral Surface Area of cuboid is 2h(l+b)")
      sleep(1)
      await message.channel.send("Total Surface Area of cuboid is 2(lb+bh+hl)")
 
   
  elif message.content.startswith("cylinder"):
      await message.channel.send("Lateral Surface Area of cylinder is  2πrh")
      sleep(1)
      await message.channel.send("Total Surface Area of cylinder is 2πr(r+h)")
 
  elif message.content.startswith("riddle"):
      tn=random.choice(riddle)
      await message.channel.send(tn)

  elif message.content.startswith("master saaim"):
      emoji = "🤨"
      await message.add_reaction(emoji)
      await message.channel.send("Master Saaim The legend of the world and created this masterpiece Jarvis Bot and one fully functioning Python jarvis that can execute more than 60 functions")

  elif message.content.startswith("who is saaim"):
      emoji = "🤨"
      await message.add_reaction(emoji)
      await message.channel.send("Master Saaim The legend of the world and created this masterpiece Jarvis Bot and one fully functioning Python jarvis that can execute more than 60 functions")

  elif message.content.startswith("meme"):
      emoji = "🤣"
      await message.add_reaction(emoji)
      content = get("https://meme-api.herokuapp.com/gimme?nsfw=false").text
      data = json.loads(content,)
      meme = discord.Embed(title=f"{data['title']}", url=f"{data['postLink']}",timestamp=message.created_at, Color = discord.Color.random()).set_image(url=f"{data['url']}")
      meme.set_author(name=message.author, url="https://discord.gg/w4rTPMjkWy", icon_url=message.author.avatar_url)
      await message.channel.send(embed=meme)


  elif message.content.startswith("all memes"):
      await message.channel.send("https://funvizeo.com/media/memes/1182d5e783af9a0e/power-carpayment-bankloan-money-combined-captain-poverty-6e70b9acaf1febd8-fd0aa48685ac13cf.jpg")
  
  
  elif message.content.startswith("candle"):
      await message.channel.send("Correct Answer for I’m tall when I’m young, and I’m short when I’m old. What am I?")
  
  elif message.content.startswith("sponge"):
      await message.channel.send("Correct Answer for What is full of holes but still holds water?")

  elif message.content.startswith("promise"):
      await message.channel.send("Correct Answer What can you break, even if you never pick it up or touch it?")

  elif message.content.startswith("piano"):
      await message.channel.send("Correct Answer What has many keys but can’t open a single lock?")
      
  
  
  elif message.content.startswith("time"):
      timestamp = datetime.datetime.now()   
      await message.channel.send(timestamp.strftime(r"%I:%M %p"))  

  elif message.content.startswith("sad"):
    with open(f"server.txt","r") as f:
      add = int(f.read())
    if message.guild.id==add:
      return
    else:
      emoji = "😔"
      await message.add_reaction(emoji)
      await message.channel.send(random.choice(starter_encouragements))

  elif message.content.startswith("say hi to chatbot"):
    await message.channel.send("Hello ChatBot i know you are made by master Akul and i am assistant of Master saaim  first i was a python program , who manages his all work Master saaim have shown this to akul , made by Master saaim but now i am also a discord bot. Nice to meet you I hope we will be good bots")

  elif message.content.startswith("marks"):
    await message.channel.send(f"{random.randint(1,100)}%")
  
  elif message.content.startswith("less"):
    with open(f"server.txt","r") as f:
      add = int(f.read())
    if message.guild.id==add:
      return
    else:
      await message.channel.send("REMEMBER ONE THING A PIECE OF PAPER     CANNOT DECIDE MY FUTURE🔥")

  

  elif message.content.startswith("jarvis leave for 1 minute"):
        emoji = "👊"
        await message.add_reaction(emoji)
        await message.channel.send("Ok Sir/Mam Bye I Will be back In 1 minute")
        sleep(60)
        await message.channel.send("Im back After 1 minute Master")

  elif message.content.startswith("jarvis leave for 2 minute"):
        await message.channel.send("Ok Sir/Mam Bye I Will be back In 2 minute")
        sleep(120)
        await message.channel.send("Im back After 2 minute Master")


  elif message.content.startswith("jarvis"):
    with open(f"server.txt","r") as f:
      add = int(f.read())
    if message.guild.id==add:
      return
    else:
       th=random.choice(present)
       await message.channel.send(th)

  elif message.content.startswith("story"):
      emoji = "📑"
      await message.add_reaction(emoji)
      when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
      who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
      names = ['Ali', 'Miriam','daniel', 'Hoouk','Starwalker']

      residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
      went = ['cinema', 'university','seminar', 'school', 'laundry']
      happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
      tic=(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
      await message.channel.send(tic)
  
  elif message.content.startswith("roll dice"):
    x = "y"
    
    if x == "y":
        
      no = random.randint(1,6)
        
      if no == 1:
          await message.channel.send("[-----]")
          await message.channel.send("[-----]")
          await message.channel.send("[  0  ]")
          await message.channel.send("[-----]")
          await message.channel.send("[-----]")
      if no == 2:
          await message.channel.send("[-----]")
          await message.channel.send("[ 0   ]")
          await message.channel.send("[-----]")
          await message.channel.send("[   0 ]")
          await message.channel.send("[-----]")
      elif no == 3:
          await message.channel.send("[-----]")
          await message.channel.send("[-----]")
          await message.channel.send("[0 0 0]")
          await message.channel.send("[-----]")
          await message.channel.send("[-----]")
      elif no == 4:
          await message.channel.send("[-----]")
          await message.channel.send("[0   0]")
          await message.channel.send("[-----]")
          await message.channel.send("[0   0]")
          await message.channel.send("[-----]")
      elif no == 5:
          await message.channel.send("[-----]")
          await message.channel.send("[0   0]")
          await message.channel.send("[  0  ]")
          await message.channel.send("[0   0]")
          await message.channel.send("[-----]")
      elif no == 6:
          await message.channel.send("[-----]")
          await message.channel.send("[0 0 0]")
          await message.channel.send("[-----]")
          await message.channel.send("[0 0 0]")
          await message.channel.send("[-----]")
    

  elif message.content.startswith("meaning of"):
    if message.channel.id==915263140923592744:
      return
    else:
      emoji = "📜"
      await message.add_reaction(emoji)
      try:
        from PyDictionary import PyDictionary
        op=message.content.replace("meaning of","")
        dict = PyDictionary()
        meaning = dict.meaning(op)
        await message.channel.send(meaning)
      except Exception:
        await message.channel.send("I dont know I am not a dictionary")

  elif message.content.startswith('inspire'):
    emoji = "🤩"
    await message.add_reaction(emoji)
    quote = get_quote()
    await message.channel.send(quote)
    
  
  elif message.content.startswith("joke"):
      emoji = "🤣"
      await message.add_reaction(emoji)
      try:
        request = get("https://some-random-api.ml/joke")
        dogjson = request.json()
        await message.channel.send("Here is one for you-")
        await message.channel.send(dogjson['joke'])
      except Exception:
        await message.channel.send("I am not a joker")
 
  elif message.content.startswith('tired'):
    with open(f"server.txt","r") as f:
      add = int(f.read())
    if message.guild.id==add:
      return
    else:
      emoji = "😷"
      await message.add_reaction(emoji)
      await message.channel.send("Oh! Yes you must be tired you have been working for so many Hours.Too much Work and stress makes people Tired")
    
  
  elif message.content.startswith("fact"):
    emoji = "🥳"
    await message.add_reaction(emoji)
    try:
      await message.channel.send("Here is one for you-")
      x = randfacts.get_fact(True)
      await message.channel.send(x)
    except Exception:
      await message.channel.send("I am not google")
    
  else:
    try:
     await client.process_commands(message)
    except Exception:
     await message.channel.send(f"<@{message.author.id}> Invalid Command!&%#\nCheck in `$help`")

    
client.run(TOKEN)
