import socket

HOST = '127.0.0.1'
PORT = 3333

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

print('Aguardando a conexão com o cliente...')

conexao, endereco = sock.accept()
print('Conectando em:', endereco)

while True:
    data = conexao.recv(1024)
    if not data:
        print('Encerrando a conexão')
        conexao.close()
        break
    
    conexao.sendall(data)