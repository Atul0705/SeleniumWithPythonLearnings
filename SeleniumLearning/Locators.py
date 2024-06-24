from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "//*[@type='search']").send_keys("Banana")
driver.find_element(By.XPATH, "//*[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()

