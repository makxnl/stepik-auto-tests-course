from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"

driver = webdriver.Chrome()
driver.get(link2)

num1 = driver.find_element(By.ID, "num1").text
num2 = driver.find_element(By.ID, "num2").text


def sum(num1, num2):
    return str(int(num1) + int(num2))

summ = sum(num1, num2)

select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_value(summ)

button = driver.find_element(By.TAG_NAME, "button").click()

time.sleep(10)

driver.quit()