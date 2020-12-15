import time 
import requests 
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = "https://www.cip-bancos.org.br/DadosEstrategicos/EvolPags.html"

#option = Options()
#option.headless = True
driver  = webdriver.Chrome()

driver.get(url)
time.sleep(5)
element = driver.find_element_by_xpath("//div[@class='a131xB']//table")
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')
df= pd.read_html(str(table))
print(df)

driver.quit()