from flask import Flask
from flask import render_template
from flask import request
from selenium import webdriver
from selenium.webdriver.common.by import By

FIRST_LINK_SUGGESTION = "http://deckofcardsapi.com/"
DRIVER_PATH = "/home/joao/GitHub/Python Advanced/Module 11 - Page rank/chromedriver"


app = Flask(__name__)


@app.route("/")
def my_form():
    return render_template("form.html")


@app.route("/", methods=["POST"])
def my_form_post():
    first_link = request.form["text"]
    links = scraper(first_link, depth=2)

    return render_template("results.html", links_amount=len(links), links=links)


def scraper(first_link, depth=2):
    # All the links on first page
    all_links = []
    link_list = [first_link]

    for _i in range(0, depth):
        new_links = get_all_links_from_this_link_list(link_list)
        all_links = new_links + all_links
        link_list = new_links

    return all_links


def get_all_links_from_this_link_list(links_list):
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    all_links_from_link_list = []

    for link in links_list:
        links = get_all_links_from_this_page(link, driver)
        all_links_from_link_list = all_links_from_link_list + links

    return all_links_from_link_list


def get_all_links_from_this_page(link, driver):
    driver.get(link)

    all_elements = driver.find_elements(By.TAG_NAME, "a")
    all_links = [link.get_attribute("href") for link in all_elements]

    return all_links
