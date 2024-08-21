from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # не забудьте импортировать класс By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru") #переход на сайт

txt = driver.find_element(By.CSS_SELECTOR, 'a[data-statlog="2informers.stocks.item.1"]').text # рабочий локатор к файлу elevent_propeties
print(txt)
