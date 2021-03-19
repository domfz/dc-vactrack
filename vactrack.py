import requests
import xml.dom.minidom
import xmltodict
import sys

urlappendix = '?xml=1'

url = sys.argv[1] + urlappendix

response = requests.get(url)
content = xmltodict.parse(response.content)
 
if content['profile']['vacBanned'] == '1':
    print('Banned')
else:
    print('CleanAF')