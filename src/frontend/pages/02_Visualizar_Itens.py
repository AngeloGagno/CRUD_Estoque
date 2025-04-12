import streamlit as st
import requests 
from utils import GenericClass

class View(GenericClass):
    def __init__(self):
        super().__init__()
        self.run()

    def get_data(self):
        try:
            response = requests.get('http://fastapi-app:8000/Estoque')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"🔌 Erro ao conectar com o backend: {e}")
        except Exception as e:
            st.error(f"❗ Erro inesperado: {e}")
        return None

    def run(self):
        self.header("📋 Todos os Itens em Estoque")
        self.divider()
        st.markdown("Abaixo estão listados todos os produtos atualmente registrados no sistema:")

        with st.spinner("🔄 Carregando dados..."):
            data = self.get_data()

        if data:
            if isinstance(data, list) and len(data) > 0:
                self.dataframe(data)
                st.success(f"✅ {len(data)} itens carregados com sucesso.")
            else:
                st.warning("⚠️ Nenhum item encontrado no estoque.")
        else:
            st.error("❌ Não foi possível carregar os dados.")

View()
