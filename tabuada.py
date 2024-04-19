import time
tabuada = int(input('Informe a tabuada desejada: '))

for i in  range(0,11):
    resultado = i * tabuada
    print('Resultado: ', int(resultado))
    time.sleep(0.25)
    