import time
lista = [1,2,3,4,5,6,7,8,9,10]

for item in lista:
    print(f"\n Tabuada de {item} \n")

    numero = item 
    for i in  range(0,11):
        resultado = numero * i
        print(f"{numero} x {i} = {numero * i}")
        time.sleep(0.25)
        