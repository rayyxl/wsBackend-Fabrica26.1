# 1. Utiliza a versão do Python compatível com a sua (3.12)
FROM python:3.12-slim

# 2. Configurações para evitar arquivos temporários e permitir logs em tempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Define o diretório de trabalho dentro do container
WORKDIR /app

# 4. Instala dependências do sistema necessárias para o SQLite e compilação
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copia o seu arquivo requirements.txt e instala as dependências
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia todo o conteúdo da pasta wsbackend para o container
COPY . /app/

# 7. Executa as migrações do banco de dados SQLite3 automaticamente
RUN python manage.py migrate

# 8. Expõe a porta 8000 (padrão do Django)
EXPOSE 8000

# 9. Inicia o servidor do projeto wsbackend
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]