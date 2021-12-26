from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/huge_form.html"

try:
    driver = webdriver.Chrome()
    driver.get(url)
    elements = driver.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = driver.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла