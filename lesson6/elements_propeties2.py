from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # не забудьте импортировать класс By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/visibility") #переход на сайт

is_displayd = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed() #метод определения видимости
print(is_displayd)
driver.find_element(By.CSS_SELECTOR, "#hideButton").click() #нажатие на Hide
# Opacity 0 окажется скрытой
#еще раз проверим видимость Opacity 0:
is_displayed = driver.find_element(
By.CSS_SELECTOR, "#transparentButton").is_displayed()
sleep(2)
print(is_displayd)