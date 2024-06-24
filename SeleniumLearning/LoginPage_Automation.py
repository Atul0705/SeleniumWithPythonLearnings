from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

#locating name field using css selector CSS Selector syntax = tagmane[attribute='attributename']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")

#username locating
driver.find_element(By.NAME , "email").send_keys("rahulshetty1234@gmail.com")

#password locating
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")

#chechbox locating
driver.find_element(By.XPATH, "//*[@id='exampleInputPassword1']").click()


#submitting the form
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

#getting the message
msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(msg)

assert "Succ" in msg

#handleing dropdown static dropdown

dropdown = Select(driver.find_element(By.XPATH,"//*[@id='exampleFormControlSelect1']"))
dropdown.select_by_index(1)
