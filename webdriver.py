import re
import os
import time
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_my_match():

	url = "http://static.cricinfo.com/rss/livescores.xml"
	browser_name = "firefox"

	if browser_name == "firefox":

		driver = webdriver.Firefox()

		driver.get(url)

		#assert 'Scores' in driver.title

		py_button = driver.find_elements_by_tag_name('h3')

		match_href = {}

		for links in py_button:
			match_href.update({x.get_attribute('text'): x.get_attribute('href') for x in links.find_elements_by_css_selector('a')})
		print (match_href)

		my_match = [(value) for key, value in match_href.items() if key.startswith("Andhra")]

		time.sleep(5)

		driver.quit()

		return my_match

	if browser_name == "chrome":

		driver = webdriver.Chrome()

		driver.get(url)

		names = driver.find_elements_by_tag_name('title')
		address = driver.find_elements_by_tag_name('link')

		match_href = {}

		for name in names:
			print(name.text)

		for name,links in zip(names,address):
			match_href.update({name.text: links.get_attribute('text')})
		print (match_href)

		my_match = [(value) for key, value in match_href.items() if key.startswith("India")]

		time.sleep(5)

		driver.quit()

		return my_match



def open_my_match(match):

	url = match
	driver = webdriver.Chrome()
	driver.implicitly_wait(10)
	driver.get(url)
	try:
	
		#element = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, "scorecard react-router-link")))
		element = driver.find_element_by_xpath("//*[@id='global-nav-tertiary']/div/ul/li[2]/a")
		element.click()
		page_link = driver.current_url
		print (page_link)
		time.sleep(10)

	
	finally:

		driver.quit()

if __name__=="__main__":
	match = get_my_match()
	print (match[0])
	start = time.time()
	open_my_match(match[0])
	end = time.time()
	print (str(end - start) + " sec")
