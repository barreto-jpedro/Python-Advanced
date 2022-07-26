""" 
- Busque no texto da página em que foi feita a raspagem todos os links que apontem para outras páginas da Wikipédia.
- Faça uma nova raspagem para cada novo link capturado e imprima em cada um deles a mensagem “Página secundária: {Nome da página visitada}”.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

DRIVER_PATH = '/home/joao/GitHub/Python Advanced/Module 3 - HTTP & APIs/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://en.wikipedia.org/wiki/Linux')
print(f"Main page: {driver.title}")
html_code = driver.page_source
all_links = driver.find_elements(By.TAG_NAME, "a")
