import time
numero1 = int(input('Informe o numero inicial de contagem: '))
numero2 = int(input('Informe o numero final de contagem:  '))
for i in  range(numero1, numero2):
    print('Resultado:', int(i))
    time.sleep(0.25)
