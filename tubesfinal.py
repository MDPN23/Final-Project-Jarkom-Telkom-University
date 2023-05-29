from socket import *
import sys

serverPort = 5500
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    print("siap untuk terhubung....")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]
        if filename == "/":
            filename = "/index.html"  # default page
        f = open("public" + filename, "r")
        outputdata = f.read()

        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + outputdata
        connectionSocket.send(response.encode())

        f.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
    finally:
        connectionSocket.close()
    serverSocket.close()
    sys.exit()
