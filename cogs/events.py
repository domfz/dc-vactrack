import discord
from discord.ext import commands
from Tasks import vactrack

class events(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self.client))
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Suspects'))
        vactrack.start(self)

def setup(client):
    client.add_cog(events(client))