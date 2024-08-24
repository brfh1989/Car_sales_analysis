import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Anuncios de Coches')

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # Si la casilla de verificación está seleccionada
    st.write('Creación de un histograma para la columna odómetro')
    fig_histogram = px.histogram(car_data, x="odometer", title='Histograma del Odómetro')
    st.plotly_chart(fig_histogram, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # Si la casilla de verificación está seleccionada
    st.write('Creación de un gráfico de dispersión entre precio y odómetro')
    fig_scatter = px.scatter(car_data, x="price", y="odometer", color="condition",
                             title='Gráfico de Dispersión: Precio vs. Odómetro')
    st.plotly_chart(fig_scatter, use_container_width=True)
