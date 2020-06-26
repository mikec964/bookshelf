import pytest
from selenium import webdriver

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()

def test_home(test_setup):
    driver.get("http://localhost:5000/")
    assert "Home Page" in driver.title
    # heading = driver.find_element_by_xpath("//h1[1]").text
    assert "Flask" in driver.find_element_by_tag_name("h1").text

