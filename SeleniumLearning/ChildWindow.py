from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()

windowHandles = driver.window_handles  # yaha saare window handles ke naam list me store ho gaye hai

driver.switch_to.window(windowHandles[1])

print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowHandles[0])
assert "Ola" in driver.find_element(By.CSS_SELECTOR,"h3").text


