import time
import random as rm
import json






def jogo():
     line = " "
     times1 = 0
     times2 = 0
     times3 = 0
     global car1
     car1 = ["      \______ \n","  1. _/ º º |_ \n"]
     global car2
     car2 = ["       \_______ \n","   2. __/   ° | \n"]
     global car3
     car3 = ["     \______ \n"," 3. _// oo |_"]
     while True:
          

          print(line*times1,car1[0],line*times1,car1[1])
          print(line*times2,car2[0],line*times2,car2[1])
          print(line*times3,car3[0],line*times3,car3[1])
          choice = rm.randint(1,3)
          if choice == 1 : times1 += rm.randint(3,5) ; times2 += rm.randint(3,5) ; times3 += rm.randint(3,5)
          elif choice == 2 : times2 += rm.randint(3,5) ; times1 += rm.randint(3,5) ; times3 += rm.randint(3,5)
          elif choice == 3 : times3 += rm.randint(3,5) ; times1 += rm.randint(3,5) ; times2 += rm.randint(3,5)
          time.sleep(1.5)
          global ganhador
          if times1 >= 30:
               print(f"Car number 1 won the game against Car 2 and Car 3")
               ganhador = 1 
               break
          elif times2 >= 30: 
               print(f"Car number 2 won the game against Car 1 and Car 3")
               ganhador = 2 
               break
          elif times3 >= 30:
               print(f"Car number 3 won the game against Car 1 and Car 2")
               
               ganhador = 3 
               break
def menu() : 

     print("1. Jogar")
     print("2. Sair")
     global r 
     r = int(input("Opção "))
def app() :
     


     while True:
          global car1
          car1 = ["      \______ \n","  1. _/ º º |_ \n"]
          global car2
          car2 = ["       \_______ \n","   2. __/   ° | \n"]
          global car3
          car3 = ["     \______ \n"," 3. _// oo |_"]
          menu()
          if r==2:break
          apostar = input("Você deseja apostar? ")
          if apostar.lower() == "s" or "sim" or "ss": apostar = True
          if apostar : 
               print(car1[0],car1[1])
               print(car2[0],car2[1])
               print(car3[0],car3[1])
               
               with open("saves.json", "r" ) as f:
                    file = json.load(f)
                    jogador = "Zeroocabuloso"
                    for i in file["Jogadores"]:
                         for j in i[f"{jogador}"]:
                              saldo = float(j["Saldo"])
                              
               carro = int(input("Digite o Número do Carro: "))
               valor = float(input(f"Digite o Valor a Apostar no Carro {carro}: "))
               if valor > saldo : print("Valor apostado é maior do que seu saldo") ;print(f"Saldo : {saldo} ") ;print(f"Valor Apostado : {valor}") 
          jogo()        
          if ganhador == carro: print(f"Você ganhou R$",valor*2.5-valor)
          else : saldo = 0;print(f"Você perdeu R${valor}.\nCarro Ganhador: Carro {ganhador} \nCarro Apostado: Carro {carro} \nSaldo : {saldo}")
app()          