import os
import time
from config import *


def delete_arquivos(caminho=str):
    try:
        time.sleep(0.5)
        arquivos = os.listdir(caminho)# listo os arquivos do diretorio e jogo em uma lista python ['arquvivos']
        logging.info("Obtendo arquivos do path {}".format(caminho))
        
        if not arquivos:
            return

        for arquivo in arquivos:  # Dentro de um laço for pego cada arquivo da lista
            arquivo_momento = r'{}\\{}'.format(caminho,arquivo)
            os.remove(arquivo_momento)# Vamos remover todos os arquvivos do diretorio apos a copia e envio
            logging.info("Arquivo excluido {}".format(arquivo))
            print("Arquivo excluido {}".format(arquivo))
            time.sleep(0.1)

    except FileNotFoundError as erro:
        logging.exception(erro)
    except Exception as erro:
        logging.exception(erro)
        
