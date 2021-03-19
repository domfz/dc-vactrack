import requests
import xml.dom.minidom
import xmltodict
import sys
import json

# Append xml to argv url profile
url_appendix = '?xml=1'
url_base = sys.argv[1]
url = url_base + url_appendix
# Parse xml to 'object'
response = requests.get(url)
content = xmltodict.parse(response.content)
 
playerName = content['profile']['steamID']
banStatus = content['profile']['vacBanned'] == '1'

profileInfo = {
    'name' : playerName,
    'banned': banStatus,
    'url': url_base
}

# Write to JSON
with open('profilelist.json') as json_file: 
    data = json.load(json_file) 
      
    temp = data['players'] 
  
    # python object to be appended 
    object = profileInfo
  
    # appending data to players
    temp.append(object) 

def write_json(data, filename='profilelist.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

write_json(data)