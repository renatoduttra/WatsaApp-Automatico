from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pandas as pd


contatos_df = pd.read_excel("Enviar.xlsx") #lista
display(contatos_df) # printa a tabela

navegador = webdriver.Firefox()
navegador.get("https://web.whatsapp.com/")


while len(navegador.find_elements_by_id("side")) < 1: #paremetro side que espera carregar o site
    time.sleep(1) #espera

# faça o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}") #variavel texto codifica
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}" # linki inteligente
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1: #paremetro side que espera carregar o site
        time.sleep(1) #espera
    navegador.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10) #espera

    #wa.me/5561994081733?text=