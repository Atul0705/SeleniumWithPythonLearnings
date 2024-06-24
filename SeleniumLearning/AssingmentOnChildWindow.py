from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window() #maximize the window
driver.implicitly_wait(5)  #adding global wait


#opening the url
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

#clicking on the link
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()

#storing the windows handles
windowHandles = driver.window_handles
driver.switch_to.window(windowHandles[1])

#grabbing the text
msg = driver.find_element(By.CSS_SELECTOR,".im-para.red").text
print(msg)
msgList = msg.split(" ")
print(msgList)


#finding the username in list
username = ""
word: str
for word in msgList:
    if "@" in word:
        username = word.title()


print(username)

#switching back to parent window
driver.switch_to.window(windowHandles[0])

#locating username
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(username)

#locating password
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("1234")

#selecting the checkbox
driver.find_element(By.CSS_SELECTOR,"#terms").click()

#subbimioting the form
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()

#adding explicit wait to invalid msg occurance

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger col-md-12']")))

#getting the error button
AlertMsg = driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text
print(AlertMsg)

#asserting in alertmsg
assert "Incorrect" in AlertMsg

#close the browser
driver.close()