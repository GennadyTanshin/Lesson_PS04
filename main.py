from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

geckodriver_path = r"C:\Geckodriver\geckodriver.exe"
service = Service(executable_path=geckodriver_path)
browser = webdriver.Firefox(service=service)
browser.get('https://en.wikipedia.org/wiki/Document_Object_Model')
time.sleep(10)
browser.quit()




