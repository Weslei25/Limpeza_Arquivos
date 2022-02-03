import logging
import os


if not os.path.isdir("logs"):
    os.mkdir("logs")



caminho_log = r"./logs\\ARQUIVO-ERROR-DeletarArquivos-IMS.log"
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
logging.basicConfig(filename=caminho_log,
                    filemode='w',
                    level=logging.INFO,
                    format=log_format,
                    encoding='UTF-8')
