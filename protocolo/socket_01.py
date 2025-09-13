import socket

resp = "S"

while (resp == "S"):
    url =  input("Digite uma URL: ")
    ip = socket.gethostbyname(url)
    print("O IP referent e a url informada é: ", ip)
    resp = input("Digite < S > para continuar: ").upper()
