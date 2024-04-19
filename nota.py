aluno = input("Informe o nome do aluno: ")
serie = input('Informe a Serie do aluno: ')
matricula = input('Informe a matricula do aluno: ')
professor = input('Informe o nome do professor: ')

quantidade_notas = int(input("Digite a quantidade de notas: "))
soma_notas = 0
media_escolar = 7

for i in range(1, quantidade_notas + 1):
    nota = float(input(f"Digite a nota {i}:"))
    soma_notas += nota

media = soma_notas / quantidade_notas
print("Nome Do Aluno: ", str(aluno))
print('Serie: ', str(serie))
print('Matricula do Aluno: ', str(matricula))
print('Professor: ', str(professor))
print(f"A media das notas é: {media:.2f}.")

if media >= media_escolar:
    print('Aluno Aprovado')
else: 
    print('Aluno Reprovado')
    
