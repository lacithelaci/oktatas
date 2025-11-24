from pyexpat.errors import messages
from selenium.webdriver.common.by import By

text_field = {
    "Username": (By.ID, 'user-name'),
    "Password": (By.ID, 'password')
}

navigation_button = {
    "Login": (By.ID, "login-button")
}

messages = {
    "login error": (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")}

