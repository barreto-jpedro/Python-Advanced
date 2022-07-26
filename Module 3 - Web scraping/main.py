from selenium import webdriver
from selenium.webdriver.common.by import By

FIRST_LINK = 'https://en.wikipedia.org/wiki/Pytest'
DRIVER_PATH = '/home/joao/GitHub/Python Advanced/Module 3 - Web scraping/chromedriver'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#Initial page
driver.get(FIRST_LINK)
print(f"Main page: {driver.title}")

#All the links on first page
all_elements = driver.find_elements(By.TAG_NAME, "a")
all_links = [link.get_attribute('href') for link in all_elements]
print(f"This page has {len(all_links)} links.")

for link in all_links:
    try: 
        if link.find("wikipedia") != -1:
            driver.get(link)
            print(100*"_")
            print(f"URL: {link}")
            print(f"Title: {driver.title}")
            print(100*"_")
    except:
        print(f"Couldn't get to this link: {link}")
        