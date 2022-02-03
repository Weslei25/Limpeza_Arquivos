from inspect import Traceback
import logging
import os


if not os.path.isdir("logs"):
    os.mkdir("logs")


caminhos = {
'teste':r'C:\\Project\\Excluir_Arquivos\\functions\\__pycache__',    
'caminho_log_ims': r'C:\\AUTO_FILES_SELLOUT\\ENVIO_FILES_IMS\\Logs',
'caminho_backup_ims':r'C:\\AUTO_FILES_SELLOUT\\ENVIO_FILES_IMS\\BACKUP',
'iniciar_procesos': r'pythonw C:\\AUTO_FILES_SELLOUT\\ENVIO_FILES_IMS\\app.pyw',
'caminho_log_mdlz': r'C:\\ServicoMondelez\ServicoMondelez\\logs',
'caminho_backup_mondelez': r'C:\\AUTO_FILES_SELLOUT\\ENVIO_FILES_IMS\\BACKUP'
}


dia_de_excluir_arquivos = '03'


caminho_log = r"./logs\\ARQUIVO-ERROR-DeletarArquivos-IMS.log"
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
logging.basicConfig(filename=caminho_log,
                    filemode='w',
                    level=logging.INFO,
                    format=log_format,
                    encoding='UTF-8')

servicos = ['EnviosDeArquivosIMS','EnviosDeArquivosMondelez']