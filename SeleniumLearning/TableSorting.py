from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
# visit the site
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on the coloumn head to sort
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# to store the sorted elements in the veggilist
veggilist = []
veggilist = driver.find_elements(By.XPATH, "//tr//td[1]")

browsersortedVeggiList = []
for ele in veggilist:
    browsersortedVeggiList.append(ele.text)

assertinglist = browsersortedVeggiList.copy()
assertinglist.sort()

assert assertinglist == browsersortedVeggiList
