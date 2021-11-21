from bs4 import BeautifulSoup
import time
import csv
import requests
starturl="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser.get(starturl)
headers=["Name","Mass","Radius","Distance"]
Mt_list=[]
soup=beautifulSoup(page.content,"html.parcer")
table=soup.find_all("table")
tablerows=table[7].findall("tr")
for tr in tablerows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    Mt_list.append(row)
Star_name=[]
radius=[]
mass=[]
for i in range(1,len(Mt_list):
    star_name.append(Mt_list[i][0])
    distance.append(Mt_lsit[i][5])
    mass.append(Mt_list[i][7])
    radius.append(Mt_list[i][8])
df2=pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=['star_name','distance','mass','radius'])
df2.to_csv('Damnboey.csv')