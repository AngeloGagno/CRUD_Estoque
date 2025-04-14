# Imagem base com Python 3.12
FROM python:3.12-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH"

# Instala dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instala poetry via pip
RUN pip install --upgrade pip \
 && pip install poetry

# Diretório de trabalho
WORKDIR /app

# Copia arquivos de dependência do frontend
COPY pyproject.toml poetry.lock* /app/

# Instala as dependências do projeto, incluindo o Streamlit
RUN poetry install --no-root

# Copia o restante do código do frontend
COPY . /app/

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando de inicialização
CMD ["poetry", "run", "streamlit", "run", "Como_usar.py", "--server.port=8501", "--server.address=0.0.0.0"]
