from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class authorization_page:
    URL = 'http://testshop.sedtest-school.ru/users/auth/'
    TITLE = (By.CSS_SELECTOR, 'body > div > div.container.mt-5.col-md-4 > h2 > b')
    input_email = (By.ID, "id_email")
    input_password = (By.ID, "id_password")
    login = (By.CSS_SELECTOR, "body > div > div.container.mt-5.col-md-4 > form > button")
    btn_exit = (By.XPATH, "//*[@id='navbarCollapse']/div/a[4]")

    def __init__(self, driver):
     self.driver = driver

    def load(self):
     self.driver.get(self.URL)
     header = self.driver.find_element(*self.TITLE).text
     assert 'Авторизация' in header

    def login_user(self,email,password):
     self.driver.find_element(*self.input_email).send_keys(email)
     self.driver.find_element(*self.input_password).send_keys(password)
     self.driver.find_element(*self.login).click()
     return self

    def chk_logged(self):
     assert 'Выйти' in self.driver.find_element(*self.btn_exit).text
