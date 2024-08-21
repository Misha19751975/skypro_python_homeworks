from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waint = WebDriverWait(driver, 50, 0.)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
waint.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))
get_attribute = driver.find_element(By.ID, "award").get_attribute("src")

print(get_attribute)

driver(quit)






