
from newspaper import Article

url = 'https://www.latimes.com'

my_article = Article(url, language='en')
my_article.download()

my_article.parse()

print('Title: ', my_article.title)

print('Author ', my_article.authors)

print('Publishing data: ', my_article.publish_date)

my_article.nlp()

print('Summary: ', my_article.summary)
