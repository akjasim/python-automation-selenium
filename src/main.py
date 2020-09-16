#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
from selenium import webdriver
import time
from config import USERNAME, PASSWORD
import sys
import pyperclip

try:
    repo_name = sys.argv[1]
except:
    print('Please provide repo name.')
    sys.exit()

try:
    visibility = sys.argv[2]
except:
    visibility = 'public'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(
    executable_path="/Users/akjasim/chromedriver/chromedriver", options=chrome_options)

browser.get("https://github.com/login")

login_field = browser.find_element_by_name('login')
login_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_field.submit()

browser.get('https://github.com/new')

repository_name = browser.find_element_by_name('repository[name]')
repository_name.send_keys(repo_name)

time.sleep(1)

visibility_radio_input = browser.find_element_by_xpath(
    f'//input[@name="repository[visibility]"][@value="{visibility}"]')
visibility_radio_input.click()

repository_name.submit()

try:
    content = browser.find_element_by_xpath(
        '//clipboard-copy[@for="empty-setup-push-repo-echo"]')
    content.click()
    time.sleep(1)
    print('****Repository created successfully****', end="\n\n")
    # print(pyperclip.paste())
    print(f"git remote add origin https://github.com/akjasim/{repo_name}.git")
    print("git branch -M master")
    print("git push -u origin master")
except:
    print('Repository cannot be created. (Confirm the repo name is unique)')
