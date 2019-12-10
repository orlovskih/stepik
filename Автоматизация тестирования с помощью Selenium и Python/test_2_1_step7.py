from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('#treasure')
x = x_element.get_attribute("valuex")
y = calc(x)

form = browser.find_element_by_css_selector('#answer')
form.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()
option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()
button = browser.find_element_by_css_selector(".btn")
button.click()

time.sleep(10)
browser.quit()