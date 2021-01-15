import pandas as pd
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen
import urllib
from prettyprinter import pprint
import lxml.html as lh
import re






ur="https://medium.com/search?q="
ds=input("what ")
url=ur+ds
r=Request(url,headers={'User-Agent':'Mozilla/5.0'})
web_url = urllib.request.urlopen(r)
d=web_url.read()
soup = BeautifulSoup(d, 'html.parser')


listu=[]



bloggy = soup.find_all('div', attrs={'class':'u-paddingTop20 u-paddingBottom25 u-borderBottomLight js-block'})
i=0
for x in bloggy:

    
    author = x.find_all('a', attrs={'class':'ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken'})
    resp=x.find_all('a',attrs={'class':'button button--chromeless u-baseColor--buttonNormal'})
   
    blog=x.find_all('h3')
    try:
        desc=x.find_all('h4')
        dgg=desc[0].text
    except:
        dgg="null"
    
    tm = x.find_all('time')
    link=x.find('a', attrs={'class':"button button--smaller button--chromeless u-baseColor--buttonNormal"})
    time=x.find('span',attrs={'class':"readingTime"})
    fg=(blog[0].text,author[0].text,(dgg).replace("\xa0"," "),tm[0].text,link.get('href'),time.get('title'))
    
    listu.append(fg)
    
df=pd.DataFrame(listu)
df.columns=['Blog','Author','Description','date','link','time']




df