#python3 version
import rsa
def cifrando(msgCif):

    arqnomepub = r"C:\Users\Noite\Desktop\Backend-Etl\socket\tcp2way\danyPub.txt"

    ##abro o arquivo com a chave
    arq = open(arqnomepub,'rb')
    ##carrego a chave
    txt = arq.read()
    arq.close()

    #decodifico para o formato expoente e modulo
    pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')

    #cifro a msg
    msgc = rsa.encrypt(msgCif,pub)


    return msgc
