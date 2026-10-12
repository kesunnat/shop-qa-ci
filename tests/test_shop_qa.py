from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from pages.login_page import LoginPage
from pages.menu_page import MenuPage

def test_shop_qa_chrome(driver_chrome):
    driver_chrome.get('https://shop-qa-master.vercel.app/#/login')
    login_page = LoginPage(driver_chrome)
    
    login_page.enter_login('arseniy')
    login_page.enter_password('svetikss1001')
    login_page.click_btn_enter()
    
    WebDriverWait(driver_chrome, 10).until(
        EC.url_changes('https://shop-qa-master.vercel.app/#/login')
    )

    menu_page = MenuPage(driver_chrome)
    menu_page.enter_search_input('pizza')
    menu_page.click_btn_search()
    menu_page.select_card_margherita_pizza()
    menu_page.click_btn_basket()
    menu_page.click_btn_back()
    menu_page.click_basket()
    menu_page.click_section_basket()
    menu_page.click_btn_exit()
    menu_page.click_btn_yes()

def test_invalid_shop_qa_chrome(driver_chrome):
    driver_chrome.get('https://shop-qa-master.vercel.app/#/login')
    login_page = LoginPage(driver_chrome)
    
    login_page.enter_login('arseniy')
    login_page.enter_password('svetikss100111')
    login_page.click_btn_enter()
    
    WebDriverWait(driver_chrome, 5).until(
        EC.presence_of_element_located(login_page.login)
    )
    assert 'login' in driver_chrome.current_url

def test_shop_qa_edge(driver_edge):
    driver_edge.get('https://shop-qa-master.vercel.app/#/login')
    login_page = LoginPage(driver_edge)
    
    login_page.enter_login('arseniy')
    login_page.enter_password('svetikss1001')
    login_page.click_btn_enter()
    
    WebDriverWait(driver_edge, 10).until(
        EC.url_changes('https://shop-qa-master.vercel.app/#/login')
    )

    menu_page = MenuPage(driver_edge)
    menu_page.enter_search_input('pizza')
    menu_page.click_btn_search()
    menu_page.select_card_margherita_pizza()
    menu_page.click_btn_basket()
    menu_page.click_btn_back()
    menu_page.click_basket()
    menu_page.click_section_basket()
    menu_page.click_btn_exit()
    menu_page.click_btn_yes()

def test_invalid_shop_qa_edge(driver_edge):
    driver_edge.get('https://shop-qa-master.vercel.app/#/login')
    login_page = LoginPage(driver_edge)
    
    login_page.enter_login('arseniy')
    login_page.enter_password('svetikss100111')
    login_page.click_btn_enter()
    
    WebDriverWait(driver_edge, 5).until(
        EC.presence_of_element_located(login_page.login)
    )
    assert 'login' in driver_edge.current_url


