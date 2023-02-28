from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class car_info:
    URL = 'http://testshop.sedtest-school.ru/product/15/'
    TITLE = (By.CSS_SELECTOR, '#nav_link_main > a')
    type_info = (By.CSS_SELECTOR, "body > div.container > h5 > a")
    car_info = (By.CLASS_NAME, "text-info")
    price_info = (By.CSS_SELECTOR, "body > div.container > div:nth-child(3) > div:nth-child(2) > div > div > div > div:nth-child(2) > span:nth-child(1)")
    old_price_info = (By.CSS_SELECTOR, "body > div.container > div:nth-child(3) > div:nth-child(2) > div > div > div > div:nth-child(2) > span:nth-child(3)")

    def __init__(self, driver):
     self.driver = driver

    def load(self):
     self.driver.get(self.URL)
     header = self.driver.find_element(*self.TITLE).text
     assert 'Главная' in header



    def info_car_Tesla(self):
     assert 'Машины' in self.driver.find_element(*self.type_info).text
     assert 'Tesla' in self.driver.find_element(*self.car_info).text
     assert '6500000.0 р' in self.driver.find_element(*self.price_info).text
     assert '7000000.0 р' in self.driver.find_element(*self.old_price_info).text


