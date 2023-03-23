from interface import*
from acoes import*
from finais import*
import time 
import sys


#SISTEMA DE BATALHA
hpremedio = 25 # quanto um remédio cura

hpleon = 100 #vida Leonn 
fuga = False

def telademorte():
  limpartela(1.5)
  print("▛               ▜\n   FIM DE JOGO\n▙               ▟\n")
  restart = int(input("O QUE VOCÊ DESEJA FAZER?\nREINICIAR.(1)\nENCERRRAR.(2)\n"))
  if restart == 1:
    menu()
  if restart == 2:
    print("\nOBRIGADO POR JOGAR!")
    sys.exit()

def telademortesaddler():
  limpartela(1.5)
  print("▛               ▜\n   FIM DE JOGO\n▙               ▟\n")
  restart1 = int(input("O QUE VOCÊ DESEJA FAZER?\n\nVOLTAR AO ÚLTIMO CHECKPOINT.(1)\nVOLTAR AO MENU PRINCIPAL.(2)\nENCERRAR.(3)\n"))
  if restart1 == 1:
    limpartela(1.5)
    igreja()
  if restart1 == 2:
    menu()
  if restart1 == 3:
    print("\nOBRIGADO POR JOGAR!")
    sys.exit()

def batalha(hpvil,ataquebsvil,pontos,danox) :#vida vilao,ataque maximo vilao,pontos de vida depois de derrotar
    limpartela(0)                           # e quanto dano extra se aumenta.
    global ataquebsleon #global transforma o valor
    global hpleon       #dessas variáveis globais e trazem pra dentro da funcao batalha
    global fuga            
    while True:         
        if (fuga==True):#testa pra ver se a fuga foi ativada
            
            break      
        if(hpleon<=0):  #testa morte do leon
            telademortesaddler() #como a batalha só acontece contra o saddler, chamo a essa tela de morte que tem como chekcpoint a igreja                   
        if(hpvil<=0):  #testa morte do vilao
            vitoria(hpleon,pontos,ataquebsleon,danox)
            break                                                
        lifes(hpvil,hpleon) #mostra a vida do vilao e do leon
        cabecalho("BATALHA")
        opc=input("1 - LUTAR\n2 - ITEM\n")
        if(opc=="1"):
           limpartela(0)
           hpvil=lutar(hpvil)  
           hpleon=ataque_inimigo(hpleon)         
        if(opc=="2"):
            item()
        if(opc!="1") and (opc!="2"):
            print("\n\nTENTE NOVAMENTE.\n\n".center(42))
            limpartela()                  
        
def item():
    global fuga
    limpartela(0)
    while True:
        global faca
        global remedio
        global hpleon
        print("\nVOCÊ POSSUI:\n{} SPRAY(S) DE PRIMEIROS SOCORROS".format(remedio))
        cabecalho("ITENS")
        opc=input("1 - SPRAY\n2 - VOLTAR\n")
        #if(opc=="0"):                        
            #if( faca > 0):
               #faca = faca - 1
               #fuga=True                                           
               #escrever("\n\nVOCÊ CONSEGUE FUGIR,MAS AGORA LHE RESTA(M) {} FACA(S)".format(faca))       
               #limpartela()
               #break
            #else:
               #escrever("\n\nVOCÊ NÃO CONSEGUE FUGIR, POIS NÃO POSSUI MAIS FACAS.") 
               #limpartela()
               #break                     
                                                 
        if(opc=="1"):                           
            if ( remedio > 0):  
                remedio = remedio - 1   
                hpleon= hpleon +(1*hpremedio)
                print(f"\n\nMAIS {1*hpremedio} DE VIDA.")                                              
                escrever("VOCÊ CONSEGUE SE CURAR, MAS AGORA LHE RESTA(M) {} SPRAY(S) DE PRIMEIROS SOCORROS.".format(remedio))
                limpartela()
                break    
            else:
               escrever("VOCÊ NÃO CONSEGUE SE CURAR POIS NÃO LHE RESTA MAIS SPRAY DE PRIMEIROS SOCORROS.") 
               limpartela()
               hpleon=ataque_inimigo(hpleon)            
               break        
                    
        if(opc=="2"):
            break
       
        if(opc!="1") and (opc!="2"): #and (opc!="3")            
            print("\n\nTENTE NOVAMENTE.\n\n".center(42))            
            limpartela()



#MENU
def menu():
  limpartela(0.001)
  print("                       ◆ RESIDÊNCIA MALIGNA ◆                       ")
  print("BEM-VINDO(A).POR FAVOR, DEIXE O CAPSLOCK ATIVADO ENQUANTO JOGA.\n\n")
  inicio = str(input("-DESEJA INICIAR O JOGO? (S/N)- "))
  if inicio == "S":
    print()
    print()
    pular = str(input("-DESEJA PULAR O MONÓLOGO?(S/N)- "))
    if pular == "N":
      monologo()
      introducao()
    else:
      introducao()
  else:
    print()
    print("NÃO QUER JOGAR? VOCÊ QUEM SABE. SEM PROBLEMAS! OBRIGADO!")

#HISTORIA DO PASSADO DO LEON
def monologo():
  print()
  mono = "1998...\n\nEu nunca vou esquecer.\n\nNesse ano ocorreram terríveis assassinatos nas Montanhas Arklay.\n\nPouco depois, a causa foi descoberta e o mundo inteiro tomou conhecimento das armas produzidas pela Empresa Farmacêutica Internacional, Umbrella.\n\nO vírus se espalhou na comunidade próxima das montanhas, Raccoon City, e atingiu a pequena e tranquila cidade com um golpe devastador, graças a fundação.\n\nNão querendo correr nenhum risco, o Presidente dos Estados Unidos ordenou um plano de contingência… esterilizar Raccoon City.\n\nCom o caso inteiro se tornando público, o governo dos Estados Unidos determinou uma suspensão indefinida da autorização de negócios da Umbrella.\n\nLogo, suas ações caíram e por esses motivos a Umbrella estava acabada.\n\n\nSeis anos se passaram desde aquele horrendo incidente…\n" 
  for ch in mono: 
    time.sleep(0.08) 
    print(ch, end='', flush=True)
  
#INTRODUCAO DO JOGO 
def introducao():
  print()
  print()
  pularintroducao = str(input("-DESEJA PULAR A INTRODUÇÃO DO JOGO?(S/N)- "))
  if pularintroducao == "S":
    jogo()
  else:
    print()
    print()
    introd = "Meu nome é Leon S. Kennedy e eu fui treinado por uma agência secreta seguindo as ordens diretas do Presidente dos EUA. No meu novo cargo, tenho a responsabilidade de proteger o presidente e sua família.Estou aqui pois minha missão é resgatar a sua filha desaparecida.\n\nLogo quando fui encarregado de proteger a filha do presidente, a sequestraram. Essa é a única razão pra eu estar nesta zona rural da Espanha.\n\nSegundo a Inteligência, uma garota parecida foi avistada pelos arredores. Pelo visto, ela foi retida por um grupo ainda não identificado.\n\nQuem diria que meu primeiro dia de trabalho seria uma missão de resgate...?\n" 
    for ch in introd: 
      time.sleep(0.08) 
      print(ch, end='', flush=True)
    jogo()


#'CHEKCPOINT' IGREJA
def igreja():
  print("\nLeon segue pela esquerda e sobe as escadas para a parte de cima da igreja. Avança pelo corredor e avista uma porta com várias luzes e símbolos estranhos, no entanto a passagem para a porta luminosa está sendo barrada por duas grades de aço que parecem funcionar a partir de um dispositivo eletrônico de tranca ou algo assim.\nLeon avança pelo cenário e encontra uma algum tipo de central de operações... há placas indicativas. Uma delas diz:\n\n-PORTA-")
 
  operar = str(input("\n\n-Leon deve operar os controles?(S/N)- "))
  if operar == "S":
    limpartela()
    print("Na tela ao lado dos controles surge a seguinte mensagem:\n\nPara a porta se abrir, digite a 'frase'.\n\nLeon se pergunta que frase é esta, então fica pensando sobre o que encontrou pelo caminho que pode lhe dar a resposta.")
    
    senha = str(input("DIGITE A FRASE CHAVE:\n\n_   _ _ _ _ _    _ _ _ _ _ _ _ _    _ _    _ __ __    _ _ _ _ _ _ _    _ _    _ _ _ _ _ _    _ _ _ _ _ _    _ _ _   -   _ _ _    _ _ _    _    _ _ _ _ _ _    _ _ _  _ _ _ _ _ _    _ _ _ _ _ _ _ _ _ _    _    _ _ _ _ _ _ _ _.\n\n"))
    if senha == "A PORTA LUMINOSA DO LOCAL SAGRADO SE ABRIRA QUANDO UNI VOS SOB O SANGUE DOS NOSSOS ANCESTRAIS A DERRAMAR":
      limpartela(3)
      print("As grades de aço se levantam e nada mais impede Leon de chegar até a porta.\nLeon chega à porta, parece ter alguém do outro lado... ele abre e lá está uma garota loira semelhante a da foto que ele carregava da Ashley Graham.\nA garota, com medo, tenta atacar Leon, que desvia.")
      print("\n------------------------------------------------")
      print("\nLeon: -Ashley? Ei, se acalme. Meu nome é Leon. Estou aqui para te resgatar a pedido do presidente.")
      print("\nAshley: -Meu... pai?")
      print("\nLeon: -Isso. ~LEON MOSTRA SUAS CREDENCIAIS DE AGENTE PARA ASHLEY.")
      print("\nAshley: -Que bom que você apareceu, Leon! Eu estava tão assustada!")
      print("\nLeon: -Não se preocupe! Irei te tirar daqui e vamos voltar para casa.")
      print("\n------------------------------------------------")
      print("\n\n\nLOADING...")
      limpartela(60)
      print("Leon investigou o local em que Ashley estava e encontrou 5 Sprays de Primeros Socorros, desceu as escadas com Ashley e voltou para o Hall da igreja para finalmente pode sair de lá e voltar para os Estados Unidos, entretanto no seu caminho aparece um homem encapuzado.")
      print("\n\n------------------------------------------------")
      print("\nHomem: -A garota virá comigo...")
      print("\nLeon: -Quem é você?")
      print("\nHomem: -Se você quer mesmo saber, me chamo Osmund Saddler. O mestre desta comunidade religiosa.")
      print("\nLeon: -O que você quer?!")
      print("\nSaddler: -Demonstrar ao mundo inteiro nosso poder, é claro. Os Estados Unidos deixarão de mandar no mundo. Por isso sequestramos a filha do presidente.")
      print("\nLeon: -O que você fez com ela?!")
      print("\nSaddler: -Por enquanto... nada. É claro que o governo mandaria um agentizinho para atrapalhar as coisas. Vai ser uma linda festa quando eu acabar com você aqui! De quebra, vou negociar com o presidente pedindo algumas... doações em troca dela. É necessário uma grande quantia de dinheiro pra manter uma igreja com esta em pé.")
      print("\nLeon: Fé e dinheiro não vão te levar a lugar nenhum, Saddler!")
      print("\n------------------------------------------------")
      
      combatesaddler = str(input("-PRESSIONE 'B' PARA BATALHAR CONTRA O SADDLER- "))
      if combatesaddler == "B":
        batalha(300, 20, 0, 0)
        limpartela(1)
        print("Após uma batalha insana, Leon consegue derrotar o Saddler e agora está livre para prosseguir.")
        print("\n\n------------------------------------------------")
        print("\n         RÁDIO DE COMUNICAÇÃO TOCANDO")
        print("\n------------------------------------------------")
        print("\nHunnigan: -Leon! Qual o status da missão?")
        print("\nLeon: -Fico feliz em dizer que cumpri meu objetivo. Podemos sair daqui e voltar para os EUA.")
        print("\nHunnigan: -Fantástico. Tomamos conhecimento que há uma trilha por trás da igreja. Siga por lá que estarei mandando um helicóptero imediatamente para você e para a Ashley.")
        print("\nLeon: -Entedido! Aliás, Hunnigan... que tal sairmos pra comemorar isso quando eu estiver de volta?")
        print("\nHunnigan: -Fico feliz que cumpriu a missão, Leon... risos ... mas devo te lembrar que você ainda está em serviço?")
        print("\nLeon: -... história da minha vida.")
        ("\n------------------------------------------------")

        encerrar = str(input("\n\nLeon chega até o helicóptero. Ashley está feliz por finalmente estar a salvo e Leon satisfeito com o sucesso de sua missão.\nAssim, os dois estão voltando para os Estados Unidos.\n\n-PRESSIONE 'E' PARA ENCERRAR O JOGO.- "))
        if encerrar == "E":
          limpartela()
          print("PARABÉNS! VOCÊ CONCLUIU A HISTÓRIA DO RESIDÊNCIA MALIGNA!\n\nOBRIGADO POR JOGAR!")
        else:
          menu()
       


      else:
        igreja()



    else:
      print("SENHA ERRADA!")
      limpartela(2)
      igreja()
  
  
  else:
    limpartela()
    igreja()


#HISTORIA DO JOGO
def jogo():
  print()
  print("------------------------------------------------\n")
  print("Leon chega em uma casa e resolve perguntar ao morador se ele avistou Ashley Graham, a filha perdida do presidente.\n\nDe repente... o morador se vira contra Leon e o ataca...")
  print()
  combate = str(input("-PRESSIONE 'X' PARA ENTRAR EM COMBATE.- "))
  if combate == "X":
    limpartela()
    #batalha(30,20,0,0)
    #batalha(VIDAINIMIGO, FORÇAINIMGO,GANHODEVIDADOLEON, GANHODEFORÇADOLEON)
    print("\n------------------------------------------------")
    print("\nLeon enfrenta um cidadão hostil que o ataca e agora segue em busca de Ashley.\nEm seguida, seu rádio de comunicação toca.")
    print("\n------------------------------------------------")
    print("\nHunnigan: -Leon, consegue me ouvir? Sou a Ingrid Hunnigan. Irei te dar suporte nesta missão. Lembre de resgatar a Ashley Graham, filha do presidente, a salvo.\nIrei tentar econtrar o máximo de informações que conseguir para lhe ajudar")
    print("\nLeon: -Ótimo. Me deparei um cidadão local hostil. Fui obrigado a neutralizá-lo.")
    print("\nHunnigan: -Entendido. Siga em frente até chegar ao vilarejo. Faça o que for necessário para cumprir com o seu objetivo.")
    print("\nLeon: -Entendido.")
    print("\n------------------------------------------------")
    print("\nLeon prossegue em sua jornada e chega a um vilarejo. Ele explora o lugar em busca de informações ou objetos que possam ajudá-lo a localizar a garota perdida.")
    #achouremedio(2)
    #achoufaca(1)
    print("\nChegando à uma possível saída ele se depara com... calma! O que é isso? Um homem com uma motosserra está a sua espera.")
    combate2 = str(input("\n-PRESSIONE 'L' PARA LUTAR- "))
    if combate2 == "L":
      #batalha(60,40,10,5)
      #print(fuga)
      limpartela()
      print("\n------------------------------------------------")
      print("\nCom um grande esforço Leon consegue avançar pelo caminho que o homem com a motossera, que se autointitulou como Dr. Salvador, bloqueava.\nSeguindo, em uma casinha mais a frente, Leon encontra um arquivo...\n\n")
      print("                       ▛                  ▜\n                          ORDEM DE ALERTA\n                       ▙                  ▟\n")

      print("Recentemente, há informações de que um agente do governo dos EUA está aqui investigando a vila. Não deixe este agente americano entrar em contato com nossa prisioneira. Para aqueles que ainda não foram informados, a prisioneira está presa em uma velha casa além da fazenda. Logo estaremos a levando para a nossa igreja, pois é mais seguro. Ela deve continuar aqui lá segunda ordem. Enquanto isso, não deixe o agente americano se aproximar.\nNão sabemos como o governo americano descobriu a nossa vila. Mas estamos investigando.\nFiquem alertas e LEMBREM-SE:\n\nA porta luminosa do local sagrado se abrirá quando uni-vos sob o sangue dos nossos ancestrais a derramar.\n\n\n\n     Líder da Igreja, Osmund Saddler.\n")
      print("\n------------------------------------------------")
      print("\n         RÁDIO DE COMUNICAÇÃO TOCANDO")
      print("\n------------------------------------------------")
      print("\nHunnigan: -Leon, obtive novas informações. Acreditamos que a Ashley está sendo mantida aprisionada aos arredores de uma igreja próxima a uma saída da vila.")
      print("\nLeon: -Então isso bate com uma nota de um tal de Saddler que achei antes. Encontrei um arquivo dizendo que a Ashley deve ser levada a uma igreja. Isso faz sentido.")
      print("\nHunnigan: -Certo! Isso confirma nossas suspeitas. Siga para a igreja!")
      print("\nLeon: -Entendido. A caminho!")
      print("\n------------------------------------------------")
      print("\nAvançando pelo local, Leon chega até uma fazenda, onde aparece mais um nativo que o ataca, assim como o primeiro com o qual ele se encontrou logo que chegou nos arredores de onde a Ashley tinha sido avistada. Leon revida o ataque e contorna a situação com facilidade.")
      print("\nLeon abre o portão no fim da fazenda e segue pela trilha que o levará até a igreja, quando de repente, do alto de um morro, alguns nativos se juntam para derrubar uma pedra em direção ao Leon para esmagá-lo...\n\n")
      esquiva = str(input("-APERTE 'X' PARA CORRER- "))
      if esquiva == "X":
        limpartela(0.5)
        esquiva1 = str(input("-APERTE 'X' PARA CONTINUAR CORRENDO- "))
        if esquiva1 == "X":
          limpartela(1)
          esquiva2 = str(input("-DIGITE 'ESQUIVAR' PARA O LEON ESQUIVAR DA PEDRA- "))
          if esquiva2 == "ESQUIVAR":
            limpartela(1)
            print("Leon consegue escapar da pedra que segue rolando e se choca contra uma parede.")
            print("\n------------------------------------------------")
            print("\n         RÁDIO DE COMUNICAÇÃO TOCANDO")
            print("\n------------------------------------------------")
            print("\nLeon: -Leon aqui.")
            print("\nHunnigan: -Leon, aparentemente existe um grupo de culto religioso envolvido no sequestro da Ashley Graham. Eles se chamam Los Illuminados. Os cidadãos hostis que você relatou são chamados Ganados.")
            print("\nLeon: -Los Illuminados? Humpf... Que tosco.")
            print("\nHunnigan: -Você está certo. Se apresse e siga para a igreja!")
            print("\n------------------------------------------------")
            print("\nLeon precisa chegar à igreja antes que algo de ruim aconteça. Ele econtra uma passagem subterrânea.\n")
            entrar = str(input("-Leon deve acessar a passagem subterrânea?(S/N)- "))
            if entrar == "S":
              limpartela()
              print("\n------------------------------------------------")
              print("\nLeon entra pela passagem subterrânea, caminha por um tempo e encontra uma escada para voltar para o solo. É sua única saída, então ele sobe. Ao sair se depara com um cemitério e ao final dele é possível avistar... A TORRE DA IGREJA!\n\nMas é óbvio que não seria tão simples chegar até lá. Alguns Ganados estão no cemitério para tentar impedir Leon de prosseguir e, então, Leon precisa enfrentá-los, porém eles estão formando um ataque agrupado e Leon não poderá lidar com cada um individualmente...\n\n")
              
              combate3 = str(input("-PRESSIONE 'E' PARA ESQUIVAR O PRIMEIRO ATAQUE- "))
              if combate3 == "E":
                limpartela()

                combate4 = str(input("Leon desvia do ataque do primeiro ganado, porém outro está vindo e Leon precisa agir rápido.\n\n-PRESSIONE 'A' PARA ATACAR- "))
                if combate4 == "A":
                  limpartela()

                  combate5 = str(input("Leon conseguiu desviar do primeiro Ganado, atacou com sucesso o segundo, mas agora um terceiro se aproxima juntamente do primeiro. Mais uma vez Leon precisa pensar e agir rápido.\n\n-PRESSIONE 'T' PARA LIDAR COM OS INIMIGOS- "))
                  if combate5 == "T":
                    limpartela()
                    print("\n------------------------------------------------")
                    print("\nLeon sacou sua pistola e conseguiu disparar tiros contra os ganados, assim os derrotando. Agora ele caminha em direção a igreja que está tão próxima.")
                    print("\n\n―――――――――――――――――――――――――――――――――――――――――――――――――")
                    print("\n               PORTA DA IGREJA")
                    print("\n―――――――――――――――――――――――――――――――――――――――――――――――――\n\n")
                    
                    opcaodireitaesquerda = str(input("Leon consegue entrar na Igreja. O que ele deve fazer?\nSeguir pela direita.(D)\nSeguir pela esquerda.(E)\n"))
                    if opcaodireitaesquerda == "D":
                      limpartela(3)
                      print("Leon encontra um pedaço de papel rasgado, mas é possível ler um pouco do final.\nDiz:\n\nA p rta l mi osa do local s grado se abri   quando u  -vos sob o        dos nossos ancest  is a derram r.")
                      igreja()


                    else:
                      limpartela(3)
                      igreja()
                    


                  else:
                    telademorte()


                else:
                  telademorte()

              
              else:
                telademorte()
            

            else:
              limpartela(2)
              print("*ERA A ÚNICA FORMA DE PROSSEGUIR. VOCÊ NÃO QUER SALVAR A ASHLEY?*")
              limpartela(5)
              telademorte()

          else:
            telademorte()
        
        else:
          telademorte()

      else:
        telademorte()

    else:
      menu()


  else:
    menu()




menu()
