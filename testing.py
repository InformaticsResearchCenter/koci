# -*- coding: utf-8 -*-
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#user_name = "YOUR EMAILID"
#password = "YOUR PASSWORD"
#driver = webdriver.Chrome()
#driver.get("https://www.google.com/")
#element = driver.find_element_by_id("email")
#element.send_keys(user_name)
#element = driver.find_element_by_id("pass")
#element.send_keys(password)
#element.send_keys(keys.RETURN)
#element.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

element = driver.find_element_by_name("q")
element.send_keys("poltekpos")
element.send_keys(keys.RETURN)

 