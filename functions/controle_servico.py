from config import *
import time

def parar_servico():
    print('Parando Serviços...')
    for servico in servicos:
        os.system('NET STOP {}'.format(servico))
        print("Parando serviço {}".format(servico))
        logging.info("Parando serviço {}".format(servico))
        time.sleep(0.5)
        logging.info("Serviço parado {}".format(servico))


def iniciar_servico():
    logging.info("Finalizando a exclusão dos arquivos")
    print('Subindo Serviços novamente...')
    print('Iniciando Serviços...')
    for servico in servicos:
        os.system('NET START {}'.format(servico))
        print("Iniciando serviço {}".format(servico))
        logging.info("Parando serviço {}".format(servico))
        time.sleep(0.5)
        logging.info("Serviço parado {}".format(servico))