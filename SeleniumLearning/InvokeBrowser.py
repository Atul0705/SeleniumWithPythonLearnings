#invokin browser visiting www.rahulshettyacademy.com
#get the title name
#get the current url of the page
#close the browser
#print it on console

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)
driver.close()