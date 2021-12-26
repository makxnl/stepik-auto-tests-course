from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(link)

price100 = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.ID, "book")))
button.click()

num = driver.find_element(By.ID, "input_value").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(num)

field = driver.find_element(By.TAG_NAME, "input")
field.send_keys(y)
btn = driver.find_element(By.ID, "solve")
btn.click()
time.sleep(10)

driver.quit()

