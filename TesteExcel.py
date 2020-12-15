from bs4 import BeautifulSoup
import requests
import pandas as pd 
import csv 

url = 'https://www.cip-bancos.org.br/DadosEstrategicos/EvolPagsMesTot.html'

table_id = 'oReportCell'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

Tabela = soup.find(attrs={'id': table_id})
df = pd.read_html(str(Tabela))

#print(df)

filename = 'teste.csv'

csv_writer = csv.writer(open(filename, 'w'))


for td in soup.find_all("td"):
    
    data = []
    data.append(td.text)
    print(data)