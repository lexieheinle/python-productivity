#user/local/bin/python
#uses python3
import urllib.request
from bs4 import BeautifulSoup

url = "http://www.bls.gov/cps/cpsaat01.htm" #access the search term through website
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page)
tables = soup.findAll('table') #find all tables
#print(tables)
mainTable = soup.find(id="cps_eeann_year")
#print(mainTable)
for table in tables:
  caption = table.find('caption')
  print(caption)
data = [] #create holder for results
rows = mainTable.findAll('tr')
#print(rows)
for row in rows[1:]:
  dataRow = [] #create smaller list for each row
  for th in row.findAll('th'):
    dataRow.append(th.text)
  for td in row.findAll('td'):
    dataRow.append(td.text) 
  data.append(dataRow)
data.pop()
print(data)