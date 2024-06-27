from .enviar_banco_email import enviar_backup_email
import schedule
import time
import asyncio


def minha_funcao():
    response = enviar_backup_email()
    print(response)

    return response


#def rodar_agendamento():
    # Agendamento diário às 23h para o envio do banco para o email.
    #schedule.every().day.at("12:20").do(minha_funcao)
    # verifica o tempo a cada segundo determinado no sleep(x).
    #while True:
        #schedule.run_pending()
        #time.sleep(1)
        # 3600 é uma hora
