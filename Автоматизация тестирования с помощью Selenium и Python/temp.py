from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/math.html"
browser.get(link)

people_radio = browser.find_element_by_id("peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked == "true", "People radio is not selected by default"
robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robots_checked: ", robots_checked)
assert robots_checked is None

button = browser.find_element_by_class_name('btn')
button_disabled = button.get_attribute("disabled")
print("value of button_disabled: ", button_disabled)

time.sleep(10)
button_disabled = button.get_attribute("disabled")
print("value of button_disabled: ", button_disabled)

browser.quit()