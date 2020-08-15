#import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv


#collect & parse webpage
page = urllib.request.urlopen("https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm")
soup = BeautifulSoup(page, 'html.parser')

#removing superfluous data - links at bottom of page
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

#creating a CSV file for the data
f = csv.writer(open('z-artist-names.csv', 'w', newline = ''))
f.writerow(['Name', 'Link'])

#pulling names
name_list = soup.find(class_='BodyText')
name_list_items = name_list.find_all('a')

#loop to print all artist names
#contents returns each tags (name) as a Python list data type
for name in name_list_items:
    names = name.contents[0]
    #adding the link to each name
    links = 'http:https://web.archive.org' + name.get('href')
    f.writerow([names,links])
    #Just a visual readout in the IDE to confirrm operation of code
    print (names)
    print (links)

f.close()

