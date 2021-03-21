import discord
from discord.ext import commands

class Status(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Commands
    @commands.command(aliases=['Ping', 'Ping!', 'latency', 'ping!'])
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)} ms')

def setup(client):
    client.add_cog(Status(client))