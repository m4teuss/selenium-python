from selenium import webdriver
from selenium.webdriver.common.by import By

# Abrir browser (selenium webdriver)
browser = webdriver.Chrome(executable_path=r'./chromedriver/chromedriver.exe')
url = 'https://curso-python-selenium.netlify.app/aula_04_a.html'
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

def find_by_href(browser, link):

    """Encontrar o elemento `a` com o link `a`.
    
    Argumentos:
        - browser = Intancia do browser [Chrome]
        - link = link das tags <a> (ancora)
    """

    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return  elemento


# Chamando função 
elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')
link_ddg = find_by_href(browser, 'ddg')