# Sistema de Estoque - Documentação

## Visão Geral

Este projeto implementa um sistema completo de gerenciamento de estoque com operações CRUD (Create, Read, Update, Delete). A aplicação é dividida em duas partes principais:

1. **Backend**: API RESTful desenvolvida com FastAPI
2. **Frontend**: Interface de usuário construída com Streamlit

O sistema é containerizado com Docker para facilitar o deployment e garantir consistência entre ambientes.

## Estrutura do Projeto

```
src/ 
├── frontend/
│   ├── Dockerfile
│   ├── Como_usar.py
│   ├── utils.py
│   └── pages/
│       ├── 01_Criar_Item.py
│       ├── 02_Visualizar_Itens.py
│       ├── 03_Buscar_Item.py
│       ├── 04_Atualizar_Item.py
│       └── 05_Deletar_Item.py
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── utils.py
│   ├── API/
│   │   ├── crud.py
│   │   └── router.py
│   ├── data_contract/
│   │   └── schemas.py
│   └── database/
│       ├── database_conf.py
│       └── models.py
└── docker-compose.yml
```

## Backend (FastAPI)

### Modelos de Dados

O sistema utiliza SQLAlchemy como ORM para interagir com o banco de dados.

```python
class Estoque(Base):
    __tablename__ = 'Estoque'
    id_produto: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome_produto: Mapped[str] = mapped_column(String())
    quantidade: Mapped[int] = mapped_column(Integer())
    marca: Mapped[str] = mapped_column(String())
    valor: Mapped[float] = mapped_column(Float())
```

### Schemas (Validação de Dados)

Os schemas são definidos usando Pydantic para validar os dados antes de serem processados:

```python
class EstoqueBase(BaseModel):
    nome_produto: str
    quantidade: PositiveInt
    marca: str
    valor: PositiveFloat

class EstoqueCreate(EstoqueBase):
    pass

class EstoqueResponse(EstoqueBase):
    id_produto: int

class EstoqueUpdate(EstoqueBase):
    nome_produto: Optional[str] = None
    quantidade: Optional[PositiveInt] = None
    marca: Optional[str] = None
    valor: Optional[PositiveFloat] = None

class EstoqueDelete(EstoqueBase):
    id_produto: int
```

### API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /Estoque/ | Retorna todos os itens do estoque |
| GET | /Estoque/{item_id} | Retorna um item específico pelo ID |
| POST | /Estoque/ | Cria um novo item no estoque |
| PUT | /Estoque/{item_id} | Atualiza um item existente |
| DELETE | /Estoque/{item_id} | Remove um item do estoque |

### Configuração do Banco de Dados

A aplicação usa a classe `Config` para gerenciar a conexão com o banco de dados:

```python
class Config:
    def __init__(self):
        self.engine = create_engine(Utils.db_url())

    def _start_session(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def engine_creator(self):
        return self.engine
    
    def get_db(self):
        SessionLocal = self._start_session()
        db = SessionLocal() 
        try:
            yield db
        finally:
            db.close()
```

A URL do banco de dados é definida em um arquivo `.env` e acessada através da classe `Utils`.

## Frontend (Streamlit)

### Páginas Principais

1. **Home (Como_Usar.py)**: Página inicial com instruções de uso do sistema
2. **Criar Item**: Interface para cadastrar novos produtos
3. **Visualizar Itens**: Lista todos os produtos do estoque
4. **Buscar Item**: Procura um produto específico pelo ID
5. **Atualizar Item**: Interface para editar dados de um produto existente
6. **Deletar Item**: Interface para remover produtos do estoque

### Classe Genérica

A classe `GenericClass` implementa métodos comuns utilizados em todas as páginas do frontend:

```python
class GenericClass:
    '''Classe com métodos uteis e compartilhados pelas páginas'''
    def __init__(self):
        st.set_page_config('Inicio', layout="wide", page_icon='📦')

    def header(self, text):
        return st.markdown(f"# {text}")
    
    def divider(self):
        return st.divider()
    
    # Outros métodos...
```

## Containerização com Docker

### Backend Dockerfile

```dockerfile
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
```

### Frontend Dockerfile

```dockerfile
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH"

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root

COPY . /app/

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "Como_usar.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Docker Compose

```yaml
version: "3.9"

services:
  fastapi-app:
    build:
      context: ./src/backend
      dockerfile: Dockerfile
    container_name: fastapi_app
    ports:
      - "8000:8000"
    env_file:
      - ./src/backend/.env
    volumes:
      - ./src/backend/API:/app/API
      - ./src/backend/database:/app/database
      - ./src/backend/data_contract:/app/data_contract
      - ./src/backend/utils.py:/app/utils.py

  streamlit-frontend:
    build:
      context: ./src/frontend
      dockerfile: Dockerfile
    container_name: streamlit_frontend
    ports:
      - "8501:8501"
    volumes:
      - ./src/frontend:/app
    depends_on:
      - fastapi-app
```

## Ambiente de Desenvolvimento

O projeto foi desenvolvido usando Python 3.12 e gerenciado com Poetry para controle de dependências.

### Dependências principais do Backend:
- FastAPI
- SQLAlchemy
- Uvicorn
- Pydantic
- Python-dotenv

### Dependências principais do Frontend:
- Streamlit
- Requests
- Pandas

## Como Usar

1. Clone o repositório
2. Configure o arquivo `.env` na pasta backend com suas credenciais de banco de dados
3. Execute `docker-compose up --build` na raiz do projeto
4. Acesse o frontend em `http://localhost:8501`
5. Acesse a documentação da API em `http://localhost:8000/docs`

## Operações CRUD

### Criar um Item
- Vá até a página "Criar Item"
- Preencha os campos necessários
- Clique em "Salvar"

### Visualizar Itens
- Vá até a página "Visualizar Itens" para ver todos os produtos
- Ou vá até "Buscar Item" para encontrar um produto específico por ID

### Atualizar um Item
- Vá até a página "Atualizar Item"
- Informe o ID do produto
- Modifique os campos desejados
- Clique em "Atualizar"

### Deletar um Item
- Vá até a página "Deletar Item"
- Informe o ID do produto
- Confirme a exclusão

