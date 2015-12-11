#user/local/bin/python
#uses python3
#import urllib.request
#from bs4 import BeautifulSoup
import mechanize

url = "https://login5.silverpop.com/login?service=https%3A%2F%2Fengage5.silverpop.com%2Fhome.do" #access the search term through website
user_name = '#'
pass_word = '#'
br = mechanize.Browser()
br.open(url)
br.select_form(nr = 0)
br.form['username'] = user_name
br.form['password'] = pass_word
br.submit()
response = br.response()
print response.read()
response2 = br.open('https://engage5.silverpop.com/reports.do?action=reportsMailingSelection&destAction=reportsSummary')
assert br.viewing_html()
print response2.read()

"""page = urllib.request.urlopen(url).read()
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
cleanedRate = []
cleanedDate = []
for da in data:
  #da[0] = eval(da[0])
  try:
    if int(da[0]) >= 1947:
      dates = "{}-{}-{}".format(da[0], 1, 1)
      cleanedDate.append(dates)
      cleanedRate.append(eval(da[-2]))
  except ValueError:
    pass
#cleaned.pop(0)
print(cleanedRate)
print(cleanedDate)
length = len(cleanedRate)
for i in range(length):
  b, bcreated = Unemployment.objects.get_or_create(rate=cleanedRate[i], date=cleanedDate[i])
  print(b)"""