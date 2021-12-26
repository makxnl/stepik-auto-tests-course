from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

driver = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
driver.get(link)

num = driver.find_element(By.ID, "input_value").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(num)


field = driver.find_element(By.TAG_NAME, "input")
driver.execute_script("return arguments[0].scrollIntoView(true);", field)
field.send_keys(y)

chkbox = driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
chkbox.click()
radio = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
radio.click()
btn = driver.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()
time.sleep(10)

driver.quit()
