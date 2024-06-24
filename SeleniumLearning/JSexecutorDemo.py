from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_obj = webdriver.ChromeOptions()


driver = webdriver.Chrome(options=chrome_obj)
chrome_obj.add_argument("headless")
chrome_obj.add_argument("--ignore-certificates-errors")  #to ignoore not secure connection error in starting
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("Screen.png")