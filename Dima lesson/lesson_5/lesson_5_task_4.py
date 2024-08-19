import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
try:
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(driver, 10)
    modal_window = wait.until(ES.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(ES.visibility_of_element_located((By.CSS_SELECTOR, '.modal-footer')))

    time.sleep(3)
    close_button.click()
    time.sleep(12)

except Exception as ex:
    print(ex)
finally:
    driver.quit()


driver = webdriver.Firefox()
try:
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(driver, 10)
    modal_window_f = wait.until(ES.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button_f = wait.until(ES.visibility_of_element_located((By.CSS_SELECTOR, '.modal-footer')))

    time.sleep(3)
    close_button_f.click()
    time.sleep(12)

except Exception as ex:
    print(ex)
finally:
    driver.quit()

