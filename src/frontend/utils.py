import streamlit as st

class GenericClass:
    '''Classe com métodos uteis e compartilhados pelas páginas'''
    def __init__(self):
        st.set_page_config('Inicio',layout="wide",page_icon='📦')

    def header(self,text):
        return st.markdown(f"# {text}")
    
    def divider(self):
        return st.divider()
    
    def markdown(self,box_text:str):
        return st.markdown(box_text)

    def text_box(self,box_text:str):
        return st.text_input(label=box_text)
    
    def number_box(self,box_text:str):
        return st.number_input(label=box_text,step=1)
    
    def float_box(self, box_text:str):
        return st.number_input(label=box_text,step=0.1)
    
    def button(self,button_text:str):
        return st.button(label=button_text)
    
    def dataframe(self,data):
        return st.dataframe(data)