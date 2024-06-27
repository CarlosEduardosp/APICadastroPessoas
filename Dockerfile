# Use a imagem oficial do Python
FROM python:3.12.4

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos da aplicação para o contêiner
COPY . .

# Expõe a porta em que a aplicação estará escutando
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]


