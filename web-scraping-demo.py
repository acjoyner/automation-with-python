from bs4 import BeautifulSoup
import  requests
import csv
file = open('scrapted_quotes.csv','w')
writer = csv.writer(file)


page_to_scrape = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(page_to_scrape.text,'html.parser')
quotes = soup.find_all('span',
                       attrs={'class':'text'})
authors = soup.find_all('small',
                       attrs={'class':'author'})

writer.writerow(['Quotes','AUTHORS'])
for quote in quotes:
    print(quote.text)
for author in authors:
    print(author.text)

file.close()