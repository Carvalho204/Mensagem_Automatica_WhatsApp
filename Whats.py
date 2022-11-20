#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\JC\AppData\Local\Google\Chrome\User Data\Profile Selenium')
navegador = webdriver.Chrome(options=options)

navegador.get('https://web.whatsapp.com/')


# In[10]:


import pandas as pd

tabela = pd.read_excel("Envios.xlsx")
display(tabela)


# In[11]:


import urllib
import time

for linha in tabela.index:
    
    nome= tabela.loc[linha,'nome']
    mensagem= tabela.loc[linha,'mensagem']
    arquivo= tabela.loc[linha,'arquivo']
    telefone= tabela.loc[linha,'telefone']
    
    texto = mensagem.replace("fulano", nome)
    texto = urllib.parse.quote(texto)
    print(texto)
    
    link = f'https://web.whatsapp.com/send?phone={telefone}o&text={texto}'
    
    navegador.get(link)
    
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    time.sleep(2)    


# In[ ]:




