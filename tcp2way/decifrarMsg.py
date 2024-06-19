#python3 version
import rsa

def decifra(msgc):

    arqnomepri = r"C:\Users\Noite\Desktop\Backend-Etl\criptografia\py3\chavesAssimetricaschaveLeoPri.txt"

    ##abro o arquivo com a chave
    arq = open(arqnomepri,'rb')
    ##carrego a chave
    txt = arq.read()
    arq.close()

    #decodifico para o formato expoente e modulo
    pri = rsa.PrivateKey.load_pkcs1(txt, format='PEM')

    #decifro a msg
    msg = rsa.decrypt(msgc,pri)

    return msg.decode('utf-8')

