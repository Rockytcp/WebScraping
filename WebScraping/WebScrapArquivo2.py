from bs4 import BeautifulSoup
import requests
import pandas as pd 

url = 'https://www.cip-bancos.org.br/DadosEstrategicos/EvolPagsMesTot.html'

table_id = 'oReportCell'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

Tabela = soup.find(attrs={'id': table_id})
df = pd.read_html(str(Tabela))

print(df)
