ano_nascimento = int(input('Informe o Ano que Nasceu: '))
ano_atual = 2024

idade = ano_atual - ano_nascimento

if idade >= 16:
    print('Pode votar esse ano')
else:
    print('Não pode votar esse ano')
