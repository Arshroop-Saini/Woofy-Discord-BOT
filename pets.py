import discord
from discord.ext import commands
import requests
import json


DogURL="https://dog.ceo/api/breeds/image/random"
FactURL="https://www.dogfactsapi.ducnguyen.dev/api/v1/facts/?number=1"
CatFact="https://catfact.ninja/fact"
CatURL="https://api.thecatapi.com/v1/images/search"

class dogs(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.command()
    async def doggo(self, context):
        response= requests.get(DogURL)
        json_response= response.json()
        imgURL=json_response['message']
        
        responseFact= requests.get(FactURL)
        json_response_Fact= responseFact.json()
        fact= json_response_Fact['facts'][0]

        myEmbed= discord.Embed(title="Random Doggo", description="Woof!", color=0xff0000) 
        myEmbed.set_image(url=imgURL)
        myEmbed.add_field(name="🐕‍🦺🐶",value=fact,inline=False)
        myEmbed.set_footer(text="Woof!")
        await context.send(embed=myEmbed)
    
    @commands.command()
    async def cat(self,context):
        responseFact= requests.get(CatFact)
        json_response_Fact= responseFact.json()
        fact= json_response_Fact['fact']

        response= requests.get(CatURL)
        json_response= response.json()
        image= json_response[0]['url']

        myEmbed= discord.Embed(title="Random Cat", description="Purr!", color=0xff0000) 
        myEmbed.set_image(url=image)
        myEmbed.add_field(name="🐱‍👓🐈",value=fact,inline=False)
        await context.send(embed=myEmbed)
