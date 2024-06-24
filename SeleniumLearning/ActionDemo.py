

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service()
driver = webdriver.Chrome(service= service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()