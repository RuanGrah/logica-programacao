print("Problema: A Lampada nao Funciona")
passo1 = input('Checar ou não: ')

if passo1 == "nao,não,Nao,Não,n,nn,ñ,Ñ":
    print("A Lampada Continua quebrada")
else:
    print("Pergunta: A Lampada esta plugada?")
    resposta2 = input("Digite Sua Resposta: ")

    if resposta2 == "Não,Nao,nao,ñ,Ñ,n,N": 
        print("Plugar a Lampada")
    else:
        print('Pergunta: O bulbo queimou?')
        resposta3 = input("Digite Sua Respota: ")
        if resposta3 == "Sim,sim,ss,s,S":
            print("Trocar Bulbo")
        else:
            print("Comprar Nova Lampada")
