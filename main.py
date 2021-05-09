import requests
from bs4 import BeautifulSoup
import pandas as pd

page=requests.get('http://coinmarketcap.com/coins/')

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify)

#list of items of all data with  class="sc-16r8icm-0 dnwuAU"
items= soup.find_all(class_= 'sc-16r8icm-0 dnwuAU')
#print(items[0])

#name of the coin
#print(items[0].find(class_='sc-1eb5slv-0 iJjGCS').text)

#image_link of the coin
#print(items[0].find(class_='coin-logo').get('src'))

#link of the coin
fulllink= items[0].find(class_='cmc-link').get('href')
linktext= "https://coinmarketcap.com/coins" + fulllink
#print (linktext)

#list of items - name, image link, link of the coin
list_names = [item.find(class_='sc-1eb5slv-0 iJjGCS').text for item in items]
list_imagelink = [item.find(class_='coin-logo').get('src') for item in items]
list_coinlink = [item.find(class_='cmc-link').get('href') for item in items]


#forming a dictionary of this table using pandas
dictionary= pd.DataFrame(
    {
        'Name of currency': list_names, 
        'Image link': list_imagelink,
        'Coin link': list_coinlink
    }
)

#save this dict to a csv file
dictionary.to_csv('coin.csv')

