from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

a_element = browser.find_element_by_css_selector('#num1')
a = int(a_element.text)
b_element = browser.find_element_by_css_selector('#num2')
b = int(b_element.text)
y = a + b

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(y)) # ищем элемент с текстом "Python"

button = browser.find_element_by_css_selector(".btn")
button.click()

time.sleep(10)
browser.quit()
