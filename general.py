import discord
import random
from discord.ext import commands
import asyncio

times_used = 0

class general(commands.Cog):
    def __init__(self,client):
        self.client=client
    


    @commands.command()
    async def ping(self,ctx):
        myEmbed= discord.Embed(color=0xC0C0C0)
        myEmbed.add_field(name="Ping",value=str(f'My ping is {self.client.latency}!'),inline=False)
        await ctx.send(embed=myEmbed)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()

        statuses=["Woofyverse", f"On {len(self.client.guilds)} Servers | $help", "discord.py", "Cat Videos"]

        while not self.client.is_closed():
            status=random.choice(statuses)
            await self.client.change_presence(activity=discord.Game(name=status))
            await asyncio.sleep(10)
        print("Ready to Woof!")



  
    
    @commands.command()
    async def used(self,ctx):
        global times_used
        myEmbed= discord.Embed(title="Used", color=0xC0C0C0)
        myEmbed.add_field(name="Times used since last reboot:",value=str(times_used),inline=False)
        await ctx.send(embed=myEmbed)
        times_used = times_used + 1
