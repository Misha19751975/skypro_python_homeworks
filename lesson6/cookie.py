from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

my_cookie = { #переменная с объектом
	'name': 'cookie_policy', # ключ 
	'value': '1'}            # значение

driver.get("https://labirint.ru/") # идем на сайт Лабиринт
driver.add_cookie(my_cookie) #добавление cookie в новую переменную 

# cookies = driver.get_cookies() #переменная, в которую соберутся cookies
# print(cookies) #запрос на вывод данных в терминал

cookie = driver.get_cookie('PHPSESSID') #положили метод в переменную cookie, обращаемся к конкретной куки
print(cookie) #попросили вывести данных по этой cookie в терминал

# driver.delete_all_cookies() #удаление всех cookie
# driver.delete_cookie('cookie_policy') # удаление отдельного куки

# driver.refresh() #обновление страницы

# sleep(10) # побудем 10 сек
driver.quit() # закроем сайт
