import discord
from discord.ext import commands, tasks

class Tasks(commands.Cog):

    def __init__(self, client):
        self.client = client
    
def setup(client):
    client.add_cog(Tasks(client))
    vactrack.start(client)

# Tasks
@tasks.loop(seconds=10)
async def vactrack(self):
    print('tack track')