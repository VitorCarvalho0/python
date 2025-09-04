def preencherInventario(lista):
    res = "S"
    while res == "S":
        equip = [input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número serial: ")),
            input("Departamento: ")]
        lista.append(equip)
        res = input("Digite \"S\" para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........:", elemento[0])
        print("valor........:", elemento[1])
        print("Serial.......:", elemento[2])
        print("Departamento.:", elemento[3])
        
def localizarPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("valor........:", elemento[1])
            print("Serial.......:", elemento[2])
            
def depreciarPorNome(lista, porc):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("Novo valor: ", elemento[1])
            
def excluirPorSerial(lista):
    serial = int(input("\nDigite o serial do equipamento que será escluido: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "itens excluidos."

def resmirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custou: ", max(valores))
        print("O equipamento mais barato custou: ", min(valores))
        print("O total de equipamento é de: ", sum(valores))
