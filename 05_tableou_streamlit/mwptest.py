import streamlit as st
import pandas as pd

# Configurando la página y estilos personalizados

st.set_page_config(page_title="My workcation path", page_icon=":world_map:", layout="wide")

custom_css = """
<style>
body {
    background-image: url('landscape_back3.png');
    background-size: cover;
        }

/* Add other custom CSS rules */
.stTextInput, .stNumberInput, .stTextArea, .stSelectbox, .stMultiSelect {
    color: black !important;
    font-size: 24px !important;
        }

/* Personalizar el título */
.title {
    color: blue;
    font-family: 'Helvetica', sans-serif;
    font-size: 72px;
    font-weight: 700;
    margin-bottom: 0px;
        }
/* st.container */
.css-2trqyj {
    background-color: #f0f2f6;
    border: 2px solid #4e2a84;
    border-radius: 20px;
}
/* st.write o Markdown */
.css-2trqyj p {
    color: #333333;
    font-family: 'Garamond', serif;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
import streamlit as st


redish_black = '#8B0000'

# Añadiendo un logo y el título en la parte superior de la página
col1, col2 = st.columns((1, 4))
with col1:
    st.image("landscape_back2.png", width=100)  # Asegúrate de tener el archivo de imagen en el directorio correcto
with col2:
    st.markdown('<p class="title">My workcation path: Un viaje a tu medida</p>', unsafe_allow_html=True)

# Ajustando el ancho de las columnas: 35% para la izquierda, 65% para la derecha
left_column, right_space = st.columns((3.29, 6.71))

with left_column:
    # Esta es la barra de selección de las rutas
    route = st.selectbox(
        "Elige tu ruta de interés",
        ["Ruta 1", "Ruta 2", "Ruta 3", "Ruta 4"],
        key="selector_ruta"
    )

# Utilizando st.container() para gestionar los espacios del contenido principal
with right_space:
    with st.container():
        # Espacio para el mapa
        st.write("Aquí va el mapa")  # Implementa tu lógica de visualización del mapa aquí
    with st.container():
        # Espacio para la información del dataset
        st.write("Información de la ruta seleccionada")  # Implementa tu lógica para mostrar el dataset aquí