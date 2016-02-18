#user/local/bin/python
#uses python3
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.faa.gov/uas/legislative_programs/section_333/333_authorizations/" #access the search term through website
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page)
table = soup.findAll('tbody') #find all tables
data = [] #create holder for results
rows = soup.findAll('tr')
for row in rows[1:]:
  data-row = [] #create smaller list for each row
  for td in row.findAll('td'):
    data-row.append(td.text)
    for link in td.findAll('a', href=True):
      print (link['href'])
      if link['href'][0] == 'm':
        full-link = "https://www.faa.gov/uas/legislative_programs/section_333/333_authorizations/"+link['href'] #create full link for media
        data-row.append(full-link)
      else:
        data-row.append(link['href'])
  data.append(data-row)
for da in data:
  print("On {0}, {1} was issued an exception. Here's the link.\n {2}".format (da[0], da[1], da[-1])) #print it.
