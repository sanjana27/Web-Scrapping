import requests
from bs4 import BeautifulSoup

data= requests.get ('https://www.mycodingzone.net/blog/english')
soup=BeautifulSoup(data.text, 'html.parser')
# print(soup.prettify())
#for paras in soup.find_all('p'):   #find() only gives the first p tag element and find_all gives all the p tags elements
 #print(paras.text, end='\n')

for link in soup.find_all('a'):
    l= link.get('href')
    if l[0:3]=="../" and l!='#':
     print("https://www.mycodingzone.net/blog/english"+ l[2:len(l)])
    elif l[0]=="/" and l!='#':
      print("https://www.mycodingzone.net/blog/english"+ l)
    elif l!='#':
        print(l)
    
