# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:52:42 2019

@author: Stef
"""

import urllib.request
from bs4 import BeautifulSoup

wp = urllib.request.urlopen("https://www.emag.ro/ssd-extern-samsung-t5-portabil-1-tb-usb-3-1-negru-mu-pa1t0b-eu/pd/D7VJLNBBM/")
page = wp.read()
print(page)

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

a = price.replace('Lei', '')
print(a)
a = float(a)
f_price = a/100

review = soup.find('div', attrs={'class':'reviews-general-rating pad-sep-xs'}).get_text(strip=True)
print


#STEFAN MAGDALIN#

txt=review.split(" ")
#am creat o lista alcatuita din elementele var. "review"

five_stars=txt[3]
five_stars=five_stars.replace(")4","")
five_stars=five_stars.replace("stele(","")
five_stars=int(five_stars)
#al III-lea element al listei reprezinta numarul de recenzii cu 5 stele.


four_stars=txt[4]
four_stars=four_stars.replace(")3","")
four_stars=four_stars.replace("stele(","")
four_stars=int(four_stars)

three_stars=txt[5]
three_stars=three_stars.replace(")2","")
three_stars=three_stars.replace("stele(","")
three_stars=int(three_stars)

two_stars=txt[6]
two_stars=two_stars.replace(")1","")
two_stars=two_stars.replace("stele(","")
two_stars=int(two_stars)

one_star=txt[7]
one_star=one_star.replace(")Detii","")
one_star=one_star.replace("stea(","")
one_star=int(one_star)

nr_recenzii=five_stars + four_stars + three_stars + two_stars + one_star
rating=(five_stars*5 + four_stars*4 + three_stars*3 +two_stars*2 + one_star* 5)/nr_recenzii

#am obtinut un numar cu 4 zecimale. Daca vrem sa utilizam un rating doar cu 2 zecimale folosim 'round'
#rating=round(rating,2)


