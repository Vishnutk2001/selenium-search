from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("testcase started")
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("iphones")
time.sleep(1)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(5)
driver.close()
print("test case completed")