import discord
from discord.ext import commands

class Start(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self.client))

def setup(client):
    client.add_cog(Start(client))