import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.sidebar.header("Filtros")

# Elementos de textos
st.title("isso e um :blue[titulo] :sunglasses:")
st.header("isso e um cabeçalho ", divider="gray")
st.subheader("isso e um subcabeçalho", divider=True)
st.text("isso e um texto")

#elementos de dados:
df = pd.DataFrame(np.random.randn(50,20), columns=["col %d" %i for i in range(20)])
st.dataframe(df)

#elementos de seleção
#checkbox
selecao1 = st.checkbox("Selecione")

if  selecao1:
    st.write("Marcado")
else:
    st.write("Não marcado")

st.write("**Novo texto**")

#cor
cor = st.color_picker("Escolha uma cor", "#00f900")
st.write("A cor escolhida foi: ", cor)

#multselect 
opcoes = st.multiselect("Escolha uma ou mais opções", ["Green", "Yellow", "Red", "Blue"])
st.write("Você escolheu: ", opcoes)

#radio
genero = st.radio("Escolha seu tipo de Filme", ["Comedia", "Drama", "Ação"])
st.write("Você escolheu: ",genero)

#selectbox
opcoes = st.selectbox("Qual ao seu melhor contato? ", ["Email", "Telefone", "Whatsapp"])
st.write("Você Selecionou: ", opcoes)

#slider
start_color , end_color = st.select_slider(
    "Selecione o range de cores", 
    options = [
        "Red", 
        "Green", 
        "Blue",
        "Gray",
        "Black",
        "indigo"],
    value = ("Red", "Blue")
)

#toogle
on = st.toggle("Ligar")
if on:
    st.write("Ligado")
else:
    st.write("Desligado")