from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
from locators import *
from csv import reader
from hamcrest import assert_that, equal_to

PAGE_URL = 'https://www.saucedemo.com/'

chrome_install = ChromeDriverManager().install()
folder = os.path.dirname(chrome_install)
chromedriver_path = os.path.join(folder, 'chromedriver.exe')
service = ChromeService(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get(PAGE_URL)

username_field = driver.find_element(*text_field["Username"])
password = driver.find_element(*text_field["Password"])
login_button = driver.find_element(*navigation_button['Login'])

lista = []
with open('data.csv', encoding='utf-8') as f:
    csreader = reader(f, delimiter=";")
    for username, password1, error_message in csreader:
        username_field.send_keys(Keys.CONTROL + 'a')
        username_field.send_keys(Keys.DELETE)

        password.send_keys(Keys.CONTROL + 'a')
        password.send_keys(Keys.DELETE)

        username_field.send_keys(username)
        password.send_keys(password1)
        login_button.click()

        actual_error = driver.find_element(*messages['login error']).text

        assert_that(actual_error, equal_to(error_message))

driver.quit()
