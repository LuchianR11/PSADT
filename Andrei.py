# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:08:32 2019

@author: Andrei
"""

import urllib.request
from bs4 import BeautifulSoup

wp = urllib.request.urlopen("https://www.emag.ro/laptop-gaming-hp-pavilion-15-cx0008nq-cu-procesor-intelr-coretm-i7-8750h-pana-la-4-10-ghz-coffee-lake-15-6-full-hd-ips-8gb-1tb-nvidiar-geforcer-gtx-1050-ti-4gb-free-dos-black-4tv12ea/pd/DXKHX4BBM/")
page = wp.read()
print(page)

##### ASA FUNCTIONEAZA #####
soup = BeautifulSoup(page, 'html.parser') 
print(soup)

name_box = soup.find('h1', attrs = {'class':'page-title'})
name = name_box.text.strip()
print(name)

old_price = soup.find('p', attrs = {'class':'product-old-price'}).get_text(strip=True)
print(old_price)

price = soup.find('p', attrs = {'class':'product-new-price'}).get_text(strip=True)
print(price)
#Trebuie inmultit cu 1000

len(price)
a = price.replace('Lei', '')
print(a)

a = float(a)
f_price = a*1000
print(a)
print(f_price)

review = soup.find('div', attrs={'class':'reviews-general-rating pad-sep-xs'}).get_text(strip=True)
print(review)
