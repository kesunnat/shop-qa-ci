from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MenuPage:
    def __init__(self,driver):
        self.driver = driver
        self.search_input = (By.CSS_SELECTOR, "#root > div.main > div.container > div > div._products_filter_1bf0g_1 > div:nth-child(2) > form > div > input")
        self.btn_search = (By.CSS_SELECTOR, "#root > div.main > div.container > div > div._products_filter_1bf0g_1 > div:nth-child(2) > form > button")
        self.card_margherita_pizza = (By.CSS_SELECTOR, "#root > div.main > div.container > div > div._products_list_1bf0g_26 > a:nth-child(2)")
        self.btn_basket = (By.CSS_SELECTOR, "#root > div.main > div.container > div > div._product_top_dhwcc_1 > button")
        self.btn_back = (By.CSS_SELECTOR, "#root > div.main > div.container > div > div._product_top_dhwcc_1 > a")
        self.basket = (By.CSS_SELECTOR, "#root > div.main > div.container > div > div._products_list_1bf0g_26 > a:nth-child(3) > button")
        self.section_basket = (By.CSS_SELECTOR, "#root > div.main > div._user_w43ta_1 > ul > a:nth-child(2)")
        self.btn_exit = (By.CSS_SELECTOR, "#root > div.main > div._user_w43ta_1 > button")
        self.btn_yes = (By.CSS_SELECTOR, "#root > div.main > div._modal_thov9_1 > div > div > button:nth-child(2)")

    def enter_search_input(self, search_input):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.search_input)).send_keys(search_input)

    def click_btn_search(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_search)).click()

    def select_card_margherita_pizza(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.card_margherita_pizza)).click()

    def click_btn_basket(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_basket)).click()

    def click_btn_back(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_back)).click()

    def click_basket(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.basket)).click()

    def click_section_basket(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.section_basket)).click()

    def click_btn_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_exit)).click()

    def click_btn_yes(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_yes)).click()





