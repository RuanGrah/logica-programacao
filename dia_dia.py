import time
print("Acordou")
print('Tomar Café')
clima = input("Dia de sol ou Não?: ")

if clima == "Sim":
    print("Ir a Praia")
else:
    print("Ver Tv")
print("Almocar")

energia = input("Informe se esta cansado: ")

if energia == "Sim":
    print("Cochilar")
else:
    print("Ir Jogar Bola")
print("Passear")
print("Jantar")
print("Dormir")
time.sleep(0.25) 