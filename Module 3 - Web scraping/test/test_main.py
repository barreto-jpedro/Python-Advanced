from selenium import webdriver

FIRST_LINK = 'https://en.wikipedia.org/wiki/Pytest'
DRIVER_PATH = '/home/joao/GitHub/Python Advanced/Module 3 - Web scraping/chromedriver'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)


def test_checking_first_page_title():
    driver.get(FIRST_LINK)
    assert "pytest - Wikipedia"==driver.title
