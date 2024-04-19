import time
contador = 0
numero= int(input('Informe O Numero de Contagem: '))
numero2 = int(input('Informe a ordem de crescencia: '))
while contador < numero:
    contador = contador + numero2
    print('Contador: ', int(contador))
    time.sleep(1)