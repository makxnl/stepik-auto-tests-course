from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
driver.get(link)

fname = driver.find_element(By.NAME, "firstname").send_keys("Ivan")
sname = driver.find_element(By.NAME, "lastname").send_keys("Ivanov")
mail = driver.find_element(By.NAME, "email").send_keys("Mail")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element = driver.find_element(By.ID, "file").send_keys(file_path)
btn = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(10)

driver.quit()



