import os
import time

tempogeral= 2 #muda aqui o tempo de espera
                #das funções de pausa
def limpartela(delay=tempogeral):
    print("\n")
    time.sleep(delay)
    os.system("clear")

def linha (taml = 42):
   return "-" * taml           
 
def cabecalho(txt):
  print("\n▛               ▜")
  print(txt.center(18))
  print("▙               ▟\n")

def tempo(s=tempogeral):
    time.sleep(s)
    
def escrever (string):
    for ch in string: 
        time.sleep(0.06) 
        print(ch, end='', flush=True)
   
def lifes(hpvil,hpleon):
    print("\nINIMIGO POSSUI {} DE VIDA.".format(hpvil))
    print("\nLEON POSSUI {} DE VIDA".format(hpleon))