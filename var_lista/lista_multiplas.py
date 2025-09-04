equipamento = []
valores = []
seriais = []
departamentos = []
res = "S"

while res == "S":
    equipamento.append(input("Equipamento: "))
    valores.append(float(input("Valor: R$")))
    seriais.append(int(input("Número serial: ")))
    departamentos.append(input("Departamento: "))
    res = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamento)):
    print("\nEquipamento..: ", (indice + 1))
    print("Nome.........: ", equipamento[indice])
    print("Valor.........:", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])
