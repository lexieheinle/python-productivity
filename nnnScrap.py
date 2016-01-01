#user/local/bin/python
from bs4 import BeautifulSoup
import pdfkit
import urllib.request

def findArticles(website, firstName, lastName):
    url = "{}?s={}+{}".format(website, firstName, lastName) #access the search term through website
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,from_encoding="utf-8")
    articles = soup.findAll('article') #find all articles
    articleLink = []
    for article in articles:
        titles = article.find_all('h2')
        for title in titles:
            links = title.find_all('a')
            for link in links:
                articleLink.append(link.get('href')) #push article links to array
    for article in articleLink:
        html = urllib.request.urlopen(article).read()
        soup = BeautifulSoup(html)
        articleTitle = soup.find('h1').prettify(formatter='html')
        print (articleTitle)
        articleAuthor = soup.find('p', class_="post-byline").prettify(formatter='html')
        print (articleAuthor)
        articleContent = soup.find('div', class_="entry-inner").prettify(formatter='html')
        print (str(articleContent))
        for content in str(articleContent):
          content = content.replace('’', '\'').replace('“', '"').replace('”', '"')
        print(str(articleContent))
        splitArticle = str(article).split('/')
        shortTitle = splitArticle[-2]
        print (shortTitle) #same as headline
        f = open('{}.html'.format(shortTitle), 'w') #create html file
        message = str(articleTitle) + str(articleAuthor) + str(articleContent) + str('<a href={} target="_blank">View the article on the original website</a>'.format(article))
        f.write(message)
        f.close()
        pdfkit.from_file('{}.html'.format(shortTitle),'{}.pdf'.format(shortTitle)) #create pdf version

articles = findArticles("http://www.newsnetnebraska.org/", "lexie", "heinle")
