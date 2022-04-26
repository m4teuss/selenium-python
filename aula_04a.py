from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(executable_path=r'./chromedriver/chromedriver.exe')
url = 'https://curso-python-selenium.netlify.app/aula_04_a.html'
browser.get(url)


# <ul> -> lista não ordenadas
# find_element  -> retorna o primeiro que econtrar na hierarquia do DOM
lista_não_ordenada = browser.find_element_by_tag_name('ul') # 1
lis = lista_não_ordenada.find_elements_by_tag_name('li')    # 2
print(lis[0].find_element_by_tag_name('a').text)            # 3


"""
1# Buscamos `ul`
2# Buscamos todos `li`
3# No primeiro `li`, buscamos `a` e pegamos o seu texto 
"""
