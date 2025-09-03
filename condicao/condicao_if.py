nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 65:
    print(nome, "Você tem" , idade, "anos, você é Prioridade.")
else:
    print(nome, "Você tem ", idade, "anos, você não é Prioridade.")
print("Fim")
