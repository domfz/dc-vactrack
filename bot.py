import os
import subprocess
import json
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load token from env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot shizzl
client = commands.Bot(command_prefix = '.vac ')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)