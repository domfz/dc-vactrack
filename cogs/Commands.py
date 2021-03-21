import discord
from discord.ext import commands
import subprocess
import json
import os

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def nameOfCommand(self, ctx):
        await ctx.send('')

    @commands.command()
    async def track(self, ctx, profileUrl):
        subprocess.Popen(f'python vactrack.py {profileUrl}', text=True, shell=True)
        await ctx.send('Player added to tracking list!')

    @commands.command()
    async def list(self, ctx):
        with open('profilelist.json') as json_file:
            data = json.load(json_file)
            for p in data['players']:
                await ctx.send(p['name'])

def setup(client):
    client.add_cog(Commands(client))
