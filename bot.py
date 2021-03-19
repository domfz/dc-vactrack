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

@client.event
async def on_ready():
    print('bot ready')

@client.command(aliases=['Ping', 'Ping!', 'latency', 'ping!'])
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def track(ctx, profileUrl):
    subprocess.check_output(f'python vactrack.py {profileUrl}', text=True, shell=True)
    await ctx.send('Player added to tracking list!')

@client.command()
async def list(ctx):
    with open('profilelist.json') as json_file:
        data = json.load(json_file)
        for p in data['players']:
            await ctx.send(p['name'])
    


client.run(TOKEN)