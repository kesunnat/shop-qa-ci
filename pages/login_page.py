from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.login = (By.CSS_SELECTOR, "#root > div.main > div.form > div > form > div:nth-child(1) > label > input")
        self.password = (By.CSS_SELECTOR, "#root > div.main > div.form > div > form > div:nth-child(2) > label > input")
        self.btn_enter = (By.CSS_SELECTOR, "#root > div.main > div.form > div > form > button")

    def enter_login(self, login):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login)).send_keys(login)

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.password)).send_keys(password)

    def click_btn_enter(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_enter)).click()

