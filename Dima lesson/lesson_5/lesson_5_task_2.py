from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Chrome()

chrome.get("http://uitestingplayground.com/dynamicid")
firefox.get("http://uitestingplayground.com/dynamicid")

for _ in range(3):

    blue_button = chrome.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    blue_button = firefox.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()

sleep(3)




