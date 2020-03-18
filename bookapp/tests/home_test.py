from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_home():
    driver.get("http://localhost:5000/")
    assert "Home Page" in driver.title

def test_greeting():
    driver.get("http://localhost:5000/")
    # heading = driver.find_element_by_tag_name("h1").text
    heading = driver.find_element_by_xpath("//h1[1]").text
    assert "Flask" in heading

def test_teardown():
    driver.close()
    driver.quit()

