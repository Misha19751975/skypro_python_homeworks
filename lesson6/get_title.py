from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

browser.get("https://rzd.ru/") #  методы для перехода на страницу (get) и сбора названия вкладки (title)
browser.title

current_title = browser.title # результат метода сохраняем в переменную
print(current_title) # печать в консоли

browser.quit() # закрытие браузера

