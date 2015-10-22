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
  dataRow = [] #create smaller list for each row
  for td in row.findAll('td'):
    dataRow.append(td.text) 
    for link in td.findAll('a', href=True):
      print (link['href'])
      if link['href'][0] == 'm':
        fullLink = "https://www.faa.gov/uas/legislative_programs/section_333/333_authorizations/"+link['href'] #create full link for media
        dataRow.append(fullLink)
      else:
        dataRow.append(link['href'])
  data.append(dataRow)
for da in data:
  print("On {}, {} was issued an exception. Here's the link.\n {}".format (da[0], da[1], da[-1])) #print it.
