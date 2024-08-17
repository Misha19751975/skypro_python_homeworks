from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

#  браузер Chrome

chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")

# нажимаем ADD Elemment

for _ in range(5):
    add_button = chrome.find_element(
        By.XPATH, '//button[text()="Add Element"]'). click()
    sleep(1)

# Собираем список кнопок DELETE
    chrome_delete_buttons = chrome.find_elements(
        By.XPATH, '//button[text()="Delete"]')

# Выводим на экран размер списка Delete
print(
    f"Размер списка Delete : {len(chrome_delete_buttons)}")

firefox = webdriver.Firefox()

#  браузер firefox

firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

# нажимаем ADD Elemment

for _ in range(5):
    add_button = firefox.find_element(
        By.XPATH, '//button[text()="Add Element"]'). click()
    sleep(1)

# Собираем список кнопок DELETE
    firefox_delete_buttons = chrome.find_elements(
        By.XPATH, '//button[text()="Delete"]')

# Выводим на экран размер списка Delete
print(
    f"Размер списка Delete : {len(firefox_delete_buttons)}")







    
 







