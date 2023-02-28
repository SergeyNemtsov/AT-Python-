import pytest
from selenium import webdriver
from pages.car_page import car_info

driver = webdriver.Chrome()
driver.implicitly_wait(5) 
car = car_info(driver)
@pytest.fixture()
@pytest.mark.slow

def pre_test(request):
    car.load()
def teardown_module(module):
    driver.close()

def test_info_car(pre_test):
    car.info_car_Tesla()
    