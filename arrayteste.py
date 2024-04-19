alunos = []

for i in range(3):
    nome = input("Nome: ")
    idade = input("Idade: ")
    nota = input("Nota: ")

    aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(aluno)
    print("                                    ")
    print("------------------------------------")
    print("                                    ")

for aluno in alunos:
    print(f"Nome: {aluno["nome"]}, Idade: {aluno["idade"]}, Nota: {aluno["nota"]}\n")