from bs4 import BeautifulSoup
import feedparser
import re


feedurl = feedparser.parse('http://forum.lowendspirit.com/extern.php?action=feed&type=atom')
#print(feed.entries[0].title)


def visible(text):
    if re.match('<!--.*-->', str(text)):
        return False
    return True

def listfeed():
    title = []
    feedlinks = []
    feedtext = []
    feedAll = []

    for i in range(15):
        title.append(feedurl.entries[i].title)
        feedlinks.append(feedurl.entries[i].link)
        #soup = BeautifulSoup(feedurl.entries[i].description)
        #soup.replace(re.match('<!--.*-->', str(soup)), '' )
        #feedtext.append(soup) #.prettify())
        feedAll.append([feedurl.entries[i].title, feedurl.entries[i].link])


    #return (title, feedlinks, feedtext)
    return feedAll



#print(listfeed()[2])



