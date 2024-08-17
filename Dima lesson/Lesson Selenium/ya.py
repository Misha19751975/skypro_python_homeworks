# from selenium import webdriver

# driver = webdriver.Chrome()


from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/")
driver.get("https://vk.com/") #открывается вторая страница

driver.back() # идти на предыдущую страницу
driver.forward() # идти на следующую страницу

driver.get("https://ya.ru/")
driver.get("https://vk.com/")
 
# for x in range(1, 10):  # создаем цикл
	# driver.back()
	# driver.forward()

driver.refresh() # обновление страницы

 # driver.set_window_size(значение длины окна, значение ширины окна)

driver.set_window_size(640, 460) #окно браузера уменьшится под параметры

sleep(15) #установили «засыпание» браузера на 50 секунд