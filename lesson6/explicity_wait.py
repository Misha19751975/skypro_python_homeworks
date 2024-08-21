from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # импоротируем класс Selenium для работы с определенными ожиданиями
# коллекция предварительно определенных условий, которые указывают, когда условие ожидания должно считаться выполненным. EC используются вместе с WebDriverWait.
from selenium.webdriver.support import expected_conditions as EC 
driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
# waiter = WebDriverWait(driver, 40)
# модификация скрипта, добавляем третий параметр на вход poll_frequency(англ. «частота опроса»).
waiter = WebDriverWait(driver, 40, 0,1)

driver.get("http://www.uitestingplayground.com/progressbar")

driver.find_element(By.CSS_SELECTOR, "#startButton").click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar"), "75%")
)

driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

print( driver.find_element(By.CSS_SELECTOR, "#result").text )
# читается: найди текст элемента и выведи его в терминал
driver.quit()


