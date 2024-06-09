from selenium import webdriver
from selenium.webdriver.firefox.service import Service

import time

geckodriver_path = r"C:\Geckodriver\geckodriver.exe"
service = Service(executable_path=geckodriver_path)
browser = webdriver.Firefox(service=service)
browser.get('https://en.wikipedia.org/wiki/Document_Object_Model')
browser.save_screenshot("dom.png")
time.sleep(5)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
time.sleep(3)
browser.refresh()



