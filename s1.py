import requests
from BeautifulSoup import BeautifulSoup 
import re

#Fetch the details of a user
main='http://www.seeedstudio.com/wiki/Main_Page'
print 'Fetcing Main Page'
r = requests.get(main)
raw_html=r.text
soup = BeautifulSoup(''.join(raw_html))
links=[]
for anchor in soup.findAll('a', href=True):
  links.append( anchor['href'])
l=len(links)
temp=[]
for i in range(len(links)):
  if links[i][0] == '/':
    links[i]='http://www.seeedstudio.com'+links[i]
    temp.append(links[i])
links=temp
print len(links),"links found"
print links[1]
page=requests.get(links[1])
raw_html=page.text
soup = BeautifulSoup(''.join(raw_html))
str1= (soup('li',{'id':'footer-info-viewcount'})[0].string)
matches=re.findall('\d+',str1)
print ",".join(matches)
heading= (soup('h1',{'id':'firstHeading'})[0])
print (heading('span',{'dir':'auto'})[0].string)
#for i in range(len(links)):
#  print links[i]
