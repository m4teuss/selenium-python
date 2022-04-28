from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(executable_path=r'./chromedriver/chromedriver.exe')
url = 'https://curso-python-selenium.netlify.app/aula_04_b.html'
browser.get(url)

# Funções
def find_by_text(browser, tag, text):
    
    """Encontrar o elemento com o texto `text`.
    
    Argumentos:
        - browser = Intancia do browser [Chrome]
        - Texto  = Elemento da tag (Conteudo que está na tag)
        - Tag = onde o texto será procurado
    
    """
    elementos = browser.find_elements_by_tag_name(tag)  # lista
    for elemento in elementos:
        if elemento.text == text:
            return elemento


nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

# clicar na ordem [1, 2, 3, 4]
for textos_caixas in nomes_das_caixas:
    find_by_text(browser, 'div', textos_caixas).click()


# API Back e Forward (volta e vai)

# clicar na ordem [4, 3, 2, 1]
for textos_caixas in nomes_das_caixas:
    sleep(0.3)
    browser.back()

# clicar na ordem [1, 2, 3, 4]
for textos_caixas in nomes_das_caixas:
    sleep(0.3)
    browser.forward()