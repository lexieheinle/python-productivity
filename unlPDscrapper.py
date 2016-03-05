import sys, os


try:
    from BeautifulSoup import BeautifulSoup
except:
    from bs4 import BeautifulSoup

import urllib.request, re, csv

html = urllib.request.urlopen("https://scsapps.unl.edu/policereports/default.aspx")

soup = BeautifulSoup(html, 'lxml')
lists = soup.find_all('ul')
reports = lists[9]
crime_base_url = 'https://scsapps.unl.edu/policereports/'
crime_links = []
items = reports.find_all('li')
for item in items:
    crime_id = item.find(id=re.compile('.*IncidentNumberLink'))
    crime_id_url = crime_base_url + crime_id['href']
    crime_links.append(crime_id_url)
print(crime_links)
if len(crime_links) > 0:
    with open('crimes.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['incidentId', 'reported', 'occured', 'building', 'location', 'locationCode', 'incidentCode', 'person_status', 'person_name', 'person_RG', 'person_affiliation', 'person_crime', 'person_age', 'synopsis'])
        for crime in crime_links:
            html = urllib.request.urlopen(crime)
            soup = BeautifulSoup(html, 'lxml')
            incident_id = soup.select('#ctl00_ContentPlaceHolder1__IncidentNumber')
            incident_id = incident_id[0].text
            print(incident_id)
            reported = soup.select('#ctl00_ContentPlaceHolder1_DateReported')
            reported = reported[0].text
            print(reported)
            occured = soup.select('#ctl00_ContentPlaceHolder1_OccurredDate')
            occured = occured[0].text
            building = soup.select('#ctl00_ContentPlaceHolder1_Building')
            building = building[0].text
            location = soup.select('#ctl00_ContentPlaceHolder1_Location')
            location = location[0].text
            location_code = soup.select('#ctl00_ContentPlaceHolder1_LocationCode')
            location_code = location_code[0].text
            incident_code = soup.select('#ctl00_ContentPlaceHolder1_IncidentCode')
            incident_code = incident_code[0].text
            persons_involved = soup.select('#ctl00_ContentPlaceHolder1_PersonsInvolvedSection')
            if len(persons_involved) > 0:
                person_status = soup.select('#ctl00_ContentPlaceHolder1__PersonsInvolvedList_ctl00_Code')
                person_status = person_status[0].text
                print(person_status)
                person_name = soup.select('#ctl00_ContentPlaceHolder1__PersonsInvolvedList_ctl00_FullName')
                person_name = person_name[0].text
                print(person_name)
                person_RG = soup.select('#ctl00_ContentPlaceHolder1__PersonsInvolvedList_ctl00_RaceGender')
                person_RG = person_RG[0].text
                person_affiliation = soup.select('#ctl00_ContentPlaceHolder1__PersonsInvolvedList_ctl00_Affiliation')
                person_affiliation = person_affiliation[0].text
                person_crime = soup.select('#ctl00_ContentPlaceHolder1__PersonsInvolvedList_ctl00_CitationOffense')
                person_crime = person_crime[0].text
                person_age = soup.select('#ctl00_ContentPlaceHolder1__PersonsInvolvedList_ctl00_Age')
                person_age = person_age[0].text
            else:
                person_status = "N/A"
                person_name = "N/A"
                person_RG = "N/A"
                person_affiliation = "N/A"
                person_crime = "N/A"
                person_age = "N/A"
            synopsis = soup.select('#ctl00_ContentPlaceHolder1__Synopsis')
            synopsis = synopsis[0].text
            writer.writerow([incident_id, reported, occured, building, location, location_code, incident_code, person_status, person_name, person_RG, person_affiliation, person_crime, person_age, synopsis])
