# зайти в лабиринт
# найти книги по слову Python
# собрать все карточки товаров
# вывести в консоль информацию: название + автор + цена

# from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By   # импортируем класс by из Selenium
from selenium.webdriver.common.keys import Keys # импортруем модуль, ответственный за нажатие клавиш


# зайти на лабиринт
driver.get("https://www.labirint.ru/")

# найти книги по слову Python
search_locator = "#search-field" #мы уже создали переменную со значением локатора
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)  #помещаем переменную
search_input.send_keys("Python")  #отправить значение Python в поисковую строку
search_input.send_keys(Keys.ENTER) #нажать кнопку ENTER

# собрать все карточки товаров
driver.find_elements(By.CSS_SELECTOR, "div.product-card") # определяем все элементы (60 книг)
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card") # записываем все элементы в переменную
print(len(books)) #вывести длину списка books

# вывести в консоль информацию: название + автор + цена
# for book in books:
	# print(book.text)    # выведем всю информацию по всем 60 книгам

# for book in books:
	# author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text # Сохраним эту информацию в переменную autor и зафиксируем текст через команду text
	# print(author)
	
for book in books:
	title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text #оздаем переменную и сохраняем в нее локатор поиска названмяя книги
	price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text #оздаем переменную и сохраняем в нее локатор поиска цены книги

	author = " " #ожидается ошибка, поэтому значение переменной пока не определяем
	try: #Python сам попробует определить значение
		author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
	except: #если не получится, то значение мы задали сами
		author = "Автор не указан"

	print(author + "\t" + title + "\t" + price) # выводим информацию в консоль с разделителем
	
	

