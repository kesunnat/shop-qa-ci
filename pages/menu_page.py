from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.CSS_SELECTOR, "form input")
        self.btn_search = (By.CSS_SELECTOR, "form button")
        self.card_margherita_pizza = (By.CSS_SELECTOR, "div[class*='_products_list_'] a:nth-child(2)")
        self.btn_basket = (By.CSS_SELECTOR, "div[class*='_product_top_'] button")
        self.btn_back = (By.CSS_SELECTOR, "div[class*='_product_top_'] a")
        self.basket = (By.CSS_SELECTOR, "div[class*='_products_list_'] a:nth-child(3) button")
        self.section_basket = (By.CSS_SELECTOR, "div[class*='_user_'] a:nth-child(2)")
        self.btn_exit = (By.CSS_SELECTOR, "div[class*='_user_'] button")
        self.btn_yes = (By.CSS_SELECTOR, "div[class*='_modal_'] button:nth-child(2)")

    def enter_search_input(self, search_input):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.search_input))
        element.clear()
        element.send_keys(search_input)

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






