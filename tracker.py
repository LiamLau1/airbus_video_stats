#!/usr/bin/python
import pandas as pd
from lxml import html
import requests

#Names as reference
names = ['Airfish', 'Seren', 'Move-ez', 'MAVERICK', 'Pandawacakra', 'The Zero Heroes', 'HKU-ARG', 'FlyLite', 'NI Aerospace', 'Waitless Technology Group']

#import dataframe
df = pd.read_csv('video_data.csv')

#scrape airbus data
page = requests.get('https://www.airbus-fyi.com/video-competition/')
tree = html.fromstring(page.content)
#This will create a list of teams:
teams = tree.xpath('//span[@class="teamname"]/text()')
#This will create a list of totals
totals = tree.xpath('//span[@class="tot"]/text()')

#create dictionary for mapping indices
dct = {'Airfish':0,'Seren':1, 'Move-ez':2,'MAVERICK':3,'Pandawacakra':4, 'The Zero Heroes':5,'HKU-ARG':6,'FlyLite':7,'NI Aerospace':8,'Waitless Technology Group':9}

# put the mapping in to a list
mapping = [dct[k] for k in teams]

# create an empty list
import numpy as np
a_list = np.empty(10, dtype=int)

for a in  mapping:
    a_list[a] = totals[mapping.index(a)]

df2 = pd.DataFrame([a_list], columns=names)
df = pd.concat([df,df2])
df.to_csv('video_data.csv', index=False)
