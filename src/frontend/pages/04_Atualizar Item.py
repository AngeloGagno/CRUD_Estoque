from utils import GenericClass
import streamlit as st


import streamlit as st
import requests
from utils import GenericClass  # ajuste o nome do arquivo conforme necessário

class AtualizarItemPage(GenericClass):
    def __init__(self):
        super().__init__()
        self.run()
    def run(self):
        self.header(" Atualizar Item")
        self.divider()

        item_id = self.text_box("Informe o ID do item que deseja atualizar")

        if item_id:
            try:
                response = requests.get(f"http://fastapi-app:8000/Estoque/{item_id}")
                if response.status_code == 200:
                    item = response.json()

                    with st.form("update_form"):
                        nome_produto = self.text_box("Nome do Produto")
                        quantidade = self.number_box("Quantidade")
                        marca = self.text_box("Marca")
                        valor = self.float_box("Valor")

                        # Preenche valores padrão se ainda estiverem em branco
                        if not nome_produto: nome_produto = item.get("nome_produto", "")
                        if not quantidade: quantidade = item.get("quantidade", 0)
                        if not marca: marca = item.get("marca", "")
                        if not valor: valor = item.get("valor", 0.0)

                        submitted = st.form_submit_button("Atualizar")
                        if submitted:
                            updated_item = {
                                "nome_produto": nome_produto,
                                "quantidade": quantidade,
                                "marca": marca,
                                "valor": valor
                            }
                            put_response = requests.put(f"http://fastapi-app:8000/Estoque/{item_id}", json=updated_item)

                            if put_response.status_code == 200:
                                st.success("✅ Item atualizado com sucesso!")
                            else:
                                st.error(f"❌ Erro ao atualizar: {put_response.status_code} - {put_response.text}")
                else:
                    st.warning("⚠️ Item não encontrado. Verifique o ID.")
            except Exception as e:
                st.error(f"❌ Erro ao buscar dados: {e}")

AtualizarItemPage()