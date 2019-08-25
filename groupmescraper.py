from bs4 import BeautifulSoup
import os
import openpyxl #https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import numpy as np
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles import colors
from openpyxl.cell import Cell
import datetime
import time
import requests
from lxml import etree
import pdb
import operator
import matplotlib.pyplot as plt

def Convert(tup, di): 
    di = dict(tup) 
    return di 

with open('GroupMedata.html', 'rb') as html:
	soup = BeautifulSoup(html, "html.parser")

namelist=np.array([])
messages = soup.find_all('div',class_='nickname')
for message in messages:
	print(list(message.strings)[0])
	namelist = np.append(namelist, list(message.strings)[0])

print('Total number of messages:', namelist.shape[0])
unique_elements, counts_elements = np.unique(namelist, return_counts=True)
name_dict = dict(zip(unique_elements,counts_elements))
print(name_dict)
name_listsorted = sorted(name_dict.items(), key=operator.itemgetter(1))
name_dictsorted ={}
name_dictsorted = Convert(name_listsorted,name_dictsorted)
print(name_dictsorted)
percentage_dict = dict(zip(unique_elements, counts_elements/namelist.shape[0]))
for key in percentage_dict: 
	percentage_dict[key]=round(percentage_dict[key],3)
percentage_dict = sorted(percentage_dict.items(), key=operator.itemgetter(1))

print(percentage_dict)
names = list(name_dictsorted.keys())
values = list(name_dictsorted.values())
plt.bar(range(len(name_dictsorted)),values,tick_label=names)
plt.savefig('bar.png')
plt.show()
