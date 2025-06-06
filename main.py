
import streamlit as st
from casos import (
    viga_balcao_concentrada,
    viga_biapoiada_concentrada,
    viga_biapoiada_distribuida,
    viga_engastada_triangulo
)

st.set_page_config(page_title="Diagramas NVM", layout="centered")
st.title("Gerador de Diagramas NVM")

cenario = st.selectbox("Escolha o cenário:", [
    "1 - Viga em balanço com carga concentrada",
    "2 - Viga biapoiada com carga concentrada no meio",
    "3 - Viga biapoiada com carga distribuída uniforme",
    "4 - Viga engastada com carga triangular crescente"
])

L = st.number_input("Comprimento da viga (m)", min_value=0.1, value=10.0, step=0.1)

if "1" in cenario:
    P = st.number_input("Valor da carga concentrada P (N)", value=100.0, step=10.0)
    if st.button("Gerar Diagramas"):
        viga_balcao_concentrada.resolver_viga_balcao(L, P)

elif "2" in cenario:
    P = st.number_input("Valor da carga concentrada P (N)", value=100.0, step=10.0)
    if st.button("Gerar Diagramas"):
        viga_biapoiada_concentrada.resolver_viga_biapoiada(L, P)

elif "3" in cenario:
    q = st.number_input("Intensidade da carga distribuída q (N/m)", value=20.0, step=1.0)
    if st.button("Gerar Diagramas"):
        viga_biapoiada_distribuida.resolver_viga_biapoiada_distribuida(L, q)

elif "4" in cenario:
    q0 = st.number_input("Valor máximo da carga triangular q₀ (N/m)", value=30.0, step=1.0)
    if st.button("Gerar Diagramas"):
        viga_engastada_triangulo.resolver_viga_engastada_triangulo(L, q0)
