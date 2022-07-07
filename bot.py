import discord
import os
import requests
import json
import random
from discord import File
from discord.utils import get
from easy_pil import Editor, load_image_async, Font
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
from fun import fun
from general import general
from moderation import moderation
load_dotenv(find_dotenv())
from pets import dogs
from edu import edu
intents = discord.Intents.default()
intents.members = True

times_used = 0

client = commands.Bot(command_prefix="$", intents=intents)

client.add_cog(dogs(client))

client.add_cog(fun(client))

client.add_cog(edu(client))

client.add_cog(general(client))
 
client.add_cog(moderation(client))

@client.event
async def on_member_join(member):

  #add the channel id in which you want to send the card
  channel = client.get_channel(993803302577901590)

  pos = sum(m.joined_at < member.joined_at for m in member.guild.members if m.joined_at is not None)

  if pos == 1:
    te = "st"
  elif pos == 2:
    te = "nd"
  elif pos == 3:
    te = "rd"
  else: te = "th"

  background = Editor("pic2.jpg")
  profile_image = await load_image_async(str(member.avatar_url))

  profile = Editor(profile_image).resize((150, 150)).circle_image()
  poppins = Font.poppins(size=50, variant="bold")

  poppins_small = Font.poppins(size=20, variant="light")

  background.paste(profile, (325, 90))
  background.ellipse((325, 90), 150, 150, outline="gold", stroke_width=4)

  background.text((400, 260), f"WELCOME TO {member.guild.name}", color="white", font=poppins, align="center")
  background.text((400, 325), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
  background.text((400, 360), f"You Are The {pos}{te} Member", color="#0BE7F5", font=poppins_small, align="center")

  file = File(fp=background.image_bytes, filename="pic2.jpg")

  channel = client.get_channel(993803302577901590)
  #if you want to message more message then you can add like this
  await channel.send(f"Heya {member.mention}! Welcome To **{member.guild.name} For More Information Go To <#993803302577901590>**")

  #for sending the card
  await channel.send(file=file)

@client.event
async def on_member_remove(member):
  channel = client.get_channel(993803302577901590)

  await channel.send(f"{member.name} Has Left The server, We are going to miss you :( ")

client.run(os.environ.get("CLIENT_SECRET"))