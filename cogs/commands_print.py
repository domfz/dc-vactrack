import json
import os, glob

from pathlib import Path
from lxml import objectify
from xml.etree.ElementTree import fromstring, ElementTree
import lxml.etree as etree
import discord
from discord.ext import commands

class commands_print(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def list(self, ctx):
        URL_BASE = 'https://steamcommunity.com/profiles/'
        folder_path = './profiles'
        for filename in glob.glob(os.path.join(folder_path, '*.xml')):
            with open(filename, 'r') as f:
                xmlFromFile = objectify.parse(f).getroot()
                await ctx.send(f'{xmlFromFile.steamID} : {URL_BASE}{xmlFromFile.steamID64}')

    @commands.command()
    async def count(self, ctx):
        folder_path = './profiles'
        counter = 0
        for filename in glob.glob(os.path.join(folder_path, '*.xml')):
            with open(filename, 'r'):
                counter = counter + 1
        await ctx.send(f'You are currently tracking {counter} players')

    # Bot status Commands
    @commands.command(aliases=['Ping', 'Ping!', 'latency', 'ping!'])
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)} ms')

def setup(client):
    client.add_cog(commands_print(client))
