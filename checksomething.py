import requests, bs4, re, time
from bs4 import BeautifulSoup
# import smtplib 
# import time
import winsound

def checkforfall():
    r = requests.get("url of your choice")
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    a = str(soup)
    if "any certain announcement you want to look for" in a:#at the time I looked for fall 2020 announcements on the university website
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)#store the wav file in the directory where your script is.

while(True):
    checkforfall()
    time.sleep(86400)
        



