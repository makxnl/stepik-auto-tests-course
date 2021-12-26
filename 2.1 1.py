from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/math.html"
driver = webdriver.Chrome()
driver.get(link)

x_element = driver.find_element(By.CSS_SELECTOR, "span#input_value")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

field = driver.find_element(By.CSS_SELECTOR, "input#answer")
field.send_keys(y)
chkbox = driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
chkbox.click()
radio = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
radio.click()

btn = driver.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()
time.sleep(10)

driver.quit()

