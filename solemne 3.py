import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("spotify-2023.csv")

# Título de la aplicación
st.title("Explorador de Canciones Spotify 2023")

# Descripción
st.write("Explora las canciones más escuchadas del año 2023.")

# Barra lateral
with st.sidebar:
    st.write("# Opciones")

    # Filtro por artista
    artist_filter = st.sidebar.selectbox(
        "Selecciona un artista", df['artist'].unique()
    )

    # Filtro por género (si tienes una columna 'genre' en tu DataFrame)
    genre_options = df['genre'].unique() if 'genre' in df.columns else []
    genre_filter = st.sidebar.multiselect(
        "Selecciona géneros", genre_options, default=genre_options
    )

# Filtrar el DataFrame
filtered_df = df[df['artist'] == artist_filter]
if 'genre' in df.columns:
    filtered_df = filtered_df[filtered_df['genre'].isin(genre_filter)]

# Mostrar la tabla filtrada (opcional)
if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(filtered_df)

# Visualizaciones
st.subheader("Visualizaciones")

# Gráfico de barras de popularidad
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(filtered_df['track_name'], filtered_df['popularity'])
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.set_xlabel("Canción")
ax.set_ylabel("Popularidad")
ax.set_title("Popularidad de las canciones")
st.pyplot(fig)