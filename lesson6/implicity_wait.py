from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# создание неявного ожидания
driver.implicitly_wait(20) # поместим метод  ожидания 20 сек для поиска перед переходом на сайт(настариваем драйвер на ожидание)
driver.get("http://www.uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click() # ищем и нажимаем кнопку

#ищем элемент с id="content"
content = driver.find_element(By.CSS_SELECTOR, "#content")

#собираем текст из элемента с тегом p и class="bg-success" 
#через элеменет в content
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()