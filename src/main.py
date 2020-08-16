from selenium import webdriver
import time
from config import EMAIL, PASSWORD
import pandas as pd

dataframe = pd.read_excel('data.xlsx')
# print(dataframe.index)

browser = webdriver.Chrome(
    executable_path='/Users/akjasim/chromedriver/chromedriver')

browser.maximize_window()

browser.get('https://www.gmail.com')

email_field = browser.find_element_by_css_selector('input[type="email"]')
email_field.send_keys(EMAIL)

next_btn = browser.find_element_by_class_name('VfPpkd-LgbsSe')
next_btn.click()

time.sleep(2)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_class_name('VfPpkd-LgbsSe')
login_btn.click()

for i in dataframe.index:
    print(dataframe.loc[i]['Name'])
    # print(i)

    time.sleep(2)

    compose_btn = browser.find_element_by_css_selector('.T-I.T-I-KE.L3')
    compose_btn.click()

    time.sleep(2)

    to_field = browser.find_element_by_name('to')
    to_field.send_keys(dataframe.loc[i]['Email'])

    subject_field = browser.find_element_by_name('subjectbox')
    subject_field.send_keys('Hiiii')

    body_field = browser.find_element_by_css_selector(
        '.Am.Al.editable.LW-avf.tS-tW')
    body_content = f"""Hii {dataframe.loc[i]['Name']},

How fdsaf,
asdfasd
fasdf
    """
    body_field.send_keys(body_content)

    send_btn = browser.find_element_by_css_selector(
        '.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
    send_btn.click()

    time.sleep(5)
