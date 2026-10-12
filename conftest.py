import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture
def driver_chrome():
    options = ChromeOptions()
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        driver.maximize_window()
        
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def driver_edge():
    options = EdgeOptions()
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
    driver = webdriver.Edge(options=options)
    
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        driver.maximize_window()
        
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
