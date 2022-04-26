from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(executable_path=r'./chromedriver/chromedriver.exe')
url = 'https://curso-python-selenium.netlify.app/aula_03.html'
browser.get(url)

sleep(1)



a = browser.find_element_by_tag_name('a')


for click in range(10):
    ps = browser.find_elements_by_tag_name('p')
    a.click()
    # [-1] -> pegando o ultimo p clicado 
    print(f'valor do ps {ps[-1].text} valor do click {click}')
    print(f'Os valores são iguais {ps[-1].text == str(click)}')




