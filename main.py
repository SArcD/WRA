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
        st.write("Ahora renombraremos las columnas")

        # Diccionario completo con las claves cortas y las descripciones largas
        preguntas = {
            "P1": "En caso de pertenecer a Oficinas Centrales Indica en cual de las siguientes áreas colaboras.",
            "P2_1": "El espacio donde trabajo me permite realizar mis actividades de manera segura e higiénica",
            "P2_2": "Mi trabajo me exige hacer mucho esfuerzo físico",
            "P2_3": "Me preocupa sufrir un accidente en mi trabajo",
            "P2_4": "Considero que en mi trabajo se aplican las normas de seguridad y salud en el trabajo",
            "P2_5": "Considero que las actividades que realizo son peligrosas",
            "P3_1": "Por la cantidad de trabajo que tengo debo quedarme tiempo adicional a mi turno",
            "P3_2": "Por la cantidad de trabajo que tengo debo trabajar sin parar",
            "P3_3": "Considero que es necesario mantener un ritmo de trabajo acelerado",
            "P4_1": "Mi trabajo exige que esté muy concentrado",
            "P4_2": "Mi trabajo requiere que memorice mucha información",
            "P4_3": "En mi trabajo tengo que tomar decisiones difíciles muy rápido",
            "P4_4": "Mi trabajo exige que atienda varios asuntos al mismo tiempo",
            "P5_1": "En mi trabajo soy responsable de cosas de mucho valor",
            "P5_2": "Respondo ante mi jefe por los resultados de toda mi área de trabajo",
            "P5_3": "En el trabajo me dan órdenes contradictorias",
            "P5_4": "Considero que en mi trabajo me piden hacer cosas innecesarias",
            "P6_1": "Trabajo horas extras más de tres veces a la semana",
            "P6_2": "Mi trabajo me exige laborar en días de descanso, festivos o fines de semana",
            "P6_3": "Considero que el tiempo en el trabajo es mucho y perjudica mis actividades familiares o personales",
            "P6_4": "Debo atender asuntos de trabajo cuando estoy en casa",
            "P6_5": "Pienso en las actividades familiares o personales cuando estoy en mi trabajo",
            "P6_6": "Pienso que mis responsabilidades familiares afectan mi trabajo",
            "P7_1": "Mi trabajo permite que desarrolle nuevas habilidades",
            "P7_2": "En mi trabajo puedo aspirar a un mejor puesto",
            "P7_3": "Durante mi jornada de trabajo puedo tomar pausas cuando las necesito",
            "P7_4": "Puedo decidir cuánto trabajo realizo durante la jornada laboral",
            "P7_5": "Puedo decidir la velocidad a la que realizo mis actividades en mi trabajo",
            "P7_6": "Puedo cambiar el orden de las actividades que realizo en mi trabajo",
            "P8_1": "Los cambios que se presentan en mi trabajo dificultan mi labor",
            "P8_2": "Cuando se presentan cambios en mi trabajo se tienen en cuenta mis ideas o aportaciones",
            "P9_1": "Me informan con claridad cuáles son mis funciones",
            "P9_2": "Me explican claramente los resultados que debo obtener en mi trabajo",
            "P9_3": "Me explican claramente los objetivos de mi trabajo",
            "P9_4": "Me informan con quién puedo resolver problemas o asuntos de trabajo",
            "P9_5": "Me permiten asistir a capacitaciones relacionadas con mi trabajo",
            "P9_6": "Recibo capacitación útil para hacer mi trabajo",
            "P10_1": "Mi jefe ayuda a organizar mejor el trabajo",
            "P10_2": "Mi jefe tiene en cuenta mis puntos de vista y opiniones",
            "P10_3": "Mi jefe me comunica a tiempo la información relacionada con el trabajo",
            "P10_4": "La orientación que me da mi jefe me ayuda a realizar mejor mi trabajo",
            "P10_5": "Mi jefe ayuda a solucionar los problemas que se presentan en el trabajo",
            "P11_1": "Puedo confiar en mis compañeros de trabajo",
            "P11_2": "Entre compañeros solucionamos los problemas de trabajo de forma respetuosa",
            "P11_3": "En mi trabajo me hacen sentir parte del grupo",
            "P11_4": "Cuando tenemos que realizar trabajo de equipo los compañeros colaboran",
            "P11_5": "Mis compañeros de trabajo me ayudan cuando tengo dificultades",
            "P12_1": "Me informan sobre lo que hago bien en mi trabajo",
            "P12_2": "La forma como evalúan mi trabajo en mi centro de trabajo me ayuda a mejorar mi desempeño",
            "P12_3": "En mi centro de trabajo me pagan a tiempo mi salario",
            "P12_4": "El pago que recibo es el que merezco por el trabajo que realizo",
            "P12_5": "Si obtengo los resultados esperados en mi trabajo me recompensan o reconocen",
            "P12_6": "Las personas que hacen bien el trabajo pueden crecer laboralmente",
            "P12_7": "Considero que mi trabajo es estable",
            "P12_8": "En mi trabajo existe continua rotación de personal",
            "P12_9": "Siento orgullo de laborar en este centro de trabajo",
            "P12_10": "Me siento comprometido con mi trabajo",
            "P13_1": "En mi trabajo puedo expresarme libremente sin interrupciones",
            "P13_2": "Recibo críticas constantes a mi persona y/o trabajo",
            "P13_3": "Recibo burlas, calumnias, difamaciones, humillaciones o ridiculizaciones",
            "P13_4": "Se ignora mi presencia o se me excluye de las reuniones de trabajo y en la toma de decisiones",
            "P13_5": "Se manipulan las situaciones de trabajo para hacerme parecer un mal trabajador",
            "P13_6": "Se ignoran mis éxitos laborales y se atribuyen a otros trabajadores",
            "P13_7": "Me bloquean o impiden las oportunidades que tengo para obtener ascenso o mejora en mi trabajo",
            "P13_8": "He presenciado actos de violencia en mi centro de trabajo",
            "P14": "En mi trabajo debo brindar servicio a clientes o usuarios:",
            "P15_1": "Atiendo clientes o usuarios muy enojados",
            "P15_2": "Mi trabajo me exige atender personas muy necesitadas de ayuda o enfermas",
            "P15_3": "Para hacer mi trabajo debo demostrar sentimientos distintos a los míos",
            "P15_4": "Mi trabajo me exige atender situaciones de violencia",
            "P16": "Soy jefe de otros trabajadores:",
            "P17_1": "Comunican tarde los asuntos de trabajo",
            "P17_2": "Dificultan el logro de los resultados del trabajo",
            "P17_3": "Cooperan poco cuando se necesita",
            "P17_4": "Ignoran las sugerencias para mejorar su trabajo"
                }
        # Invertir el diccionario para mapear nombres largos a claves cortas
        nombres_invertidos = {v: k for k, v in preguntas.items()}

        # Función para renombrar las columnas
        def renombrar_columnas(col):
            # Conservar columnas específicas
            if col in ["Marca temporal", "Selecciona tu centro de trabajo"]:
                return col
            # Eliminar corchetes y mapear a clave corta si está en el diccionario
            col_limpia = col.strip(" []")
            return nombres_invertidos.get(col_limpia, col)

        # Aplicar el renombrado a las columnas de `df`
        df.columns = [renombrar_columnas(col) for col in df.columns]
        import pandas as pd

        # Reemplazar "Marca temporal" por una columna "Folio"
        df["Folio"] = [f"part-{i+1}" for i in range(len(df))]
    
        # Reorganizar las columnas para que "Folio" esté al inicio
        columnas_ordenadas = ["Folio"] + [col for col in df.columns if col != "Folio"]
        df = df[columnas_ordenadas]
        import pandas as pd


        # Cambiar los nombres de las columnas específicas
        df.rename(columns={
            "Selecciona tu centro de trabajo": "CT",
            "En caso de pertenecer a Oficinas Centrales Indica en cual de las siguientes áreas colaboras.": "Area"
        }, inplace=True)

        # Reorganizar las columnas para que "Folio" esté al inicio
        columnas_ordenadas = ["Folio"] + [col for col in df.columns if col != "Folio" and col != "Marca temporal"]
        df = df[columnas_ordenadas]

        
        st.dataframe(df)

        st.title("Filtrar Datos por CT en Streamlit")


        # Crear un menú desplegable con los valores únicos de "CT"
        valores_ct = df["CT"].unique()
        valor_seleccionado = st.selectbox("Selecciona un valor de CT:", valores_ct)

        # Filtrar el DataFrame según la selección
        nuevo_df = df[df["CT"] == valor_seleccionado]

        st.success(f"Mostrando datos filtrados para CT = {valor_seleccionado}")
        st.dataframe(nuevo_df)

        # Permitir descargar el DataFrame filtrado
        @st.cache_data
        def convertir_csv(df):
            return df.to_csv(index=False).encode("utf-8")

        archivo_csv = convertir_csv(nuevo_df)

        st.download_button(
            label="Descargar datos filtrados (CSV)",
            data=archivo_csv,
            file_name=f"datos_CT_{valor_seleccionado}.csv",
            mime="text/csv")
        

















    
    except Exception as e:
        st.error(f"Se produjo un error al cargar el archivo: {e}")
else:
    st.warning("Por favor, sube un archivo Excel para continuar.")

