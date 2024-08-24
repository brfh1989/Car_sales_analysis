import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de Anuncios de Coches')

# Botón para histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión entre precio y odómetro')
    fig = px.scatter(car_data, x="price", y="odometer", color="condition")
    st.plotly_chart(fig, use_container_width=True)
