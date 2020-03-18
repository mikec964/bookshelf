from selenium import webdriver

driver = webdriver.Firefox()

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://localhost:5000/")
assert "Home Page" in driver.title

driver.close()
driver.quit()
