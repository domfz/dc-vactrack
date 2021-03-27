import discord
from discord.ext import commands
from Tasks import vactrack

class Start(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self.client))
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Suspects'))
        vactrack.start()

def setup(client):
    client.add_cog(Start(client))