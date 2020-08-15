from bs4 import BeautifulSoup
import urllib.request
import csv

#creating a CSV file for the data
f = csv.writer(open('z-artist-names.csv', 'w', newline = ''))
f.writerow(['Name', 'Link'])

#multiple pages
pages = []

for i in range (1,5):
    url = 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    # collect & parse webpage
    page = urllib.request.urlopen(item)
    soup = BeautifulSoup(page, 'html.parser')

    # removing superfluous data - links at bottom of page
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    # pulling names
    name_list = soup.find(class_='BodyText')
    name_list_items = name_list.find_all('a')

    for name in name_list_items:
        names = name.contents[0].strip()
        links = 'http:https://web.archive.org' + name.get('href')
        f.writerow([names, links])
        print(names)
        print(links)

f.close()