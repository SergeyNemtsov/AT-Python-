import pytest
from selenium import webdriver
from pages.catalog_page import search_prod

driver = webdriver.Chrome()
driver.implicitly_wait(5) 
catalog = search_prod(driver)

@pytest.fixture()
@pytest.mark.slow

def pre_test(request):
    catalog.load()

def teardown_module(module):
    driver.close()

def test_search_producr(pre_test):
    catalog.search_prod('Tesla')
    catalog.search_prod('Google')



