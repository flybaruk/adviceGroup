# Use uma imagem base Python 3.11 slim para reduzir o tamanho
FROM python:3.11-slim

# Evita que o Python gere arquivos .pyc no container e desativa o buffer para logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Define o comando de execução
CMD ["python", "fluxo.py"]