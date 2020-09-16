from selenium import webdriver
import time

browser = webdriver.Chrome(
    executable_path="/Users/akjasim/chromedriver/chromedriver")

browser.get("https://github.com/login")
