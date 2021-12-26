from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)

btn = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

num = driver.find_element(By.ID, "input_value").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(num)

field = driver.find_element(By.TAG_NAME, "input")
field.send_keys(y)
btn = driver.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()
time.sleep(10)

driver.quit()