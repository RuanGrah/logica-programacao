numero1 = float(input('Informe o Numero 1 : '))
operacao = str(input('Informe a Operação'))
numero2 = float(input('Informe o Numero 2 : '))
resultado = 0

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2

print('Resultado :', float(resultado) )
