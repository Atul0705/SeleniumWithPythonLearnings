#End to End testin of a e-commerce website
# topics covered like chaining explicit wait etc
#regularexpressions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class rahulshettyacademy:
    def endtoendTesting(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.find_element(By.XPATH, "//a[text()='Shop']").click()

        phoneName = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for name in phoneName:  # chaining ka use hua hai
            prdname = name.find_element(By.XPATH, "div/h4/a").text
            if prdname == "Blackberry":
                name.find_element(By.XPATH, "div/button").click()

        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

        driver.find_element(By.ID, "country").send_keys("ind")

        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        driver.find_element(By.LINK_TEXT, "India").click()

        driver.find_element(By.XPATH, "//div[contains(@class,'checkbox')]").click()
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        successMsg = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text

        assert 'Success' in successMsg


test = rahulshettyacademy()
test.endtoendTesting()