import streamlit as st
import requests
from utils import GenericClass  

class Create_item(GenericClass):
    '''Classe para inserção um novo item no banco de dados.'''
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.header(" Cadastrar Novo Produto")
        self.divider()
        st.markdown("Preencha os campos abaixo para adicionar um novo item ao estoque.")

        with st.form("create_form", clear_on_submit=True):
            product: str = self.text_box(" Nome do Produto")
            quantity: int = self.number_box(" Quantidade")
            label: str = self.text_box(" Marca")
            price: float = self.float_box(" Preço de Compra")

            submitted = st.form_submit_button("💾 Salvar")

            if submitted:
                payload = {
                    "nome_produto": product,
                    "quantidade": quantity,
                    "marca": label,
                    "valor": price
                }

                try:
                    response = requests.post("http://fastapi-app:8000/Estoque", json=payload)
                    if response.status_code == 200:
                        st.success("✅ Produto cadastrado com sucesso!")
                    else:
                        st.error(f"❌ Erro ao cadastrar. Código: {response.status_code}")
                except Exception as e:
                    st.error(f"🚫 Erro ao conectar com o backend: {e}")

Create_item() # Função que executa o código da página
