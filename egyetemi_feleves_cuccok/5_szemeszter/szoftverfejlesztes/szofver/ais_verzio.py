import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


testdata = [
    ("", "", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("standard_user", "wrong_password",
     "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce",
     "Epic sadface: Sorry, this user has been locked out.")
]


@pytest.mark.parametrize("username,password,error_msg", testdata)
def test_invalid_login(driver, username, password, error_msg):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)

    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "login-button").click()

    error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error_msg in error_element.text
