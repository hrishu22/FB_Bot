from selenium import webdriver

browser=webdriver.Chrome()
browser.get("https://www.facebook.com")

email=browser.find_element_by_id('email')
email.send_keys('Your Email')
passq=browser.find_element_by_id('pass')
passq.send_keys('YOur password')
submit=browser.find_element_by_id('u_0_b')
submit.click()
