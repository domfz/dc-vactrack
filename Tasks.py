import discord
from discord.ext import commands, tasks
import os, glob
from pathlib import Path
import urllib.request
from lxml import objectify
from xml.etree.ElementTree import fromstring, ElementTree
import lxml.etree as etree

URL_BASE = 'https://steamcommunity.com/profiles/'
URL_APPENDIX = '?xml=1'

# Tasks
@tasks.loop(minutes=60)
async def vactrack(self):
    folder_path = './profiles'
    for filename in glob.glob(os.path.join(folder_path, '*.xml')):
        with open(filename, 'r') as f:
            steamIDFromFile = (Path(filename).stem)
            
            response = urllib.request.urlopen(URL_BASE+steamIDFromFile+URL_APPENDIX).read()
            xmlFromUrl = objectify.fromstring(response)
            xmlFromFile = objectify.parse(f).getroot()
            print(f'Checking {xmlFromUrl.steamID}\'s Profile...')
            if (xmlFromUrl.vacBanned != xmlFromFile.vacBanned):
                print(f'Checking {xmlFromUrl.steamID} was banned!')
                await self.client.get_channel(822258507549638667).send(f'{xmlFromUrl.steamID} got banned!\n Check out his profile: {URL_BASE+steamIDFromFile}')
                os.remove(filename)
            else:
                print(f'✓')
