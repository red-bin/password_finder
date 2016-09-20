#!/usr/bin/python2.7

import re
import requests
import sys
from pprint import pprint
from passwordmeter import test as meter_test


url = sys.argv[1]

r = requests.get(url)
resp = r.text.encode("utf8")
splittext = re.split('[ \t\'"<>]', resp)

splittext = map(str.strip, [ i for i in splittext if len(i) > 4 and len(i) < 12])
strengths = map(meter_test, splittext)

for word,strength in zip(splittext,strengths):
    strength = strength[0]
    if strength > .5:
        print word, strength

