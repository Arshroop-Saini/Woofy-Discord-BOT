import discord
from discord.ext import commands
import asyncio

class moderation(commands.Cog):
    def __init__(self,client):
        self.client=client
    

# Banning Someone
    @commands.command() # uses command decorators, in this case inside a cog
    @commands.has_permissions(ban_members=True) # only people that have permissions to ban users can use this command
    async def ban(self, ctx, user: discord.Member, *, reason): # The person banning someone has to ping the user to ban, and input a reason. Remove self if you are outside a cog.
        await ctx.guild.ban(user, reason=reason) # Bans the user.
        await user.send(f"You have been banned in {ctx.guild} for {reason}") # Private messages user.
        await ctx.send(f"{user} has been successfully banned.") # messages channel to tell everyone it worked

# Blocking cuss words 
    @commands.Cog.listener()
    async def on_message(self,message):
        global bad_words
        bad_words = ["fuck", "pussy", "asshole", "chutiya", "mother fucker", "lawde"]
        for word in bad_words:
            if word in str.lower(message.content):
                await asyncio.sleep(3)
                await message.delete()

# Clearing messages
    @commands.command(aliases=['c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,*,amount=2):
        await ctx.channel.purge(limit=amount)

# Kicking Someone
    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member : discord.Member,*,reason="No reason provided"):
        await member.send(f"You have been banned in {ctx.guild} for {reason}")
        await ctx.send(f"{member} has been successfully kicked.") # messages channel to tell everyone it worked
        await member.kick(reason=reason)

# Unbanning Someone
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned: {user.mention}")
                return
        await ctx.send(member+"was not found")

# Muting Someone
    @commands.command(aliases=['m'])
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx,member : discord.Member):
        muted_role= ctx.guild.get_role(994245400049483806)

        await member.add_roles(muted_role)
        await ctx.send(member.mention+ " has been muted")

# Unmuting Someone
    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(kick_members=True)
    async def unmute(self,ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await member.send(f" you have unmutedd from: - {ctx.guild.name}")
        embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)

# Adding a channel
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def create_channel(self,ctx, channel_name):
        guild = ctx.guild
        await guild.create_text_channel(channel_name)

# Deleting a channel
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def delete_channel(self,ctx, channel_name):
        # check if the channel exists
        existing_channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        
        # if the channel exists
        if existing_channel is not None:
            await existing_channel.delete()
        # if the channel does not exist, inform the user
        else:
            await ctx.send(f'No channel named, "{channel_name}", was found')
#Bans a member for a specific number of days
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def softban(self,context, member : discord.Member, days, reason=None):
        #Asyncio uses seconds for its sleep function
        #multiplying the num of days the user enters by the num of seconds in a day
        days * 86400 
        await member.ban(reason=reason)
        await context.send(f'{member} has been softbanned')
        await asyncio.sleep(days)
        print("Time to unban")
        await member.unban()
        await context.send(f'{member} softban has finished')

#This event waits for commands to be issued, if a specific command requires a permission or arguement
#This event will be invoked to tell the user that they dont have the required permissions
#or they havent issues the command correctly

    @commands.Cog.listener()
    async def on_command_error(self,context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await context.send("Oh no! Looks like you have missed out an argument for this command.")
        if isinstance(error, commands.MissingPermissions):
            await context.send("Oh no! Looks like you Dont have the permissions for this command.")
        if isinstance(error, commands.MissingRole):
            await context.send("Oh no! Looks like you Dont have the roles for this command.")
        #bot errors
        if isinstance(error, commands.BotMissingPermissions):
            await context.send("Oh no! Looks like I Dont have the permissions for this command.")
        if isinstance(error, commands.BotMissingRole):
            await context.send("Oh no! Looks like I Dont have the roles for this command.")