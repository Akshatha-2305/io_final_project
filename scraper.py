#city 1
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Albury.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city 2
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/BadgerysCreek.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city 3
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Cobar.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city4
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/CoffsHarbour.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city5
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Moree.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('output1.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city6
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Newcastle.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city7
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/NorahHead.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city8
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/NorfolkIsland.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city9
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Penrith.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city10
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Richmond.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city11
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Sydney.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city12
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/SydneyAirport.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city13
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/WaggaWagga.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city14
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Williamtown.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city15
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Wollongong.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city16
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Canberra.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city17
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Tuggeranong.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city18
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/MountGinini.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city19
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Ballarat.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city20
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Bendigo.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

#city21
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Sale.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city22
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/MelbourneAirport.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city23
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Melbourne.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city24
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Mildura.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city25
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Nhil.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city26
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Portland.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city27
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Watsonia.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city28
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Dartmoor.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city29
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Brisbane.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city30
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Cairns.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city31
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/GoldCoast.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city32
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Townsville.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city33
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Adelaide.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city34
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/MountGambier.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city35
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Nuriootpa.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)




#city36
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Woomera.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)




#city37
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Albany.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city38
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Witchcliffe.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city39
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/PearceRAAF.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('output1.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)




#city40
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/PerthAirport.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city41
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Perth.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city42
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/SalmonGums.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city43
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Walpole.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city44
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Hobart.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city45
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Launceston.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('output1.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city46
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/AliceSprings.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)



#city47
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Darwin.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city48
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Katherine.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


#city49
from bs4 import BeautifulSoup
import csv
import lxml
import urllib.request
html = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Uluru.html").read()
soup = BeautifulSoup(html,'lxml')
table = soup.find("table")

output_rows = []
for table_row in table.find_all('tr'):
    columns = table_row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('dataset.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


