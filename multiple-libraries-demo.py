import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.devtools.v136.cache_storage import request_entries


current_page = 1
data = []
proceed = True

while(proceed):
    print('Currently scraping page ', + current_page)
    url = 'https://books.toscrape.com/catalogue/page-1.html'
    page = str(current_page) + '.html'
    page = requests.get(url)
    print(page.text)
    soup = BeautifulSoup(page.text,"html.parser")
    if(soup.title.text) == '404 not found':
        proceed = False
    else:
        all_books = soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
        for book in all_books:
            item = {}
            item['title'] = book.find('img').attrs['alt']
            item['Link'] = 'https://books.toscrape.com/catalogue/' + book.find('a').attrs['href']
            item['price'] = book.find('p',class_='instock availability').text.strip()
            data.append(item)
            current_page += 1
            df = pd.DataFrame(data)
            df.to_excel('books.xlsx')
            df.to_csv('books.csv')