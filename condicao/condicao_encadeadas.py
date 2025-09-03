nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?" ).upper()

if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário.")
elif doenca_infectocontagiosa == "SIM":
    print("O paciente ", nome, " deve ser direcioando para sala reservada.")
else:
    print("O paciente", nome, "NÂO possi atendimento prioritário.")
