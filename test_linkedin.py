from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
print("testcase started")

driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("LinkedIn")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
driver.get("https://www.linkedin.com/login")
driver.find_element_by_name("session_key").send_keys("8667511846")
time.sleep(1)
driver.find_element_by_name("session_password").send_keys("vishnu2001")
driver.find_element_by_class_name("login__form_action_container ").click()
driver.find_element_by_id("ember27").click()
driver.find_element_by_id("ember28").click()
time.sleep(7)
driver.close()
print("testcase completed")
