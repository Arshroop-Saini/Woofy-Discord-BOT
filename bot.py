import discord
import os
from pandas import value_counts
import requests
import json
import random
from discord import File
from easy_pil import Editor, load_image_async, Font
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
from fun import fun
from general import general
from moderation import moderation
load_dotenv(find_dotenv())
from pets import dogs
from edu import edu

times_used = 0

client = commands.Bot(command_prefix="$")

client.add_cog(dogs(client))

client.add_cog(fun(client))

client.add_cog(edu(client))

client.add_cog(general(client))
 
client.add_cog(moderation(client))

@client.event
async def on_member_join(self,member):
    channel=member.guild.system_channel

    background= Editor('pic2.jpg')
    profile_image= await load_image_async(str(member.avatar.url))
    profile=Editor(profile_image).resize((150,150)).circle_image()
    poppins= Font.poppins(size=50, variant="bold")
    poppins_small= Font.poppins(size=20, variant="light")
    background.paste(profile,(325,90))
    background.ellipse((325,90),150,150, outline="white", stroke_width=5)
    background.text((400,260), f"WELCOME TO {member.guild.name}", color="white", font=poppins, align="center")
    background.text((400,325),f"{member.name}#{member.discriminator}",color="white",font=poppins_small, align="center")

    file=File(fp=background.image_bytes,filename="pic1.jpg")
    await channel.send(f"Hello {member.mention}| Welcome to **{member.guild.name} for More Information Go To #rules**")
    await channel.send(file=file)

client.run(os.environ.get("OTkzODA3MjQ5NTM5NjE2ODcw.G8V8jS.nt5ukeU1CfEy_wUCENEPZhRXUsT6gjEyjjhEn8"))