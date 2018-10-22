#!/usr/bin/env python3

import time
import webbrowser
import random
from random import shuffle
import sys

from bs4 import BeautifulSoup
import urllib.request

finalSearch = True
page = "https://en.wikipedia.org/wiki/Special:Random"
#page = "https://en.wikipedia.org/wiki/Michael_D._Higgins"
hops = 0
firstSearch = True

if(len(sys.argv) > 1):
    mode = sys.argv[1]
else:
    mode = "search"

if(mode == "search"):
    while(finalSearch):

        resp = urllib.request.urlopen(page)
        soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

        if(firstSearch):
            firstSearch = False
            print("\n\nStarting Page: " + soup.title.string)

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

        if(badLink):
            #favor the primary
            primaryLinks = [line.rstrip('\n') for line in open("primary.txt")]
            shuffle(primaryLinks)
            for i in links:
                for linkED in primaryLinks:
                    if(str(i.get('title')).replace(" ", "_") == linkED):
                        print("\nGoing to primary page: " + i.get("title"))
                        link = i
                        badLink = False
                        break

        if(badLink):
            #favor the secondary
            secondaryLinks = [line.rstrip('\n') for line in open("secondary.txt")]
            shuffle(secondaryLinks)
            for i in links:
                for linkED in secondaryLinks:
                    if(str(i.get('title')).replace(" ", "_") == linkED):
                        print("\nGoing to secondary page: " + i.get("title"))
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

            if(link.get('href') == "/wiki/Main_Page"):
                continue

            if(":" in link.get('href')):
                continue

            try:
               link.get('href') 
            except:
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
elif(mode == "primary"):
    try:
        file = open("primary.txt", 'r')
    except FileNotFoundError:
        file = open("primary.txt", 'w')

    primaryLinks = [line.rstrip('\n') for line in open("primary.txt")]
    
    for x in range(0, 50000):
        resp = urllib.request.urlopen(page)
        soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

        links = soup.find_all('a', href=True)

        for i in links:
            if(i.get('href') == "/wiki/Halloween"):
                if(soup.title.string not in links):
                    title = soup.title.string
                    title = title[:-12]
                    title = title.replace(" ", "_")
                    print("Adding: " + title)
                    with open("primary.txt", "a") as myfile:
                        myfile.write(title  + "\n")
                    break



elif (mode == "secondary"):
    try:
        file = open("secondary.txt", 'r')
    except FileNotFoundError:
        file = open("secondary.txt", 'w')

    primaryLinks = [line.rstrip('\n') for line in open("primary.txt")]
    secondaryLinks = [line.rstrip('\n') for line in open("secondary.txt")]
    
    for x in range(0, 50000):
        resp = urllib.request.urlopen(page)
        soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

        links = soup.find_all('a', href=True)

        for i in links:
            for y in primaryLinks:
                title = "The_Troubles"
                if(i.get('title') == y):
                    title = soup.title.string
                    title = title[:-12]
                    title = title.replace(" ", "_")
                if(title not in secondaryLinks):
                    print("Adding: " + title)
                    with open("secondary.txt", "a") as myfile:
                        myfile.write(title  + "\n")
                    break