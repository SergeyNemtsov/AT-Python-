import pytest
from selenium import webdriver
from pages.basket_page import basket



driver = webdriver.Chrome()
driver.implicitly_wait(5) 
product = basket(driver)
@pytest.fixture()
@pytest.mark.smoke

def pre_test(request):
    product.load()

def teardown_module(module):
    driver.close()
    
    
def test_qty_in_basket(pre_test):
    product.add_in_basket()
    product.set_qty('2')
    product.del_prod()

    

