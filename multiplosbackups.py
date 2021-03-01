# Python-Script
# Script-name: multiplosbackups.py
# Autor: evttenorio
import os


diretoriosTXT = open("diretorios.txt", "r")
array_de_Listas=[]

for linha in diretoriosTXT:
  string_linha = linha.strip()
  lista_da_Linha = string_linha.split()
  array_de_Listas.append(lista_da_Linha)
  #diretoriosTXT.close()  

for caminho in array_de_Listas:
  origem = str(caminho[:1]).strip('[').strip(']').strip('"').strip(',')
  destino = str(caminho[1:2]).strip('[').strip(']').strip('"').strip(',')
  #caminho2 = str(caminho[1:2]).replace('[','').replace(']','')
  rsync = ('rsync -raAXtuv '+origem+' '+destino)
  os.system(rsync)
