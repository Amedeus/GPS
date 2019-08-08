#!/usr/bin/python3

import requests
import urllib.request
import time
import argparse
import sys
import json
from bs4 import BeautifulSoup
import re

pattern = re.compile("^([N|S|E|W][0-9]+°[0-9]+'[0-9\.]+'')+$")


parser = argparse.ArgumentParser(description="I need longidute and latitude. (accpted formats : DD, DMS [N|S|E|W]X°XX'XX.XX'')")
parser.add_argument("latitude", help="DD or DMS latitude in string")
parser.add_argument("longitude", help="DD or DMS longitude in string")
parser.parse_args()


lat = sys.argv[1]
lon = sys.argv[2]


def convert(dms):
	print("type DMS->DD conversion")
	print(dms)
	#EX : N7°32'43.267''
	array=dms.split('\'')
	#N7°32|43.267
	array2=array[0].split('°')
	#N7|32
	sens=array2[0][0]
	deg=array2[0][1:]
	minutes=array2[1]
	sec=array[1]
	minutes=float(minutes)
	sec=float(sec)
	tmp=(minutes+sec/60)/60
	if sens=="S" or sens=="W":
		deg="-"+deg
	dd=deg[:2]+"."+(str(tmp)[2:])
	print("|->"+dd)
	return dd

if pattern.match(lat):
	lat=convert(lat)

if pattern.match(lon):
	lon=convert(lon)



url = 'https://nominatim.openstreetmap.org/reverse.php?lat='+lat+'&lon='+lon+'&format=json'
headers = {"Accept-Language": "en-US,en;q=0.5"}

response = requests.get(url, headers=headers)
d=json.loads(response.text)

print("")

if not "address" in d:
	print("you're probably off shore")

else :
	for key in d["address"]:
		print(key+" : "+d["address"][key])

