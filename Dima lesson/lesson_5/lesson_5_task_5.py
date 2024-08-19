from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    input_field_ch = driver.find_element(By.TAG_NAME, "input")
    input_field_ch.send_keys("1000")
    sleep(2)
    input_field_ch.clear()
    sleep(2)
    input_field_ch.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.quit

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    sleep(2)
    input_field.clear()
    sleep(2)
    input_field.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.quit

    