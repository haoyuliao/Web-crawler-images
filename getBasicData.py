from bs4 import BeautifulSoup
import requests
import os
import pandas as pd

#Get requests from specifc page
response = requests.get(f"https://www.ifixit.com/smartphone-repairability")
soup = BeautifulSoup(response.text, "lxml")
results = soup.find_all('div', {"class": "table parent"})

#Save dataset preparation
dataset = {}
dataset['Brand'], dataset['mode'] = [], []
dataset['year'], dataset['repairability'], dataset['link'] = [], [], []	

for i in range(len(results)):
    #Get info from each sub-class
    link = 'https://www.ifixit.com'+results[i].find('a')['href']
    brand = results[i].find('div', {"class": "cell device-name"}).getText().split()[0]
    mode = results[i].find('span', {"class": "selected"}).getText()
    year = results[i].find('span', {"class": "date"}).getText()
    rs = results[i].find('div', {"class": "cell device-score"}).find('h3').getText()
    #Save dataset
    dataset['Brand'].append(brand)
    dataset['mode'].append(mode)
    dataset['year'].append(year)
    dataset['repairability'].append(rs)
    dataset['link'].append(link)

ds = pd.DataFrame(dataset)
ds.to_excel('BasicData.xlsx', index=False)
#mydivs = soup.find_all("div", {"class": "cell image-container"})
#results
