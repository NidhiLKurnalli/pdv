# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 11:52:04 2020

@author: Nidhi Kurnalli
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3


conn=sqlite3.connect('NidhiLKurnalli_ML_201051015.db')
c=conn.cursor()
c.execute('''CREATE TABLE Painting(Painting_Name TEXT,Painting_Description TEXT,Painting_code TEXT)''')


pages=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
       24,25,26,27,28,29,30]

for page in pages:
  source=requests.get('http://mahuagallery.com/shop/page/{}'.format(page)).text
  soup=BeautifulSoup(source,'html.parser')

  infos=soup.find_all('div',{'class':'cmsmasters_product_inner'})
  for item in infos:
      title=item.find('h4',{'class':'cmsmasters_product_title entry-title'}).text.strip()
      description=item.find('div',{'class':'woocommerce-product-details__short-description'}).text.strip()
      paintcode=item.find('span',{'class':'sku'}).text
      c.execute('''INSERT INTO Painting VALUES(?,?,?)''',(title,description,paintcode))


conn.commit()
print('Complete')
df=pd.read_sql_query('''SELECT * FROM Painting''',conn)
results=c.fetchall()
print(df)
conn.close   