# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from bs4 import BeautifulSoup
import urllib.request
import time

#Replace the following url with the month of interest
r = urllib.request.urlopen("http://www.ceca.uwaterloo.ca/students/sessions.php?month_num=9&year_num=2016").read()
calendarSoup = BeautifulSoup(r, "lxml")
#print(soup.prettify())

links = []

for a in calendarSoup.find_all("a", href = True):
    links.append(a["href"])

np_links = np.array(links)
np_links = np_links[[i for i,item in enumerate(np_links) if "sessions_details.php?id=4" in item]]
print("Links cleaned")

for i in range(0, len(np_links)):
    np_links[i] = np_links[i].split("php?id=", 1)[1]

print("Indexes grabbed")

frontSep = "Changes in the schedule may occur, so please check back on day of event for most current information."
backSep = "Back to Listing"

with open('parseddata.txt', 'w') as f:
    for index in range(0,len(np_links)):
        pageSrc = urllib.request.urlopen("http://www.ceca.uwaterloo.ca/students/sessions_details.php?id=" + np_links[index]).read()
        pageSoup = BeautifulSoup(pageSrc, "lxml")
        descrip = pageSoup.get_text()
        rest = descrip.split(frontSep, 1)[1]
        rest = rest.split(backSep, 1)[0]
        f.write(rest)
        #f.write(descrip)

print("File outputted. Closing in 3 seconds")
time.sleep(3)
