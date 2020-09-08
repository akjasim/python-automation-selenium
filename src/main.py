from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


browser = webdriver.Chrome(
    executable_path='/Users/akjasim/chromedriver/chromedriver')

browser.get('https://selenium.jasim.tech/')

dataframe = pd.read_excel('data.xlsx')

for i in dataframe.index:
    entry = dataframe.iloc[i]

    name_input = browser.find_element_by_name('fullname')
    name_input.send_keys(entry['Full Name'])

    email_input = browser.find_element_by_name('email')
    email_input.send_keys(entry['Email'])

    gender_xpath = f"//input[@name=\"gender\"][@value=\"{entry['Gender']}\"]"
    gender_input = browser.find_element_by_xpath(gender_xpath)
    gender_input.click()

    interested_languages = entry['Interested Languages']
    langs = interested_languages.split(', ')

    for lang in langs:
        lang_xpath = f'//input[@type="checkbox"][@value="{lang}"]'
        lang_input = browser.find_element_by_xpath(lang_xpath)
        lang_input.click()

    status_select = Select(browser.find_element_by_name('workingstatus'))
    status_select.select_by_value(entry['Working Status'])

    print('Sleeping for 5 seconds before submitting...')
    time.sleep(3)

    # email_input.submit()

    submit_btn = browser.find_element_by_css_selector('input[type="submit"]')
    browser.execute_script("return arguments[0].click()", submit_btn)

    time.sleep(2)
