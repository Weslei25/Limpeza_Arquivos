import time
import schedule
from config import *
from datetime import date
from functions.delete import delete_arquivos
from functions.controle_servico import iniciar_servico, parar_servico
        

def job():
    if __name__ == "__main__":
        logging.info("Iniciando varredura de pastas")
        try:
            data_atual = date.today()
            data_atual = data_atual.strftime('%d')

            if data_atual == dia_de_excluir_arquivos:
                parar_servico()
                for caminho_arq in caminhos.values():                    
                    delete_arquivos(caminho=caminho_arq)
                    time.sleep(0.1)
                iniciar_servico()
            else:
                logging.warning("Hoje não é a data para exluir os arquivos - {} O dia para exclusão é {}".format(data_atual, dia_de_excluir_arquivos))
        except Exception as error:
            logging.exception(error)


#schedule.every().day.at("08:00").do(verificacao_diaria)
schedule.every(0.1).minutes.do(job)
    
while True:
    schedule.run_pending()
    time.sleep(1)
    