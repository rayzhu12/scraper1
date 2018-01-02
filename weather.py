import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://www.wunderground.com/weather/us/ga/warsaw/KGADULUT30'
# url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
# print(soup.prettify())

temp = soup.find('span _ngcontent-c15', attrs={'class':'wu-value wu-value-to'})
print(temp)

#
# list_of_rows = []
# for row in table.findAll('tr'):
#     list_of_cells = []
#     for cell in row.findAll('td'):
#         text = cell.text.replace('&nbsp;', '')
#         list_of_cells.append(text)
#     list_of_rows.append(list_of_cells)
#
# outfile = open("./inmates.csv", "wb")
# writer = csv.writer(outfile)
# writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
# writer.writerows(list_of_rows)
