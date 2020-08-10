from selenium import webdriver
import time
from config import USERNAME, PASSWORD

browser = webdriver.Chrome(
    executable_path='/Users/akjasim/chromedriver/chromedriver')

browser.get('https://www.instagram.com/')

username_field = browser.find_element_by_name('username')
username_field.send_keys(USERNAME)

username_field = browser.find_element_by_name('password')
username_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()
