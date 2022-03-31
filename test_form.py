import pytest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def setup():
    global product, driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.maximize_window()
    yield
    time.sleep()
    driver.close()

def test_searchproducts(setup):
    driver.get('https://iprimedtraining.herokuapp.com/')
    time.sleep(5)
    driver.find_element_by_name("name").send_keys("Nithin")
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[4]").click()
    driver.find_element_by_name("fcheckbox").click()
    driver.find_element_by_name("subbtn").click()
    time.sleep()




