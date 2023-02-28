from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class basket:
    URL = 'http://testshop.sedtest-school.ru/product/15/'
    TITLE = (By.CSS_SELECTOR, '#nav_link_main > a')
    btn_basket = (By.XPATH, "//*[@id='in_cart_link_15']")
    enter_basket = (By.CSS_SELECTOR, "#navbarCollapse > div > a:nth-child(1) > img")
    qty_car = (By.CLASS_NAME, 'form-control')
    price_car = (By.CSS_SELECTOR, 'body > div.container > div > div.col-md-2 > span:nth-child(3)')
    btn_delete = (By.CSS_SELECTOR, 'body > div.container > div > div.col-md-10 > div > div > div > div > div:nth-child(4) > a')
    basket_empty = (By.CSS_SELECTOR, 'body > div.container > div > div > h1')
    all_qty = (By.CSS_SELECTOR,'body > div.container > div > div.col-md-10 > div > div > div > div > div.col-md-3 > div > div.col-md-10')

    def __init__(self, driver):
     self.driver = driver

    def load(self):
     self.driver.get(self.URL)
     header = self.driver.find_element(*self.TITLE).text
     assert 'Главная' in header



    def add_in_basket(self):
     self.driver.find_element(*self.btn_basket).click()
     self.driver.find_element(*self.enter_basket).click()
     assert '6500000.0 р' in self.driver.find_element(*self.price_car).text
     assert 'В наличии 3шт' in self.driver.find_element(*self.all_qty).text
     assert  '1' in self.driver.find_element(*self.qty_car).get_attribute('value')

    def set_qty(self,qty):
     self.driver.find_element(*self.qty_car).send_keys(Keys.DELETE,qty)
     self.driver.find_element(*self.qty_car).send_keys(Keys.ENTER)
     assert '13000000.0 р' in self.driver.find_element(*self.price_car).text
     assert  '2' in self.driver.find_element(*self.qty_car).get_attribute('value')

    def del_prod(self):
     self.driver.find_element(*self.btn_delete).click()
     assert 'Ваша корзина пуста :(' in self.driver.find_element(*self.basket_empty).text


    
