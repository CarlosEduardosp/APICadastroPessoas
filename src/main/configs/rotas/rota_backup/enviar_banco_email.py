import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime


def enviar_backup_email():

    # Obter a data e hora atuais
    data_e_hora_atual = datetime.now()

    # Formatar a data e hora como string
    data_e_hora_formatadas = data_e_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

    try:
        caminho_arquivo = "pessoas.db"

        with open(caminho_arquivo, "rb") as arquivo:
            conteudo = arquivo.read()

        corpo_email = "<p>Backup do banco pessoas.db, feito com sqlite para api de icnvararuama.</p>" \
                      f"<p>{data_e_hora_formatadas}.</p>"

        destinatarios = ["carlos.spadilha@yahoo.com.br", "Cadastroicnv@gmail.com"]

        # Crie um objeto MIMEMultipart
        msg = MIMEMultipart()
        msg["Subject"] = "Backup do banco de dados"
        msg["From"] = "tec.mundo.py@gmail.com"
        msg["To"] = ", ".join(destinatarios)

        # Adicione o corpo do e-mail como texto
        msg.attach(MIMEText(corpo_email, "html"))

        # Adicione o arquivo .db como um anexo
        anexo = MIMEApplication(conteudo, _subtype="octet-stream")
        anexo.add_header("Content-Disposition", f"attachment; filename={caminho_arquivo}")
        msg.attach(anexo)

        password = "jakhonuthvdvrkvw"

        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()

        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_bytes())

        return {"Success": True, "Data": {"message": "Backup enviado com sucesso."}}

    except Exception as e:
        return {"Success": False, "Data": {"error_message": str(e)}}

