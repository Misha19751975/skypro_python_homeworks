from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By #не забудьте импортировать класс By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru") #переход на сайт

element = driver.find_element(By.CSS_SELECTOR, "#text") #поиск элемента
element.send_keys("t", "e", "s", "t", "skypro") #отправляем текст
sleep(3)
# element.clear() #очищаем текстовое поле
sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click() # кликаем на кнопку найти , находим ее по локатору
sleep(3)


# print(element) #отображение результата в терминале
driver.quit() #закрытие драйвера