import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
# implicit wait is global wait

actuallist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
namesofprod = []

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)  # iski jarurat isliye hai kyuki agar jo list hai wo bhale hi 0 element de tab bhi wo succesful wala case
# hai so ese case or implicit wait succesful hote hi aage proceed kar leta hai
driver.find_element(By.CSS_SELECTOR, ".search-button").click()
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
# this is the chaining process in selenium we have shrinked our driver scope only to result scope cause we need to find
# the elements only inn the result Webelement
for result in results:
    namesofprod.append(result.find_element(By.XPATH, "//h4").text)
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# sum validtation

prices = driver.find_elements(By.XPATH, "//tr//td[5]//p")
sum = 0
for price in prices:
    sum += int(price.text)
print(sum)

assert sum == int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)  # explicit wait it will be only applied to the selected webelement
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

print(namesofprod)
assert sum >= float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)  # assingment part
assert namesofprod == actuallist
