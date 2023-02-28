import pytest
from selenium import webdriver
from pages.login_page import authorization_page

driver = webdriver.Chrome()
driver.implicitly_wait(5) 
enter = authorization_page(driver)

@pytest.fixture()
@pytest.mark.smoke

def pre_test(request):
    enter.load()
def teardown_module(module):
    driver.close()
    
    
def test_login_enter(pre_test):
    enter.login_user('qwerty@mail.ru','123456').chk_logged()