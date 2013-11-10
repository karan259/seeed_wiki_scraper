import requests
from BeautifulSoup import BeautifulSoup 
import re

#Fetch the main page
main='http://www.seeedstudio.com/wiki/Main_Page'
print 'Fetching Main Page'
r = requests.get(main)
raw_html=r.text
soup = BeautifulSoup(''.join(raw_html))
links=[]

#Find links in the page
for anchor in soup.findAll('a', href=True):
  links.append( anchor['href'])
l=len(links)
temp=[]

for i in range(len(links)):
  if links[i][0] == '/':	#For searching only the Grove sensors
      links[i]='http://www.seeedstudio.com'+links[i]
      temp.append(links[i])
links=temp
print len(links),"links found"

op_file=open("all.csv", "w")

for i in range(len(links)):
  #Fetch other links
  try:
    page=requests.get(links[i])
    raw_html=page.text
    soup = BeautifulSoup(''.join(raw_html))
    print i,"of",len(links),":"
    
    #Page Title
    heading= (soup('h1',{'id':'firstHeading'})[0])
    p_head=heading('span',{'dir':'auto'})[0].string,
    p_h=str(p_head[0])
    p_h=p_h.decode("utf-8")			#Correct encoding for not ASCII characters like 02
    p_h=p_h.encode('ascii',errors='ignore')	
    print p_h
    op_file.write(p_h+';')
    
    #Page Viewcount
    str1= (soup('li',{'id':'footer-info-viewcount'})[0].string)
    matches=re.findall('\d+',str1)
    p_vc=",".join(matches)
    print p_vc
    op_file.write(p_vc+';')
    
    #print url
    p_lk=links[i]
    print p_lk,'\n'
    op_file.write(p_lk+'\n')
  except IndexError:
    print "Error"
op_file.close()
