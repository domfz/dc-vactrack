
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load token from env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot shizzl
client = commands.Bot(command_prefix = '.vac ')

@client.event
async def on_ready():
    print('bot ready')

@client.command(aliases=['Ping' 'Ping!', 'latency', 'ping!'])
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')
    
client.run(TOKEN)