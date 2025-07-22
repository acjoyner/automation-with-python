from bs4 import BeautifulSoup
import requests

url = 'https://www.google.co.in'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

print(soup)

soup.find('div')

soup.find_all('div')