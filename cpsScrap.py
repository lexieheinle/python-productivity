#user/local/bin/python
#uses python3
import urllib.request
from bs4 import BeautifulSoup
from reports.models import Unemployment

url = "http://www.bls.gov/cps/cpsaat01.htm" #access the search term through website
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page)
tables = soup.findAll('table') #find all tables
#print(tables)
main-table = soup.find(id="cps_eeann_year")
#print(main-table)
for table in tables:
  caption = table.find('caption')
  print(caption)
data = [] #create holder for results
rows = main-table.findAll('tr')
#print(rows)
for row in rows[1:]:
  data-row = [] #create smaller list for each row
  for th in row.findAll('th'):
    data-row.append(th.text)
  for td in row.findAll('td'):
    data-row.append(td.text)
  data.append(data-row)
data.pop()
print(data)
cleaned-rate = []
cleaned-date = []
for da in data:
  #da[0] = eval(da[0])
  try:
    if int(da[0]) >= 1947:
      dates = "{0}-{1}-{2}".format(da[0], 1, 1)
      cleaned-date.append(dates)
      cleaned-rate.append(float(da[-2]))
  except ValueError:
    pass
#cleaned.pop(0)
print(cleaned-rate)
print(cleaned-date)
length = len(cleaned-rate)
for i in range(length):
  b, bcreated = Unemployment.objects.get_or_create(rate=cleaned-rate[i], date=cleaned-date[i])
  print(b)
