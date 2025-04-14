import streamlit as st
from utils import GenericClass
class Home(GenericClass):
    def __init__(self):
        '''Classe geradora da página de explicação de como o sistema funciona.'''
        st.set_page_config('Inicio',layout="centered",page_icon='📦')

    def run(self):
        super().header("Sistema de Estoque")
        super().divider()
        super().markdown(
'''
        ## Instruções de Uso

        ### 📦 Criar um Item
        - Vá até a página **"Criar Item"**
        - Preencha todos os campos obrigatórios
        - Clique em **"Salvar"** para adicionar o item ao estoque

        ---

        ### 🔍 Buscar Itens

        #### 🔹 Buscar Todos os Itens
        - Vá até a página **"Visualizar Itens"**
        - Todos os itens cadastrados serão listados automaticamente

        #### 🔹 Buscar um Item Específico
        - Vá até a página **"Buscar Item"**
        - Informe o **ID do item** e clique em **"Buscar"**
        - Se o item existir, seus dados serão exibidos

        ---

        ### ✏️ Atualizar um Item
        - Vá até a página **"Atualizar Item"**
        - Informe o **ID do item** que deseja atualizar
        - Edite os campos desejados e clique em **"Atualizar"**

        ---

        ### 🗑 Excluir um Item
        - Vá até a página **"Excluir Item"**
        - Informe o **ID do item** e clique em **"Excluir"**
        - O item será removido permanentemente do sistema
        ''')

Home().run() # Função que executa o código da página