import json
import os, glob
import subprocess
from pathlib import Path
from lxml import objectify
from xml.etree.ElementTree import fromstring, ElementTree
import lxml.etree as etree
import discord
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def nameOfCommand(self, ctx):
        await ctx.send('')

    @commands.command()
    async def track(self, ctx, profileUrl):
        subprocess.Popen(f'python save_players_xml.py {profileUrl}', text=True, shell=True)
        await ctx.send('Player added to tracking list!')

    @commands.command()
    async def list(self, ctx):
        URL_BASE = 'https://steamcommunity.com/profiles/'
        folder_path = './profiles'
        for filename in glob.glob(os.path.join(folder_path, '*.xml')):
            with open(filename, 'r') as f:
                xmlFromFile = objectify.parse(f).getroot()
                await ctx.send(f'{xmlFromFile.steamID} : {URL_BASE}{xmlFromFile.steamID64}')

def setup(client):
    client.add_cog(Commands(client))
