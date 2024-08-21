from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# browser.get("https://ya.ru/") # правильное подключение
browser.get("http://ya.ru/") # пробуем небезопасное подключение 

url = browser.current_url # создаем метод current_url и помещаем в переменную url
print(url)

browser.quit()