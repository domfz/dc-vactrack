import requests
import xml.dom.minidom
from lxml import objectify
import sys
import json
from xml.etree.ElementTree import fromstring, ElementTree
import lxml.etree as etree
import urllib.request

PATH = 'profiles/'
URL_APPENDIX = '?xml=1'

url_base = sys.argv[1]
url = url_base + URL_APPENDIX

response = urllib.request.urlopen(url).read()
xmlFromUrl = objectify.fromstring(response)

profile = objectify.Element('profile')
profile.steamID = xmlFromUrl.steamID
profile.steamID64 = xmlFromUrl.steamID64
profile.vacBanned = xmlFromUrl.vacBanned

profileObject = etree.ElementTree(profile)

profileObject.write(f'{PATH}{profile.steamID64}.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")