import csv
import requests
import json
from bs4 import BeautifulSoup as bs
import operator
import sys
import urllib
import urllib.request as ur
import json
import re
import datetime
import csv
import time
from os import system
import random
import math
from fake_useragent import UserAgent

#set user agent so they don't know this is a bot
ua = UserAgent()

#function to check price is the best and reasonable
def bestprice():
    #set random timout to not annoy the site owner
    timeout = random.randrange(240,720,1)
    #print how long it's going to wait this round
    print("-------------- " + str(timeout) + "s --------------")

    # check price is reasonable
    myprice = 12000.0
    theirprice = float(jobject['response'][1]['price_unit'])
    global latestprice
    # if it's way lower - then anounce that
    if (theirprice < myprice):
        announcement = "Time to buy, price dropped to £" + str(theirprice)
        print(announcement)
        system("say " + announcement)
    if (theirprice >= latestprice):
        announcement = "^ " + str(theirprice - latestprice)
        print(announcement)
        system("afplay up.mp3")
    else:
        announcement = "v" + str(latestprice - theirprice)
        print(announcement)
        system("afplay down.mp3")
    latestprice = theirprice
    time.sleep(timeout)

global latestprice
latestprice = 10000.0
# Do until I say stop
while(True):
    # set target api and fake user agent
    response = requests.get('https://bitbargain.co.uk/api/buy', headers={'User-Agent': ua.random})
    # grab the data as an object
    jobject = json.loads(response.content.decode('utf8'))
    # run the price checking function
    bestprice()
