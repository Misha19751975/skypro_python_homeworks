from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep #импортировали метод из пакета

# browser = webdriver.Chrome(service=ChromeService(
ChromeDriverManager().install() #можно записать в одну строку

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# browser = webdriver.Firefox(service=FirefoxService(
GeckoDriverManager().install() #так называется драйвер-менеджер для Firefox

# browser.maximize_window() #для разворачивания окна
# browser.get("https://ya.ru/") #для перехода на нужную страницу
# sleep(5) #для паузы на загрузку контента страницы

# browser.save_screenshot("./ya.png") #для сохранения скриншота
# browser.quit() #для закрытия окна

def make_screenshot(browser):
	browser.maximize_window()
	browser.get("https://ya.ru/")
	sleep(5)
	browser.save_screenshot("./ya_"+browser.name+".png") #изменили
	browser.quit()
	
chrome = webdriver.Chrome(service=ChromeService(
ChromeDriverManager().install()))

ff = webdriver.Firefox(service=FirefoxService(
GeckoDriverManager().install()))

edge = webdriver.Edge(service=EdgeService(
EdgeChromiumDriverManager().install()))

make_screenshot(chrome)
make_screenshot(ff)
make_screenshot(edge)
