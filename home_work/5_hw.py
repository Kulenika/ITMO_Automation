from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://saucedemo.com/')

# поиск элемента Username
icon1 = driver.find_element(By.CSS_SELECTOR, '#user-name')
if icon1 is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

# поиск элемента Password
icon2 = driver.find_element(By.CSS_SELECTOR, '#password')
if icon2 is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

# поиск элемента Submit
icon3 = driver.find_element(By.CSS_SELECTOR, '#login-button')
if icon3 is None:
    print('Элемент не найден')
else:
    print('Элемент найден')