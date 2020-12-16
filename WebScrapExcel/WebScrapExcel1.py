from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv 

url = 'https://www.cip-bancos.org.br/DadosEstrategicos/EvolPags.html'

table_id = 'a89'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

Tabela = soup.find(attrs={'class': table_id})
#df = pd.read_html(str(Tabela))


filename = 'WebScrapTabela.csv'

csv_writer = csv.writer(open(filename, 'w'))

tr = Tabela.find_all('tr')
data = []
for row in tr[1:]:
    data2 = []
    for td in row.find_all(['td']):
        data2.append(td.text.replace('\n', '').strip())
    data.append(data2)
for table in data:
    csv_writer.writerow(table)