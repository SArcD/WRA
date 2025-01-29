import streamlit as st
import pandas as pd

st.title("Carga de Archivo Excel en Streamlit Cloud")

# Cargar el archivo desde la interfaz de usuario
archivo_excel = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if archivo_excel is not None:
    try:
        # Leer el archivo Excel en un DataFrame
        df = pd.read_excel(archivo_excel)
        st.success("Archivo cargado exitosamente")
        
        # Mostrar el DataFrame en la aplicación
        st.write("Vista previa de los datos:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Se produjo un error al cargar el archivo: {e}")
else:
    st.warning("Por favor, sube un archivo Excel para continuar.")

