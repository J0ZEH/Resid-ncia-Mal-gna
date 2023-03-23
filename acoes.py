from interface import*
from random import randint

remedio=5
faca=1

vpv =[0, 0.2, 0.2, 0.6, 0.6, 0.6, 1, 1, 2, 2] #Vetor potencia do ataque do vilão
vpl =[0, 0.1, 0.6, 0.6, 0.8, 0.8, 1, 1, 2, 2] #vetor potencia do ataque do leon

ataquebsleon = 40  #ataque base leon
ataquebsvil = 30    #ataque base vilão

def achouremedio(qt): #quantidade de remédios achados
    #limpartela(40)
    global remedio
    remedio = remedio + qt      
    print ("\n\n\nLEON ENCONTROU {} SPRAY(S) DE PRIMEIROS SOCORROS. AGORA LEON POSSUI {}".format(qt,remedio))
    #limpartela(5)

def achoufaca(qt): #quantidade de facas achadas
    #limpartela()
    global faca
    faca = faca + qt    
    print( "\n\n\nLEON ENCONTROU {} FACA(S). AGORA LEON POSSUI {}".format(qt,faca))
    #limpartela(5)
    
def danovil ():
    acao=1
    ale=randint(0,9)
    danoi = vpv[ale]            # calculo da potência do dano
    if (danoi==0):
        acao=0    
    danoi = danoi * ataquebsvil  # calculo da força real do dano
    if (danoi>0):
        acao = danoi/ataquebsvil
    return danoi , acao

def danoleon():
    acao=1
    ale=randint (0, 9)
    danol = vpl[ale]            # calculo da potencia do dano
    if (danol==0):
        acao=0
    danol = danol * ataquebsleon # calculo da forca real do dano
    if (danol>0):
        acao = danol/ataquebsleon    
    return danol , acao

def lutar(vidavilao):
    
    global danol
    #teste
    cabecalho("LEON ATACA")      
    limpartela()#importante
    danol , acao=danoleon()              
    if (acao==0):
        escrever("\n\nINIMIGO SE ESQUIVOU.\n")
        limpartela()
    if (acao>0) and (acao<0.5):
        escrever("\n\nATAQUE FOI FRACO.\n\n")
        limpartela()
    if (acao>=0.5) and (acao<=1):
        escrever("\n\nATAQUE BÁSICO.\n")
        limpartela()   
    if (acao==2):
        cabecalho("CRÍTICO!") 
        limpartela()
    vidavilao=vidavilao - danol        
    if (vidavilao<0):
        vidavilao=0      
 #print(f"\n\n\n\n\nSeu dano foi de {danol}\n")
    return vidavilao

def ataque_inimigo(vidaheroi):
   
    global danol
    #teste   
   
    cabecalho("ATAQUE INIMIGO")
    limpartela()
    danoi , acao =danovil()
    if (acao==0):
        escrever("\n\nLEON ESQUIVOU.\n")
        limpartela()    
    if (acao>0) and (acao<0.5):
        escrever("\n\nATAQUE FRACO.\n\n")
        limpartela()
    if (acao>=0.5) and (acao<=1):
        escrever("\n\nATAQUE BÁSICO.\n")
        limpartela()                  
    if (acao==2):
        cabecalho("CRÍTICO!")
        limpartela()           
    vidaheroi= vidaheroi - danoi    
    if (vidaheroi<0):
        vidaheroi=0      
    print(f"\nO DANO DO INIMIGO FOI DE {danoi}\n")         
   
    print(f"O DANO DO LEON FOI DE {danol}\n")
    #teste
   
    return vidaheroi