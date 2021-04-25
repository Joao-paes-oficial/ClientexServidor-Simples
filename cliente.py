import socket

HOST = '127.0.0.1'
PORT = 3333

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(str.encode('Olá, servidor!'))
data = sock.recv(1024)

print('Mensagem ecoada:', data.decode())