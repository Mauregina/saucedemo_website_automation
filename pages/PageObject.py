from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class PageObject:
    URL_inventory = 'https://www.saucedemo.com/inventory.html'
    class_title_page = 'title'
    txt_title = 'PRODUCTS'

    def __init__(self, browser=None, driver=None):
        #chamado por ProductPage
        if driver:
            self.driver = driver
        # chamado por LoginPage
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            else:
                raise Exception(f'Browser não suportado!')

    def close(self):
        self.driver.quit()