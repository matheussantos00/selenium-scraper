import login
import sys
import time
from selenium import webdriver
from bs4 import BeautifulSoup

#firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
#driver = webdriver.Firefox(firefox_profile=firefox_profile)

class Scrape:

    def __init__(self):
        self.url = 'https://br.tradingview.com/#signin'

    def scrape(self):
        #SELENIUM
        driver = webdriver.Firefox()
        driver.get(self.url)
        print(driver.window_handles)
        time.sleep(5)
        login_page = driver.find_element_by_css_selector('span.tv-signin-dialog__social--big:nth-child(1)')
        login_page.click()
        print(driver.window_handles)
        print(driver.current_window_handle)
        driver.switch_to.window(driver.window_handles[1])
        print(driver.current_window_handle)
        time.sleep(5)
        data = login.Login()
        id = driver.find_element_by_id('identifierId')
        id.send_keys(data.usuario['email'])
        time.sleep(5)
        prox = driver.find_element_by_id('identifierNext')
        prox.click()
        time.sleep(10)
        password = driver.find_element_by_name('password')
        password.send_keys(data.usuario['senha'])
        time.sleep(5)
        prox = driver.find_element_by_id('passwordNext')
        prox.click()
        driver.quit()

if __name__ != 'main':
    app = Scrape()
    app.scrape()