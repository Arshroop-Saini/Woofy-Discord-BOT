import discord
import requests
import json
import random
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

Joke_URL= 'https://v2.jokeapi.dev/joke/Any'
Meme_URL= ' https://meme-api.herokuapp.com/gimme'

class fun(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def joke(self,context):
        
        res= requests.get(Joke_URL)
        res_json= res.json()
        type= res_json['type']
        category= res_json['category']
    
        
        if type== 'single':
            joke= res_json['joke']

            jEmbed= discord.Embed(title="Random Joke", color=0x00ffff)
            jEmbed.add_field(name='Joke:',value=joke,inline=False)
            jEmbed.set_footer(text=f"Category: {category} Type: {type}")
            
            await context.send(embed=jEmbed)
        if type =='twopart':
            setup= res_json['setup']
            delivery= res_json['delivery']
            jEmbed= discord.Embed(title="Random Joke", color=0x00ffff)
            jEmbed.add_field(name='Setup:',value=setup,inline=False)
            jEmbed.add_field(name='Delivery:',value=delivery,inline=False)
            jEmbed.set_footer(text=f" Category: {category} Type: {type}")
            
            await context.send(embed=jEmbed)
        
    @commands.command()
    async def meme(self,context): 
        response= requests.get(Meme_URL)
        json = response.json()
        meme=json['url']
        author= json['author']
        subreddit= json['subreddit']

        jEmbed= discord.Embed(title="Meme", color=0xff6600)
    
        jEmbed.set_image(url=meme)
        jEmbed.add_field(name="Author:",value=author, inline=True)
        jEmbed.add_field(name="Subreddit:",value=subreddit, inline=True)
        jEmbed.set_footer(text="Woof 😂")

        await context.send(embed=jEmbed)
    
    @commands.command()
    async def bored(self,context):
        URL= 'http://www.boredapi.com/api/activity/'
        res= requests.get(URL)
        res_json= res.json()
        activity= res_json['activity']
        type= res_json['type']
        participants= res_json['participants']
        price= res_json['price']
        link= res_json['link']
        accessibility= res_json['accessibility']

        jEmbed= discord.Embed(title='Try This!', color=0x009900)
        
        jEmbed.add_field(name="Activity:", value=activity,inline=False)
        jEmbed.add_field(name='Type:',value=type,inline=False)
        jEmbed.add_field(name='Participants:',value=participants,inline=False)
        jEmbed.add_field(name='Price:',value=price,inline=False)
        jEmbed.add_field(name='Accessibility:',value=accessibility,inline=False)

        jEmbed.set_footer(text='⚒️')

        await context.send(embed=jEmbed)


    @commands.command()
    async def guessAge(self,context,name):
        name= context.message.content.replace('$guessAge ', "")
        URL=f'https://api.agify.io/?name={name}'
        response= requests.get(URL)
        response_json=response.json()
        age= response_json['age']
        count= response_json['count']

        jEmbed= discord.Embed(title='Age Calculator', color=0xcc6699)
        jEmbed.add_field(name="Name:", value=name,inline=False)
        jEmbed.add_field(name='Age:',value=age,inline=False)
        jEmbed.add_field(name='Count:',value=count,inline=False)
        jEmbed.set_footer(text='🔞')

        await context.send(embed=jEmbed)