# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:39:43 2019

@author: luchi
"""
import urllib.request
from bs4 import BeautifulSoup

wp = urllib.request.urlopen("https://www.emag.ro/ssd-extern-samsung-t5-portabil-1-tb-usb-3-1-negru-mu-pa1t0b-eu/pd/D7VJLNBBM/")
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
#trebuie impartit la 100


len(price)
#def remove():
a = price.replace('Lei', '')
print(a)
a = float(a)
f_price = a/100

review = soup.find('div', attrs={'class':'reviews-general-rating pad-sep-xs'}).get_text(strip=True)
print(review)













