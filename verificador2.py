usuario = input('Digite o nome de Usuario: ')
senha = input('Digite a senha: ')

if usuario == "admin" and senha == "123":
    print('Acesso concedido')
else:
    print('Acesso negado')