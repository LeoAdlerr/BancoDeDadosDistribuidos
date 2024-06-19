#Cliente TCP
import socket
from threading import Thread
from decifrarMsg import decifra
from cifrarMsg import cifrando

global tcp_con

def receber():
    global tcp_con
    while True:
        msgd = tcp_con.recv(2048)
        msg = decifra(msgd)
        print ("Server:",msg)

def enviar():
    global tcp_con
    print ('Para sair use CTRL+X\n')
    msg = cifrando(input().encode())

    while msg != '\x18':
        tcp_con.send(msg)
        msg = cifrando(input().encode())

    tcp_con.close()

# Endereco IP do Servidor
# 192.168.5.239 
SERVER = '192.168.5.239'

# Porta que o Servidor esta escutando
PORT = 5002

tcp_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp_con.connect(dest)


t_rec = Thread(target=receber, args=())
t_rec.start()

t_env = Thread(target=enviar, args=())
t_env.start()
