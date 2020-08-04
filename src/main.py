from selenium import webdriver
import time

browser = webdriver.Chrome(
    executable_path='/Users/akjasim/chromedriver/chromedriver')

browser.get('https://www.google.com')

time.sleep(2)

search_input = browser.find_element_by_name('q')
search_input.send_keys('hello world')

time.sleep(2)

search_btn = browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()

'''
<input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwiK0rzooIHrAhWk7XMBHZ7lBfIQ39UDCAQ">
<input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" type="submit" data-ved="0ahUKEwiK0rzooIHrAhWk7XMBHZ7lBfIQ4dUDCAs">
'''
