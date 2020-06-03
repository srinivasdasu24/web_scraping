"""
Web scraping or controlling using selenium 
https://selenium-python.readthedocs.io/
"""
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://automatetheboringstuff.com")
elem = browser.find_element_by_css_selector("unique css selector")
elem.click()
elem = browser.find_elements_by_css_selector("p")
print(len(elem))

searchElem= browser.find_element_by_css_selector(".search-field")
searchElem.send_keys('zophie')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()


