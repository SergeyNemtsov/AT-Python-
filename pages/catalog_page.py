from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class search_prod:
    URL = 'http://testshop.sedtest-school.ru/'
    TITLE = (By.CSS_SELECTOR, '#nav_link_main > a')
    search_product = (By.CLASS_NAME, "form-control")
    product_info = (By.CLASS_NAME, "text-info")

    def __init__(self, driver):
     self.driver = driver

    def load(self):
     self.driver.get(self.URL)
     header = self.driver.find_element(*self.TITLE).text
     assert 'Главная' in header



    def search_prod(self,product):
     self.driver.find_element(*self.search_product).send_keys(product, Keys.ENTER)
     assert product in self.driver.find_element(*self.product_info).text
     

