import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = +)
client.remove_command(help)

@client.event
async def on_ready()
    print(Logged in as  + client.user.name)
    print(The announce bot is online!)

@client.command(pass_context=True)
async def announce(ctx,,message,)
    embed = discord.Embed(title=Announcement,description=message,color=0x9208ea)
    embed.set_footer(text=Made by Emanuelmpro#9999)
    await ctx.send(embed=embed)

client.run(TOKEN HERE)