from selenium import webdriver
from selenium.webdriver.common.by import By
from json import dump

FIRST_LINK = 'https://www.w3schools.io/file/yaml-sample-example'
DRIVER_PATH = '/home/joao/GitHub/Python Advanced/Module 4 - Yalm file/chromedriver'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#Initial page
driver.get(FIRST_LINK)
print(f"Main page: {driver.title}")

#All the elements on first page
elements = driver.find_elements(By.CLASS_NAME, "c")

#Getting the comments
all_comments = [element.text for element in elements]
dict_comments = {"all_comments" : all_comments}

#Saving in a Yalm file
with open("Module 4 - comments.yml", "w") as file:
    dump(dict_comments, file)
    