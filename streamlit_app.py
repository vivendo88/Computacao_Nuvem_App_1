import streamlit as st

# Cria 1 coluna (row1 é uma lista com 1 elemento)
row1 = st.columns(1)
row2= st.columns(3)

# Usa a primeira coluna para exibir a imagem
with row1[0]:
    st.image(
        "rede.jpg",
        caption="Monitoramente de Rede",
        alt="Rede na palma da mão",
        use_container_width=True,
    )

with row1[3]:
    st.image(
        "rede.jpg",
        caption="Monitoramente de Rede",
        alt="Rede na palma da mão",
        use_container_width=True,
    )
with row2[0]:
    st.image(
        "obs.png",
        caption="Imagem 1",
        alt="Obserbabilidade",
        use_container_width=True,
    )
with row2[1]:
    st.image(
        "mr.png",
        caption="Imagem 2",
        alt="Monitoramento da Rede",
        use_container_width=True,
    )
with row2[2]:
    st.image(
        "vr.png",
        caption="Imagem 3",
        alt="Visão de Relatorio",
        use_container_width=True,
    )