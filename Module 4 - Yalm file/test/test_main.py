from selenium import webdriver

FIRST_LINK = "https://www.w3schools.io/file/yaml-sample-example"
DRIVER_PATH = "/home/joao/GitHub/Python Advanced/Module 4 - Yalm file/chromedriver"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)


def test_checking_first_page_title():
    driver.get(FIRST_LINK)
    assert "YAML sample example file with examples" == driver.title
