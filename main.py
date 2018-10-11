#!/usr/bin/env python3

import time
import webbrowser
import random

from bs4 import BeautifulSoup
import urllib.request

finalSearch = True
page = "https://en.wikipedia.org/wiki/Main_Page"
hops = 0

while(finalSearch):

    resp = urllib.request.urlopen(page)
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

    links = soup.find_all('a', href=True)

    badLink = True
    link = ""
    hops += 1

    #favor the desired page
    for i in links:
        if(i.get('href') == "/wiki/Halloween"):
            link = i
            badLink = False
            break

    while(badLink):
        link = random.choice(links)

        if(link.get('href') == None or link.get('href') == ""):
            continue

        if(link.get('href')[:5] == "https"):
            continue

        if(link.get('href')[:5] != "/wiki"):
            continue
        
        if(link.get('title') == None or link.get('title') == ""):
            continue

        if(":" in link.get('href')):
            continue

        badLink = False

    if(link.get('href') == "/wiki/Halloween"):
        print("\n\nWE FOUND HALLOWEEN IN " + str(hops) + " HOPS")
        time.sleep(2)
        webbrowser.open("https://www.youtube.com/watch?v=PBHvJrVma8Y&feature=youtu.be&t=1s")
        time.sleep(1)
        webbrowser.open("https://en.wikipedia.org" + link.get('href'))
        exit()


    print("\n" + str(link.get('title').encode("cp437", "ignore").strip().decode('cp437')))
    print("https://en.wikipedia.org" + str(link.get('href').encode("cp437", "ignore").strip().decode('cp437')))
    page = "https://en.wikipedia.org" + link.get('href')