import requests
from BeautifulSoup import BeautifulSoup 
import re

#Fetch the details of a user
r = requests.get('http://www.seeedstudio.com/wiki/Main_Page')
raw_html=r.text
soup = BeautifulSoup(''.join(raw_html))
#print soup
soup.prettify()
links=[]
for anchor in soup.findAll('a', href=True):
  links.append( anchor['href'])
l=len(links)
print l
temp=[]
for i in range(len(links)):
  if links[i][0] == '/':
    links[i]='http://www.seeedstudio.com'+links[i]
    temp.append(links[i])
links=temp
print len(links)
for i in range(len(links)):
  print links[i]
#print links
'''
titleTag = soup.html.head.titleTag
#Fetches the title name
title_name=titleTag.string[:-8]

#Follower count
follower_url='/'+title_name.replace(" ","-")+'/followers'	
follower_str=soup.find('a', href=follower_url)
#Take the follower count from span tag
follower_count=int(follower_str.contents[1].contents[0])

#Following count
following_url='/'+title_name.replace(" ","-")+'/following'	
following_str=soup.find('a', href=following_url)
#Take the follower count from span tag
following_count=int(following_str.contents[1].contents[0])
#print title_name," ",following_count," ",follower_count
y
#follower_url_list=soup.find('a', href=follower_url)

#Fetch the followers html and parse
r1 = requests.get('http://www.quora.com/'+title_name.replace(" ","-")+'/followers')
raw_html1=r1.text
soup1 = BeautifulSoup(''.join(raw_html1))
x=soup1.find("h1" )
print x.findAllNext(text=True)
'''
