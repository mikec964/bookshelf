import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The web server must be running for these tests to work:
#   source venv, then `python app.py`

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


@pytest.mark.dependency()
def test_create_book(web_setup):
    driver.get("http://localhost:5000/add")
    assert "Add Book" in driver.title
    driver.find_element_by_id("title").send_keys("Entirely New Book")
    driver.find_element_by_id("description").send_keys("This book is so new I can hardly describe it.")
    driver.find_element_by_id("isbn").send_keys("111-222-3")
    driver.find_element_by_id("submit").click()

    time.sleep(5)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.title_is("Flask Stub - Home Page"))

    driver.get("http://localhost:5000/book/3")
    assert len(driver.find_elements_by_id("title")) == 1


@pytest.mark.dependency(depends=['test_create_book'])
def test_read_book(web_setup):
    driver.get("http://localhost:5000/book/3")
    assert driver.find_element_by_id("title").text == "Entirely New Book"
    assert len(driver.find_elements_by_id("description")) == 1
    assert len(driver.find_elements_by_id("isbn")) == 1


@pytest.mark.dependency(depends=['test_create_book'])
def test_update_book(web_setup, depends=[test_create_book]):
    driver.get("http://localhost:5000/update/3")
    elem = driver.find_element_by_id("title")
    new_title = "All New Book Title"
    elem.clear()
    elem.send_keys(new_title)
    driver.find_element_by_id("submit").click()
    time.sleep(5)
    driver.get("http://localhost:5000/book/3")
    assert driver.find_element_by_id("title").text == new_title
