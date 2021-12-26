from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()
driver.get(link)

img_element = driver.find_element(By.CSS_SELECTOR, "img")
x = img_element.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

field = driver.find_element(By.CSS_SELECTOR, "input#answer")
field.send_keys(y)
chkbox = driver.find_element(By.ID, 'robotCheckbox')
chkbox.click()
radio = driver.find_element(By.ID, 'robotsRule')
radio.click()

btn = driver.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()
time.sleep(10)

driver.quit()

