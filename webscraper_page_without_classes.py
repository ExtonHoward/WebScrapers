from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

#User-Agent is used to trick bots as my computer browser instead of the script
url = 'https://socialblade.com/youtube/top/50/mostviewed'
page = Request(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'})
webpage = urlopen(page).read()
soup = BeautifulSoup (webpage, 'html.parser')

#Since socialblade doesn't use classes in their code, use attrs to find style for list. recursive is off to only find surface level children under style
rows = soup.find('div', attrs={'style': 'float: right; width: 900px;'}).find_all('div', recursive=False)[4:]

#open file to store data from scraper
f = csv.writer(open('TopYouTubers.csv', 'w', encoding='utf-8', newline= ''))

#write header row for file
f.writerow(['YouTube Username', 'Uploads', 'Total Channel Views'])

for row in rows:
    username = row.find('a').text.strip()
    #color is the anchor on this particular page with how it was coded in CSS. Able to use both 1st & 2nd options on list in order to get dta needed.
    numbers = row.find_all('span', attrs={'style': 'color:#555;'})
    uploads = numbers[0].text.strip()
    views = numbers[1].text.strip()
    print (username + ' ' + uploads + ' - ' + views)
    f.writerow([username, uploads, views])

f.close()