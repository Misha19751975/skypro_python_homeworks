from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # не забудьте импортировать класс By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru") #переход на сайт

# usd = driver.find_element(By.CSS_SELECTOR, 'a[title*="USD"]')  # локатор элемента курс доллара

# txt = usd.txt #в переменную с методом text соберется информация об элемент
txt = driver.find_element(By.CSS_SELECTOR, 'a[data-statlog="2informers.stocks.item.1"]').text 
print(txt) #запрос выведет информацию из переменной в терминал

tag = driver.find_element(By.CSS_SELECTOR, 
'a[data-statlog="2informers.stocks.item.1"]').tag_name #собираем информацию о теге в переменную тут наименование теге (вообще то обычно не нужен)
print(tag)

id = driver.find_element(By.CSS_SELECTOR, 
'a[data-statlog="2informers.stocks.item.1"]').id #собираем информацию об идентификаторе в данном случае id
print(id)
# id элемента постоянно меняется , поэтому не заносим его в переменную, а обращаемя через локатор каждый раз

href = driver.find_element(
By.CSS_SELECTOR, 'a[data-statlog="2informers.stocks.item.1"]').get_attribute("href") # в его параметрах нам нужно обратиться к конкретному атрибуту элемента. в дангом случае элемента href
print(href)

ff = driver.find_element(By.CSS_SELECTOR,'a[data-statlog="2informers.stocks.item.1"]'.value_of_css_property("font-family"))  # метод получения CSS-свойтвах элемента (шрифт, цвет и т.д)

print(ff)
    

driver.quit() #закрываем драйвер


