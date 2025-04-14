# Sistema de Gerenciamento de Estoque

Sistema completo de gerenciamento de estoque com operações CRUD, usando FastAPI para o backend e Streamlit para o frontend.

## Requisitos

- Docker
- Docker Compose

## Início Rápido

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/CRUD_Estoque.git
   cd CRUD_Estoque
   ```

2. Configure o arquivo de ambiente:
   ```
   # Crie um arquivo .env na pasta src/backend com o conteúdo:
   SQLALCHEMY_DATABASE_URL=postgresql://usuario:senha@seu_host:5432/nome_do_banco
   ```

3. Inicie os containers:
   ```
   docker-compose up -d
   ```

4. Acesse a aplicação:
   - Frontend: http://localhost:8501
   - Documentação da API: http://localhost:8000/docs

## Uso Básico

- **Criar Item**: Página para adicionar novos produtos ao estoque
- **Visualizar Itens**: Lista completa dos produtos cadastrados
- **Buscar Item**: Encontre um produto específico pelo ID
- **Atualizar Item**: Edite as informações de um produto existente
- **Deletar Item**: Remova produtos do estoque

## Documentação

Para informações detalhadas sobre instalação, uso e API, consulte a [documentação completa](https://angelogagno.github.io/CrewAI_Constructor/).

## Contato

- GitHub: [Angelo Gagno](https://github.com/AngeloGagno)
- LinkedIn: [Angelo Gagno](https://www.linkedin.com/in/angelogagno)