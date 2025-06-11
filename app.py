import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.title("Análisis de Vehículos Usados en EE.UU.")
st.markdown("Esta aplicación interactiva muestra visualizaciones de los datos de autos usados.")

# Mostrar/ocultar los datos
if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(df)

# Histograma de precios
st.subheader("Distribución de Precios")
fig_hist = px.histogram(df, x='price', nbins=50, title='Distribución de Precios')
st.plotly_chart(fig_hist)

# Gráfico de dispersión: precio vs odómetro
st.subheader("Relación entre Precio y Kilometraje")
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition',
                         title='Precio vs Kilometraje (odometer)')
st.plotly_chart(fig_scatter)
