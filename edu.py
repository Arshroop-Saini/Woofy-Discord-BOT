import discord
import requests
import json
import random
from discord.ext import commands

TriviaURL="http://jservice.io/api/random?count=1"
Quote_URL = "https://zenquotes.io/api/random"
IMAGE_URL=f'https://picsum.photos/id/{random.randint(1,1000)}/info'

class edu(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command(name='trivia')
    async def trivia(self,ctx):
        response = requests.get(TriviaURL)
        json_response= response.json()
        question= json_response[0]['question']
        answer= json_response[0]['answer']
        title= json_response[0]['category']['title']
        
        myEmbed= discord.Embed(title=title, color=0xff0000) 
        myEmbed.add_field(name="Question",value=question,inline=False)
        myEmbed.set_footer(text="Any Guesses?")
        await ctx.send(embed=myEmbed)

        def check(msg):
            return msg.content.lower()
        
        msg = await self.client.wait_for("message", check=check)
        if msg.content.lower() == answer.lower():
            await ctx.send("You got it right ✌")
        else:
            await ctx.send(f"Nah, the answer is {answer}")


    @commands.command()
    async def quote(self,context):
        response = requests.get(Quote_URL)
        json_response = response.json()
        unique_quote = json_response[0]['q']
        author_name = json_response[0]['a']

        ress= requests.get(IMAGE_URL)
        json_ress= ress.json()
        width= json_ress['width']=1500
        height= json_ress['height']=1500
        image= json_ress["download_url"]=f'https://picsum.photos/id/{random.randint(1,1000)}/{width}/{height}'

        myEmbed= discord.Embed(title="Random Quote", description="Woof!", color=0xff0000)
        myEmbed.add_field(name="Quote:",value=unique_quote,inline=False)
        myEmbed.set_thumbnail(url=image) 
        myEmbed.set_footer(text=f"Author: {author_name}")
        
        await context.send(embed=myEmbed)