import discord
from discord.ext import commands
import subprocess

class commands_track(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def track(self, ctx, profileUrl):
        subprocess.Popen(f'python save_players_xml.py {profileUrl}', text=True, shell=True)
        await ctx.send('Player added to tracking list!')

def setup(client):
    client.add_cog(commands_track(client))
