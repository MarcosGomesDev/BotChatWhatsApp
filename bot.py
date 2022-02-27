from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager 
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') 
time.sleep(10)

contatos = ['Pretinha']

mensagem = 'Te amo <3'

def buscar_contato(contato):
    campo_pesquisa = driver.find_elements(by="xpath", value='//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.send_keys(Keys.ENTER)
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements(by="xpath", value='//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    for c in range(1, 21):
        campo_mensagem[1].send_keys(str(mensagem))
        campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    time.sleep(1)