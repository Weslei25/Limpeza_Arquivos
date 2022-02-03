from config import *
import time

def parar_servico(servicos=list):
    for servico in servicos:
        os.system('NET STOP {}'.format(servico))
        logging.info("Parando serviço {}".format(servico))
        time.sleep(0.5)
        logging.info("Serviço parado {}".format(servico))


def iniciar_servico(servicos=list):
    logging.info("Finalizando a exclusão dos arquivos")
    logging.info('Subindo Serviços novamente...')
    for servico in servicos:
        os.system('NET START {}'.format(servico))
        logging.info("Iniciando serviço {}".format(servico))
        time.sleep(0.5)
        logging.info("Serviço Iniciado {}".format(servico))