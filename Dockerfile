# Usar imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo de requisitos (opcional)
COPY requirements.txt .

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o código do KeepAlive para o contêiner
COPY keepalive.py .

# Comando para rodar o KeepAlive
CMD ["python", "keepalive.py"]
