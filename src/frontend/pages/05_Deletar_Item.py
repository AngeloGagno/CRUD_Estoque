import streamlit as st
import requests
from utils import GenericClass  

class DeletarItemPage(GenericClass):
    '''Classe para instanciar a página de Delete de items do banco'''
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.header(" Deletar Item")
        self.divider()

        item_id = self.text_box("Informe o ID do item que deseja deletar")

        if item_id:
            if self.button("🔍 Verificar Item"):
                try:
                    response = requests.get(f"http://fastapi-app:8000/Estoque/{item_id}")
                    if response.status_code == 200:
                        item = response.json()
                        st.success("Item encontrado:")
                        st.json(item)

                        if st.checkbox("Confirmar exclusão do item"):
                            if self.button("❌ Deletar"):
                                delete_response = requests.delete(f"http://fastapi-app:8000/Estoque/{item_id}")
                                if delete_response.status_code == 200:
                                    st.success("✅ Item deletado com sucesso!")
                                else:
                                    st.error(f"❌ Erro ao deletar: {delete_response.status_code} - {delete_response.text}")
                    else:
                        st.warning("⚠️ Item não encontrado. Verifique o ID.")
                except Exception as e:
                    st.error(f"❌ Erro ao buscar dados: {e}")

DeletarItemPage() # Função que executa o código da página