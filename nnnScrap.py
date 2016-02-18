#user/local/bin/python
from bs4 import BeautifulSoup
import pdfkit
import urllib.request

def find-articles(website, first-name, last-name):
    'find all Nebrask news service articles for first-name and last-name reporter and outputs html and pdfs'
    url = "{0}?s={1}+{2}".format(website, first-name, last-name) #access the search term through website
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,from_encoding="utf-8")
    articles = soup.findAll('article') #find all articles
    article-link = []
    for article in articles:
        titles = article.find_all('h2')
        for title in titles:
            links = title.find_all('a')
            for link in links:
                article-link.append(link.get('href')) #push article links to array
    for article in article-link:
        html = urllib.request.urlopen(article).read()
        soup = BeautifulSoup(html)
        article-title = soup.find('h1').prettify(formatter='html')
        print (article-title)
        article-author = soup.find('p', class_="post-byline").prettify(formatter='html')
        print (article-author)
        article-content = soup.find('div', class_="entry-inner").prettify(formatter='html')
        print (str(article-content))
        for content in str(article-content):
          content = content.replace('’', '\'').replace('“', '"').replace('”', '"')
        print(str(article-content))
        split-article = str(article).split('/')
        short-title = split-article[-2]
        print (short-title) #same as headline
        f = open('{0}.html'.format(short-title), 'w') #create html file
        message = str(article-title) + str(article-author) + str(article-content) + str('<a href={0} target="_blank">View the article on the original website</a>'.format(article))
        f.write(message)
        f.close()
        pdfkit.from_file('{0}.html'.format(short-title),'{0}.pdf'.format(short-title)) #create pdf version

articles = find-articles("http://www.newsnetnebraska.org/", "lexie", "heinle")
