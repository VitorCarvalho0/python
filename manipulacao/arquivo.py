arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Hello World!")

arquivo.close()

## outra forma de fazer

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nOla Mundo!")
