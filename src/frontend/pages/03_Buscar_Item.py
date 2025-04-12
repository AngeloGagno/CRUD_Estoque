import streamlit as st
import requests 
from utils import GenericClass


class SelectItem(GenericClass):
    def __init__(self):
        super().__init__()
        self.run()

    def get_data(self, item_id: int):
        try:
            response = requests.get(f"http://fastapi-app:8000/Estoque/{item_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            st.error(f"🚫 Erro HTTP: {e}")
        except requests.exceptions.RequestException as e:
            st.error(f"🔌 Erro de conexão com o backend: {e}")
        except Exception as e:
            st.error(f"❗ Erro inesperado: {e}")
        return None

    def run(self):
        self.header(" Visualizar Item no Estoque")
        self.divider()
        st.markdown("Preencha o código do item abaixo para consultar os dados do produto.")
        
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                codigo = self.text_box("Digite o Código do Produto")
            with col2:
                buscar = self.button("🔍 Buscar")

        if buscar:
            if not codigo.isdigit():
                st.warning("⚠️ Por favor, insira apenas números.")
                return

            item_data = self.get_data(int(codigo))
            if item_data is None:
                return  # Erro já tratado

            if isinstance(item_data, dict) and item_data.get("detail") == "Item não encontrado":
                st.error("❌ Item não encontrado no estoque.")
            else:
                st.success("✅ Item encontrado com sucesso!")
                st.markdown("### Detalhes do Produto:")
                st.json(item_data)

SelectItem()
