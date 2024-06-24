import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']//a")

for country in countries:
    if country.text == "India":
        country.click()


print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))