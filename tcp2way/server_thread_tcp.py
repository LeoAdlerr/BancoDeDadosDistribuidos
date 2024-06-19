#Servidor TCP
import socket
from threading import Thread
from decifrarMsg import decifra
from cifrarMsg import cifrando

global tcp_con

def enviar():
    global tcp_con
    msg = cifrando(input().encode())
    while True:
        tcp_con.send(msg)
        msg = cifrando(input().encode())

# Endereco IP do Servidor
HOST = '192.168.5.245'

# Porta que o Servidor vai escutar
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)


while True:
    tcp_con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    t_env = Thread(target=enviar, args=())
    t_env.start()
    while True:
        msg = tcp_con.recv(2048)
        if not msg: break
        print("Cliente:", decifra(msg))
    print ('Finalizando conexao do cliente', cliente)
    tcp_con.close()
