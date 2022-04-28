from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

browser = webdriver.Chrome(executable_path=r'./chromedriver/chromedriver.exe')
url = 'https://curso-python-selenium.netlify.app/aula_04_b.html'
browser.get(url)

url_parseda = urlparse(browser.current_url)