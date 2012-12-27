#! /usr/bin/python
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import string

r = requests.get('http://malc0de.com/database/')
htdoc = r.content
soup = BeautifulSoup(htdoc)
table = soup.find("table",{"class": "prettytable"})

FORMAT = '%Y%m%d%H%M%S'
ofn = '/tmp/Malecode-Culled-Product-%s.csv' % (datetime.now().strftime(FORMAT))
g = open(ofn,"w")
for row in table.find_all('tr')[1:]:
  rec = row.find_all('td')
  date = rec[0].string
  g.write(date + ",")
  url = str(rec[1].string)
  if url not in ('None'):
    fn = string.split(string.split(url,'/')[-1],'?')[0]
    g.write(fn)
  g.write(",")
  ip = rec[2].string
  cc = rec[3].string
  asn1 = rec[4].string
  asn2 = str(rec[5].string)
  md5s = rec[6].string
  g.write(ip + "," + cc + "," + asn1 + "," + asn2 + "," + md5s + "\n")

g.close
