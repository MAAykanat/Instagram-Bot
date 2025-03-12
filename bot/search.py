import time
from selenium import webdriver

class InstagramSearch:
    def __init__(self, driver):
        self.driver = driver

    def search(self, keyword):
        search_url = f"https://www.instagram.com/explore/tags/{keyword}/"
        self.driver.get(search_url)
        time.sleep(5)
        print(f"🔍 Searching for: {keyword}")

    def search_by_url(self, url):
        self.driver.get(url)
        time.sleep(5)
        print(f"🔍 Searching by URL: {url}")
