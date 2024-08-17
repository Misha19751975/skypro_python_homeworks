from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
input_name = driver.find_element(By.ID, "username")
input_name.send_keys("tomsmith")
sleep(2)
input_pass = driver.find_element(By.ID, 'password')
input_pass.send_keys("SuperSecretPassword!")
sleep(2)
button = driver.find_element(By.TAG_NAME, "button")
button.click

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
input_name = driver.find_element(By.ID, "username")
input_name.send_keys("tomsmith")
sleep(2)
input_pass = driver.find_element(By.ID, 'password')
input_pass.send_keys("SuperSecretPassword!")
sleep(2)
button = driver.find_element(By.TAG_NAME, "button")
button.click