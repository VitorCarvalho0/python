inventario = []
res = "S"

while res == "S":
    equip = [input("Equipamento: "),
             float(input("Valor: ")),
             int(input("Número serial: ")),
             input("Departamento: ")]
    inventario.append(equip)
    res = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print("Nome.........:", elemento[0])
    print("valor........:", elemento[1])
    print("Serial.......:", elemento[2])
    print("Departamento.:", elemento[3])

busca = input("\nDigite o nome do equipamento que deseja buscar: ")

for elemento in inventario:
    if busca == elemento[0]:
        print("valor........:", elemento[1])
        print("Serial.......:", elemento[2])

depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

serial = int(input("\nDigite o serial do equipamento que será escluido: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

valores = []

for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro custou: ", max(valores))
    print("O equipamento mais barato custou: ", min(valores))
    print("O total de equipamento é de: ", sum(valores))

