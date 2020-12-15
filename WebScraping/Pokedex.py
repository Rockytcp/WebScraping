from bs4 import BeautifulSoup
import requests
import pandas as pd 

url = 'https://pokemondb.net/pokedex/all'

table_id = "pokedex"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

Tabela = soup.find('table', attrs={'id': table_id})
df = pd.read_html(str(Tabela))


print(df)