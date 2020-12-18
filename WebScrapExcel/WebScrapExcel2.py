from bs4 import BeautifulSoup
import requests
import pandas as pd 
import csv 

def webscraping(url, table_id, filename):

    url = url

    table_id = table_id

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    Tabela = soup.find(attrs={'class': table_id})
    df = pd.read_html(str(Tabela))

    #print(df)

    filename = filename

    csv_writer = csv.writer(open(filename, 'w'))


    tr = Tabela.find_all('tr')
    data = []
    for rows in tr[1:]:
        data2 = []
        for td in rows.find_all(['td']):
            
            data2.append(td.text.replace('\n', '').strip())

        data.append(data2)
    for Table in data:
        csv_writer.writerow(Table)



# Código Principal
tabela1 = webscraping("https://www.cip-bancos.org.br/DadosEstrategicos/EvolPagsMesTot.html", "a84", "tabela1.csv")
tabela2 = webscraping("https://www.cip-bancos.org.br/DadosEstrategicos/EvolPags.html", "a89", "tabela2.csv")
    

