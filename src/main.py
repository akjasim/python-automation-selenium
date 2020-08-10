from selenium import webdriver
import time

browser = webdriver.Chrome(
    executable_path='/Users/akjasim/chromedriver/chromedriver')

browser.get('https://www.instagram.com/')

username_field = browser.find_element_by_name('username')
username_field.send_keys('akjasim')

search_btn = browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()
