nome = input("Digite um funcionario: ")
empresa = input("Digite a instituição: ")
qtde_funcionario = int(input("Digite a qtde de funcionario: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " Trabalha da empresa " + empresa)
print("Possui: ", qtde_funcionario, "funcionários.")
print("A média da mensalidade é de: R$" + str(mediaMensalidade))

print("======= Verifique os tipos de dados abaixo ======")

print("O tipo de dado da varial [nome]", type(nome))
print("O tipo de dado da varial [empresa] ", type(empresa))
print("O tipo de dado da varial [qtde_funcionarios] ", type(qtde_funcionario))
print("O tipo de dado da varial [mediaMensalidade] é: ", type(mediaMensalidade))
