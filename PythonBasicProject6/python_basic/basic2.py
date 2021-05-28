#-*- coding:utf-8 -*-
import urllib.request as req
from bs4 import BeautifulSoup
from urllib import parse


fd=input("검색어 입력:")
fd=parse.quote(fd) #인코딩 
print(fd)
url=f"http://newssearch.naver.com/search.naver?where=rss&query={fd}"

res=req.urlopen(url)
soup=BeautifulSoup(res,'html.parser')
#print(soup)
data=soup.find_all("item")
for item in data:
    #print(item)
    title=item.find("title").text
    link=item.find("link").text
    #print(title)
    desc=item.find("description").text
    author=item.find("author").text
    #pubDate=item.find("pubDate").text
    
    category=item.find("category").string
    print(title)
    print(desc)
    #print(pubDate)
    print(link)
    print(category)
    print("=================================================================")