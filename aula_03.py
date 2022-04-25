from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path=r'./chromedriver/chromedriver.exe')
browser.get('https://google.com')