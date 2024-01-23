import pyautogui
import pandas as pd
import time


    #BOT DE AUTOMAÇÃO DE TAREFAS

# AUTOMATIZAR CADASTROS DE PRODUTOS NO SISTEMA DE UMA EMPRESA
pyautogui.PAUSE = 0.5

#Abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#sleep para esperar carregar
time.sleep(3)
pyautogui.press("tab")

#Fazer login no sistema (ficticio neste caso)
pyautogui.write("seulogin@hotmail.com")
pyautogui.press("tab")
pyautogui.write("senhalogin")
pyautogui.press("tab")
pyautogui.click(x=928, y=561)
time.sleep(3)

#Registro das informações no sistema

tabela = pd.read_csv("produtos.csv")


for linha in tabela.index:
    pyautogui.click(x=725, y=285)
    pyautogui.write(str(tabela.loc[linha]["codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha]["marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha]["tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha]["categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha]["preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha]["custo"]))
    pyautogui.press("tab")
    #verifica se existe informações no campo obs
    if not pd.isna(tabela.loc[linha,"obs"]):
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")
    # Cadastra o produto
    pyautogui.press("enter")
    #Scrolla até o ínicio da página para repetir o processo
    pyautogui.scroll(5000)




