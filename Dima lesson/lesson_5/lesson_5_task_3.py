from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

for _ in range(3):
    blue_button = driver.find_element(
        "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    sleep(1)

    driver.switch_to.alert.accept()
    sleep(1)

driver = webdriver.Firefox()

driver.get("http://uitestingplayground.com/classattr")

for _ in range(3):
    blue_button = driver.find_element(
        "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    sleep(1)

    driver.switch_to.alert.accept()
    sleep(1)