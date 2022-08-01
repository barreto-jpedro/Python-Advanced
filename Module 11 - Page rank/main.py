from flask import Flask
from flask import render_template
from flask import request
from selenium import webdriver
from selenium.webdriver.common.by import By

FIRST_LINK = "https://en.wikipedia.org/wiki/Pytest"
DRIVER_PATH = "/home/joao/GitHub/Python Advanced/Module 11 - Page rank/chromedriver"


app = Flask(__name__)


@app.route("/")
def my_form():
    return render_template("form.html")


@app.route("/", methods=["POST"])
def my_form_post():
    text = request.form["text"]
    all_links_from_first_page = scraper(text)
    titles = all_links_from_first_page.keys()
    return render_template("results.html", titles=titles)


def scraper(first_link):
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    # Initial page
    driver.get(first_link)
    print(f"Main page: {driver.title}")

    # All the links on first page
    all_elements = driver.find_elements(By.TAG_NAME, "a")
    all_links = [link.get_attribute("href") for link in all_elements]
    print(f"This page has {len(all_links)} links.")

    links_and_titles_dict = dict()

    for link in all_links:
        try:
            driver.get(link)
            links_and_titles_dict[driver.title] = link
            print(100 * "_")
            print(f"URL: {link}")
            print(f"Title: {driver.title}")
            print(100 * "_")
        except Exception:
            print(f"Couldn't get to this link: {link}")

    return links_and_titles_dict
