from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

geckodriver_path = r"C:\Geckodriver\geckodriver.exe"
service = Service(executable_path=geckodriver_path)
browser = webdriver.Firefox(service=service)
browser.get('https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0')
#paragraphs = browser.find_elements(By.TAG_NAME,"p")
#for paragraph in paragraphs:
#    print (paragraph.text)
#    input()

hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl=element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

print(hatnotes)

hatnote = random.choice(hatnotes)
link=hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)


