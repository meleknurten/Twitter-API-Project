import tweepy
import argparse
import csv
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def twitter():
    consumer_key = "tgbveNsPzqrjI2S7NcIbZIHPt"
    consumer_secret = "a2t2A7UieGoLEPxGw4D630C7vIEuQFcImvJzcMs5Ur7U4v7UTU"
    access_token = "747913828076249088-MoQGSMfhQoBh3b1Xn5dIw7ZpnaTuEjG"
    access_token_secret = "ux3WyKdIZj6EU7yOP0LH53pDqsrE0ypmeK7xnFLOKEEx2"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    csvFile = open('tweets.csv', 'w')

    csvWriter = csv.writer(csvFile)

    user=api.get_user("yildiz")

    for tweet in tweepy.Cursor(api.user_timeline, screen_name = "yildiz",since="2016-07-01",until="2016-07-05").items():

        csvWriter.writerow([tweet.created_at])

def sort():
    f=open("tweets.csv","r")

    read=f.readlines()
    d=open("saat.txt","w")
    t= open("tarih.txt","w")

    for i in read:
        i=i.split(" ")[1].strip()
        d.write(i+"\n")
    for i in read:
        i=i.split(" ")[0].strip()
        t.write(i+"\n")

    d.close()
    t.close()
    m=open("tarih.txt","r")
    a=open("saat.txt","r")

    timess=a.readlines()
    datess= m.readlines()
    d={}
    t={}
    arrHour = []
    arrMin = []
    for j in timess:
        s = j.split(":")
        h = s[0].strip()
        m = s[1].strip()
        arrHour.append(h)
        arrMin.append(m)

    arrYear = []
    arrMont = []
    for j in datess:
        s = j.split("-")
        h = s[0].strip()
        m = s[1].strip()
        arrYear.append(h)
        arrMont.append(m)

    z = open("aralik.txt","w")
    z.write(str(sorted(d.items())))
    plt.plot_date(datess,arrHour)
    plt.show()
    plt.savefig("Grafik.png")

def main():
    twitter()
    sort()

main()
