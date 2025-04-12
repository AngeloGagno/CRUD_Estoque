FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction

COPY main.py ./
COPY API/ ./API/
COPY data_contract/ ./data_contract
COPY database/ ./database/
COPY utils.py ./
COPY .env ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
