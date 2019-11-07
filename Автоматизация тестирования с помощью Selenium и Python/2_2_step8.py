from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element_by_name('firstname')
input1.send_keys("Ivan")
input2 = browser.find_element_by_name('lastname')
input2.send_keys("Petrov")
input3 = browser.find_element_by_name('email')
input3.send_keys("ivan@petrov.com")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'step8.txt')           # добавляем к этому пути имя файла
input4 = browser.find_element_by_css_selector('[type="file"]')
input4.send_keys(file_path)

button = browser.find_element_by_css_selector(".btn")
button.click()

time.sleep(10)
browser.quit()