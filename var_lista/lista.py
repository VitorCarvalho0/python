inventario = []
res = "S"

while res == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: R$")))
    inventario.append(int(input("Número serial: ")))
    inventario.append(input("Departamento: "))
    res = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print(elemento)
