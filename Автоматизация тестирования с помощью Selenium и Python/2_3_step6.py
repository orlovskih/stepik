from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element_by_css_selector(".trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    form = browser.find_element_by_css_selector('#answer')
    form.send_keys(y)

    button = browser.find_element_by_css_selector(".btn")
    button.click()
except:
    pass
finally:
    time.sleep(10)
    browser.quit()