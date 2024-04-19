num = int(input('Informe Sua Idade: '))

if num >= 16:
    print('Pode Votar')
else:
    print('Não pode votar')
if num == 16:
    print('Voto Não Obrigatorio')
elif num >= 18:
    print('Voto Obrigatorio')
