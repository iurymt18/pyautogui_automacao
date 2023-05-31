

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

#entrar no sistema da empresa
pyautogui.hotkey("win", "r")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(2)


# #pegar posição do cursor
# time.sleep(5)
# print(pyautogui.position())

#fazendo login no sistema
pyautogui.click(x=723, y=357)
pyautogui.write("meulogin")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.click(x=685, y=490)
time.sleep(2)
#baixando base de dados do sistema
pyautogui.click(x=515, y=332)
pyautogui.click(x=599, y=710)
time.sleep(5)

#importando base de dados

tabela = pd.read_csv(r"C:\Users\Monteiro\Downloads\Compras.csv", sep=';')
print(tabela)

#calcular indicadores
#total gasto
total_gasto = tabela["ValorFinal"].sum()
#quantidade
quantidade = tabela["Quantidade"].sum()
#preco medio
preco_medio = total_gasto / quantidade
print(total_gasto, quantidade, preco_medio)


texto ="""" """""


import pyperclip
#enviar dados por e-mail
pyautogui.hotkey("ctrl", "t") 
pyautogui.write("gmail.com")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=96, y=173)
pyautogui.write("iurymt18@gmail.com")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("Relatorio de compras")
pyautogui.press("tab")
texto = f"""
Prezados,
Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}


"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")

