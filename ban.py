import discord
import random
import asyncio
import datetime
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')




@client.command()
@commands.has_permissions(manage_channels = True)
async def timer(ctx, seconds):
    try:
        secondint = int(seconds)
        

        await ctx.send('Once the timer ends the channel will unlock. \nStart banning anyone and everyone using `-ban @user` \nThe last person left in the server will be victorious and take the reward home.')
        
        
        message = await ctx.send(f"Ban battle starts in {seconds}")

        while True:
            secondint -= 1
            if secondint == 0:
                
                break

            await message.edit(content=f" \nBan battle starts in {secondint}")
            await asyncio.sleep(1)
        await message.edit(content=f"Channel is going to be unlocked")
        await ctx.send('@everyone Let the banning begin!')
        
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

    except ValueError:
        await ctx.send('You must enter a number')

    



@client.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now in locked.***")













@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit + 1)
        await ctx.message.delete()

@purge.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")









@client.command()
async def ban(ctx, user:discord.Member):
    await ctx.guild.ban(user)
    await ctx.channel.send(f"{ctx.author.mention} just banned {user.mention}")
    await asyncio.sleep(300)
    await ctx.guild.unban(user)
    



client.run('ODE0ODIzMTAwMDU5MzUzMDg4.YDjdJQ.q_aRRrw5yunOJxawuST-80vF0dg')