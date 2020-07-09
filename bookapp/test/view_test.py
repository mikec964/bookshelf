import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def web_setup():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
#    driver.maximize_window()
    yield
    driver.close()
    driver.quit()

def test_home(web_setup):
    driver.get("http://localhost:5000/")
    assert "Home Page" in driver.title
    # heading = driver.find_element_by_xpath("//h1[1]").text
    assert "Flask" in driver.find_element_by_tag_name("h1").text

def test_create_book(web_setup):
    driver.get("http://localhost:5000/add")
    assert "Add Book" in driver.title
    assert len(driver.find_elements_by_id("title")) == 1
    assert len(driver.find_elements_by_id("description")) == 1
    assert len(driver.find_elements_by_id("isbn")) == 1
    assert len(driver.find_elements_by_id("submit")) == 1

def test_read_book(web_setup):
    driver.get("http://localhost:5000/book/1")
    assert len(driver.find_elements_by_id("title")) == 1
    assert len(driver.find_elements_by_id("description")) == 1
    assert len(driver.find_elements_by_id("isbn")) == 1

def test_update_book(web_setup):
    driver.get("http://localhost:5000/update/1")
    elem = driver.find_element_by_id("title")
    orig_title = elem.text
    new_title = "All New Book Title"
    elem.clear()
    elem.send_keys(new_title)
    driver.find_element_by_id("submit").click()
    driver.get("http://localhost:5000/book/1")
    assert driver.find_element_by_id("title").text == new_title
