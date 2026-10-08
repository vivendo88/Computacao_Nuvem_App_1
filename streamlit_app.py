import streamlit as st

# --- Linha 1: 1 imagem grande ---
row1 = st.columns(1)

with row1[0]:
    st.image(
        "rede.jpg",
        caption="Monitoramento de Rede",
        alt="Rede na palma da mão",
        width="stretch",
    )

# --- Linha 2: 3 imagens lado a lado ---
row2 = st.columns(3)

with row2[0]:
    st.image(
        "obs.png",
        caption="Imagem 1",
        alt="Observabilidade",
        width="stretch",
    )

with row2[1]:
    st.image(
        "mr.png",
        caption="Imagem 2",
        alt="Monitoramento da Rede",
        width="stretch",
    )

with row2[2]:
    st.image(
        "vr.png",
        caption="Imagem 3",
        alt="Visão de Relatório",
        width="stretch",
    )