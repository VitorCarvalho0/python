from funcoes import *

usuario = {}
opcao = pergunta()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuario)
    opcao = pergunta()
