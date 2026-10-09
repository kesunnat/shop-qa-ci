import time
from time import sleep
from selenium.common.exceptions import TimeoutException
import allure

from pages.login_page import LoginPage
from pages.menu_page import MenuPage


def test_shop_qa_chrome(driver_chrome):
    driver_chrome.get('https://shop-qa-master.vercel.app/#/login')
    login_page = LoginPage(driver_chrome)
    login_page.enter_login('arseniy')
    time.sleep(2)
    login_page.enter_password('svetikss1001')
    time.sleep(2)
    login_page.click_btn_enter()
    time.sleep(2)

    menu_page = MenuPage(driver_chrome)
    menu_page.enter_search_input('pizza')
    time.sleep(2)
    menu_page.click_btn_search()
    time.sleep(2)
    menu_page.select_card_margherita_pizza()
    time.sleep(2)
    menu_page.click_btn_basket()
    time.sleep(2)
    menu_page.click_btn_back()
    time.sleep(2)
    menu_page.click_basket()
    time.sleep(2)
    menu_page.click_section_basket()
    time.sleep(2)
    menu_page.click_btn_exit()
    time.sleep(2)
    menu_page.click_btn_yes()
    time.sleep(2)

def test_invalid_shop_qa_chrome(driver_chrome):
    driver_chrome.get('https://shop-qa-master.vercel.app/#/login')
    login_page = LoginPage(driver_chrome)
    login_page.enter_login('arseniy')
    time.sleep(2)
    login_page.enter_password('svetikss100111')
    time.sleep(2)
    login_page.click_btn_enter()
    time.sleep(2)


def test_shop_qa_edge(driver_edge):
    driver_edge.get('https://shop-qa-master.vercel.app/#/login')
    login_page = LoginPage(driver_edge)
    login_page.enter_login('arseniy')
    time.sleep(2)
    login_page.enter_password('svetikss1001')
    time.sleep(2)
    login_page.click_btn_enter()
    time.sleep(2)

    menu_page = MenuPage(driver_edge)
    menu_page.enter_search_input('pizza')
    time.sleep(2)
    menu_page.click_btn_search()
    time.sleep(2)
    menu_page.select_card_margherita_pizza()
    time.sleep(2)
    menu_page.click_btn_basket()
    time.sleep(2)
    menu_page.click_btn_back()
    time.sleep(2)
    menu_page.click_basket()
    time.sleep(2)
    menu_page.click_section_basket()

    time.sleep(2)
    menu_page.click_btn_exit()
    time.sleep(2)
    menu_page.click_btn_yes()
    time.sleep(2)

def test_invalid_shop_qa_edge(driver_edge):
    driver_edge.get('https://shop-qa-master.vercel.app/#/login')
    login_page = LoginPage(driver_edge)
    login_page.enter_login('arseniy')
    time.sleep(2)
    login_page.enter_password('svetikss100111')
    time.sleep(2)
    login_page.click_btn_enter()
    time.sleep(2)
