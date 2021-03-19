import requests
import xml.dom.minidom
import xmltodict
import sys

urlappendix = '?xml=1'

url = sys.argv[1] + urlappendix

response = requests.get(url)
content = xmltodict.parse(response.content)
 
playerName = content['profile']['steamID']
banStatus = content['profile']['vacBanned'] == '1'

print(f'Player: **{playerName}**\nVACBan = **{banStatus}**')