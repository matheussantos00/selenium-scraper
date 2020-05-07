import login
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#icognito
#firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
#driver = webdriver.Firefox(firefox_profile=firefox_profile)


class Scrape:

    def __init__(self):
        self.url = 'https://br.tradingview.com/#signin'
        self.driver = webdriver.Firefox()
        self.pages = {}

    def page_management(self):
        pass

    def log_in(self):
        self.driver.get(self.url)

        time.sleep(5)
        login_page = self.driver.find_element_by_css_selector('span.tv-signin-dialog__social--big:nth-child(1)')
        login_page.click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        time.sleep(5)
        data = login.Login()
        id = self.driver.find_element_by_id('identifierId')
        id.send_keys(data.usuario['email'])
        time.sleep(5)
        prox = self.driver.find_element_by_id('identifierNext')
        prox.click()
        time.sleep(10)
        password = self.driver.find_element_by_name('password')
        password.send_keys(data.usuario['senha'])
        time.sleep(5)
        prox = self.driver.find_element_by_id('passwordNext')
        prox.click()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def new_stock(self, stock):
        search = self.driver.find_element_by_css_selector('.tv-header-search__input')
        search.send_keys(stock, Keys.ENTER)
        time.sleep(5)
        self.driver.find_element_by_link_text('Gráfico completo').click()


if __name__ == '__main__':
    print(__name__)
    app = Scrape()
    app.log_in()
    app.new_stock('NASDAQ:CDNS')