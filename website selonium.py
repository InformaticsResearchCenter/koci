# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://198.54.124.245/")
sleep(2)
driver.find_element_by_xpath('//*[@id="s"]').send_keys("joker")
sleep(2)
driver.find_element_by_xpath('//*[@id="searchform"]/span').click()
