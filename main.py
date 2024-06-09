from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def initialize_driver():
    PATH = "C:\\Geckodriver\\geckodriver.exe"
    service = Service(PATH)
    driver = webdriver.Firefox(service=service)
    return driver

def search_wikipedia(driver, query):
    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Ждем, пока страница загрузится

def get_paragraphs(driver):
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
    return [paragraph.text for paragraph in paragraphs]

def get_internal_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    return [(link.text, link.get_attribute('href')) for link in links if link.text]

def main():
    driver = initialize_driver()

    try:
        while True:
            query = input("Введите запрос для поиска в Википедии: ")
            search_wikipedia(driver, query)

            while True:
                print("\nВыберите действие:")
                print("1. Листать параграфы текущей статьи")
                print("2. Перейти на одну из связанных страниц")
                print("3. Выйти из программы")

                choice = input("Введите номер действия: ")

                if choice == "1":
                    paragraphs = get_paragraphs(driver)
                    for i, paragraph in enumerate(paragraphs):
                        print(f"Параграф {i + 1}: {paragraph}\n")
                    continue

                elif choice == "2":
                    links = get_internal_links(driver)
                    for i, (text, href) in enumerate(links):
                        print(f"{i+1}. {text} - {href}")

                    link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
                    if 0 <= link_choice < len(links):
                        driver.get(links[link_choice][1])
                        time.sleep(2)  # Ждем, пока страница загрузится

                        while True:
                            print("\nВыберите действие для этой страницы:")
                            print("a) Листать параграфы статьи")
                            print("b) Перейти на одну из внутренних страниц")
                            print("c) Вернуться назад")

                            sub_choice = input("Введите букву действия: ").lower()

                            if sub_choice == "a":
                                paragraphs = get_paragraphs(driver)
                                for i, paragraph in enumerate(paragraphs):
                                    print(f"Параграф {i + 1}: {paragraph}\n")
                                continue

                            elif sub_choice == "b":
                                internal_links = get_internal_links(driver)
                                for i, (text, href) in enumerate(internal_links):
                                    print(f"{i+1}. {text} - {href}")

                                internal_link_choice = int(input("Введите номер ссылки для перехода на внутреннюю страницу: ")) - 1
                                if 0 <= internal_link_choice < len(internal_links):
                                    driver.get(internal_links[internal_link_choice][1])
                                    time.sleep(2)  # Ждем, пока страница загрузится
                                else:
                                    print("Недопустимый выбор. Попробуйте снова.")
                                continue

                            elif sub_choice == "c":
                                break

                            else:
                                print("Недопустимый выбор. Попробуйте снова.")
                    else:
                        print("Недопустимый выбор. Попробуйте снова.")
                    continue

                elif choice == "3":
                    print("Выход из программы.")
                    break

                else:
                    print("Недопустимый выбор. Попробуйте снова.")

            if choice == "3":
                break

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
