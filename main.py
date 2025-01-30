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
        #st.dataframe(nuevo_df)

        # Función para verificar si una celda contiene una combinación inválida o es NaN
        def es_valor_invalido(valor):
            #if pd.isna(valor):  # Verifica si es NaN
            #    return True
            if isinstance(valor, str):
                # Verifica si contiene una coma o un espacio adicional después de una coma
                if "," in valor:
                    return True
                # Verifica si contiene caracteres invisibles como saltos de línea
                #if "\n" in valor or "\r" in valor:
                #    return True
            return False

        # Identificar filas con valores inválidos
        filas_invalidas = nuevo_df.map(es_valor_invalido).any(axis=1)

        # Crear un nuevo DataFrame excluyendo las filas con valores inválidos
        nuevo_df = nuevo_df[~filas_invalidas].copy()

        # Mostrar el resultado
        print("DataFrame limpio:")
        st.dataframe(nuevo_df)

        # Opciones para P14
        opciones_p14 = {"Sí": "Si", "No": "No"}
        valor_p14 = st.radio("Indique si en su trabajo debe brindar servicio a clientes o usuarios:", list(opciones_p14.keys()))

        # Filtrar por la opción de P14
        valor_seleccionado = opciones_p14[valor_p14]
        nuevo_df2 = nuevo_df[nuevo_df["P14"] == valor_seleccionado].copy()

        # Si selecciona "No", asignar 0 a las columnas P15
        if valor_seleccionado == "No":
            columnas_p15 = ['P15_1', 'P15_2', 'P15_3', 'P15_4']
            for col in columnas_p15:
                if col in nuevo_df2.columns:
                    nuevo_df2[col] = 0

        st.success(f"Mostrando datos filtrados para P14 = {valor_seleccionado}")
        st.dataframe(nuevo_df2)
        #########

        # Opciones para P16 (Ser jefe de otros trabajadores)
        opciones_p16 = {"Sí": "Si", "No": "No"}
        valor_p16 = st.radio("¿En su trabajo es jefe de otros trabajadores?", list(opciones_p16.keys()))

        # Filtrar por la opción seleccionada en P16
        valor_seleccionado_p16 = opciones_p16[valor_p16]
        nuevo_df3 = nuevo_df2[nuevo_df2["P16"] == valor_seleccionado_p16].copy()

        # Si selecciona "No" en P16, asignar 0 a las columnas P17
        if valor_seleccionado_p16 == "No":
            columnas_p17 = ['P17_1', 'P17_2', 'P17_3', 'P17_4']
            for col in columnas_p17:
                if col in nuevo_df3.columns:
                    nuevo_df3[col] = 0

        st.success(f"Mostrando datos filtrados para P16 = {valor_seleccionado_p16}")
        st.dataframe(nuevo_df3)
        #############

        import streamlit as st
        import pandas as pd
    
        # Definición de escalas Likert y preguntas
        escala_likert_positiva = {"Siempre": 4, "Casi siempre": 3, "Algunas Veces": 2, "Casi nunca": 1, "Nunca": 0}
        escala_likert_negativa = {"Siempre": 0, "Casi siempre": 1, "Algunas Veces": 2, "Casi nunca": 3, "Nunca": 4}

        preguntas_likert_positiva = [
            "P2_1", "P2_4", "P7_1", "P7_2", "P7_3", "P7_4", "P7_5", "P7_6",
            "P8_2", "P9_1", "P9_2", "P9_3", "P9_4", "P9_5", "P9_6",
            "P10_1", "P10_2", "P10_3", "P10_4", "P10_5",
            "P11_1", "P11_2", "P11_3", "P11_4", "P11_5",
            "P12_1", "P12_2", "P12_3", "P12_4", "P12_5", "P12_6", "P12_7", "P12_8",
            "P12_9", "P12_10", "P13_1"
        ]

        preguntas_likert_negativa = [
            "P2_2", "P2_3", "P2_5", "P3_1", "P3_2", "P3_3",
            "P4_1", "P4_2", "P4_3", "P4_4", "P5_1", "P5_2", "P5_3", "P5_4",
            "P6_1", "P6_2", "P6_3", "P6_4", "P6_5", "P6_6", "P8_1",
            "P13_2", "P13_3", "P13_4", "P13_5", "P13_6", "P13_7", "P13_8",
            "P15_1", "P15_2", "P15_3", "P15_4",
            "P17_1", "P17_2", "P17_3", "P17_4"
        ]

        # Función para transformar respuestas a escala Likert numérica
        def transformar_respuestas_likert(df):
            for columna in df.columns:
                if columna.startswith("P15") or columna.startswith("P17"):
                    # Dejar intactas las filas con valor 0
                    df[columna] = df[columna].apply(
                        lambda x: 0 if x == 0 else (
                            escala_likert_positiva.get(x) if columna in preguntas_likert_positiva else
                            escala_likert_negativa.get(x, 0)
                        )
                    )
                elif columna in preguntas_likert_positiva:
                    df[columna] = df[columna].map(escala_likert_positiva).fillna(0)
                elif columna in preguntas_likert_negativa:
                    df[columna] = df[columna].map(escala_likert_negativa).fillna(0)
            return df

        # Función para calcular niveles de riesgo
        def calcular_niveles_riesgo_persona(respuestas):
            niveles_generales = {
                "Nulo o despreciable": lambda c: c < 50,
                "Bajo": lambda c: 50 <= c < 75,
                "Medio": lambda c: 75 <= c < 99,
                "Alto": lambda c: 99 <= c < 140,
                "Muy alto": lambda c: c >= 140
            }
            puntaje_total = sum(respuestas.values())
            nivel_general = next(
                (nivel for nivel, condicion in niveles_generales.items() if condicion(puntaje_total)),
                "No determinado"
            )
            return puntaje_total, nivel_general

        # Transformar las respuestas y calcular puntajes
        def procesar_dataframe(df):
            # Seleccionar columnas relevantes para transformar
            columnas_preguntas = preguntas_likert_positiva + preguntas_likert_negativa
            df_respuestas = df[columnas_preguntas].copy()

            # Transformar respuestas a escala Likert
            df_respuestas = transformar_respuestas_likert(df_respuestas)

            # Calcular puntajes y niveles de riesgo
            calificaciones = []
            for _, row in df_respuestas.iterrows():
                respuestas = row.to_dict()
                puntaje_total, nivel_general = calcular_niveles_riesgo_persona(respuestas)
                calificaciones.append({
                    "Calificación Total": puntaje_total,
                    "Nivel de Riesgo": nivel_general
                })

            # Convertir calificaciones a DataFrame
            df_calificaciones = pd.DataFrame(calificaciones)

            # Concatenar resultados con el DataFrame original
            df_resultados = pd.concat([df.reset_index(drop=True), df_calificaciones], axis=1)
            return df_resultados

        # Aplicar procesamiento y mostrar en Streamlit
        if 'nuevo_df3' in locals():
            nuevo_df3_resultado = procesar_dataframe(nuevo_df3)

            st.success("Cálculo de Nivel de Riesgo Completado")
            st.dataframe(nuevo_df3_resultado)

        ####################3

        import streamlit as st

        # Crear una copia del DataFrame original
        nuevo_df3_resultado_num = nuevo_df3_resultado.copy()

        # Transformar columnas de preguntas Likert a formato numérico
        for col in nuevo_df3_resultado.columns:
            if col in preguntas_likert_positiva:
                nuevo_df3_resultado_num[col] = nuevo_df3_resultado[col].map(escala_likert_positiva).fillna(0)
            elif col in preguntas_likert_negativa:
                nuevo_df3_resultado_num[col] = nuevo_df3_resultado[col].map(escala_likert_negativa).fillna(0)

        # Mantener las columnas no numéricas si existen en el DataFrame
        columnas_no_numericas = ["Folio", "CT", "P1"]
        columnas_existentes = [col for col in columnas_no_numericas if col in nuevo_df3_resultado.columns]
        nuevo_df3_resultado_num[columnas_existentes] = nuevo_df3_resultado[columnas_existentes]

        st.success("Transformación de respuestas Likert a formato numérico completada")
        st.dataframe(nuevo_df3_resultado_num)

        #############
        import streamlit as st
        import pandas as pd
    
        # Función para generar DataFrames separados
        def generar_dataframes_separados(df):
            # Seleccionar las columnas de la escala positiva y negativa junto con las columnas clave
            columnas_clave = ["Folio", "CT"]
            columnas_positivas = columnas_clave + preguntas_likert_positiva
            columnas_negativas = columnas_clave + preguntas_likert_negativa

            # Crear DataFrame para la escala positiva
            df_positivos = df[columnas_positivas].copy()
            for col in preguntas_likert_positiva:
                df_positivos[col] = pd.to_numeric(df_positivos[col], errors="coerce").fillna(0)  # Convertir a numérico y manejar valores faltantes
            df_positivos["Suma Positiva"] = df_positivos[preguntas_likert_positiva].sum(axis=1)
            df_positivos["Calificación Total"] = pd.to_numeric(df["Calificación Total"], errors="coerce").fillna(0)
            df_positivos["Nivel de Riesgo"] = df["Nivel de Riesgo"]

            # Crear DataFrame para la escala negativa
            df_negativos = df[columnas_negativas].copy()
            for col in preguntas_likert_negativa:
                df_negativos[col] = pd.to_numeric(df_negativos[col], errors="coerce").fillna(0)  # Convertir a numérico y manejar valores faltantes
            df_negativos["Suma Negativa"] = df_negativos[preguntas_likert_negativa].sum(axis=1)
            df_negativos["Calificación Total"] = pd.to_numeric(df["Calificación Total"], errors="coerce").fillna(0)
            df_negativos["Nivel de Riesgo"] = df["Nivel de Riesgo"]

            return df_positivos, df_negativos

        # Generar los DataFrames separados    
        nuevo_df3_resultados_positivos, nuevo_df3_resultados_negativos = generar_dataframes_separados(nuevo_df3_resultado_num)

        # Interfaz en Streamlit para seleccionar la visualización
        st.title("Visualización de Escalas Likert Positiva y Negativa")

        opcion_visualizacion = st.radio(
            "Selecciona el tipo de escala Likert a visualizar:",
            ("Escala Positiva", "Escala Negativa")
        )

        if opcion_visualizacion == "Escala Positiva":
            st.success("Mostrando DataFrame con preguntas de Escala Likert Positiva")
            st.dataframe(nuevo_df3_resultados_positivos)

            # Permitir descarga del DataFrame de escala positiva
            archivo_csv_positivos = nuevo_df3_resultados_positivos.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Descargar datos de Escala Positiva (CSV)",
                data=archivo_csv_positivos,
                file_name="datos_escala_positiva.csv",
                mime="text/csv"
            )

        else:
            st.warning("Mostrando DataFrame con preguntas de Escala Likert Negativa")
            st.dataframe(nuevo_df3_resultados_negativos)

            # Permitir descarga del DataFrame de escala negativa
            archivo_csv_negativos = nuevo_df3_resultados_negativos.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Descargar datos de Escala Negativa (CSV)",
                data=archivo_csv_negativos,
                file_name="datos_escala_negativa.csv",
                mime="text/csv"
            )


        ###############

        import streamlit as st
        import matplotlib.pyplot as plt

        st.title("Distribución de Niveles de Riesgo")

        # Contar los valores únicos en la columna "Nivel de Riesgo"
        nivel_riesgo_counts = nuevo_df3_resultado["Nivel de Riesgo"].value_counts()

        # Crear un gráfico de pastel
        fig, ax = plt.subplots(figsize=(8, 8))
        nivel_riesgo_counts.plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            cmap='tab20',
            legend=False,
            title='Distribución por Nivel de Riesgo',
            ax=ax
        )
        ax.set_ylabel('')  # Eliminar el texto del eje y
        plt.tight_layout()

        # Mostrar la gráfica en Streamlit
        st.pyplot(fig)

        ##########

        # Diccionario de dominios reales y las preguntas que los conforman
        dominios_reales = {
            "Condiciones en el ambiente de trabajo": ["P2_1", "P2_2", "P2_3", "P2_4", "P2_5"],
            "Carga de trabajo": ["P3_1", "P3_2", "P3_3", "P4_1", "P4_2", "P4_3", "P4_4",
                         "P15_1", "P15_2", "P15_3", "P15_4", "P5_1", "P5_2", "P5_3", "P5_4"],
            "Falta de control sobre el trabajo": ["P7_1", "P7_2", "P7_3", "P7_4", "P7_5",
                                          "P7_6", "P8_1", "P8_2", "P9_5", "P9_6"],
            "Jornada de trabajo": ["P6_1", "P6_2"],
            "Interferencia en la relación trabajo-familia": ["P6_3", "P6_4", "P6_5", "P6_6"],
            "Liderazgo": ["P9_1", "P9_2", "P9_3", "P9_4", "P10_1", "P10_2", "P10_3", "P10_4", "P10_5"],
            "Relaciones en el trabajo": ["P11_1", "P11_2", "P11_3", "P11_4", "P11_5",
                                 "P17_1", "P17_2", "P17_3", "P17_4"],
            "Violencia": ["P13_1", "P13_2", "P13_3", "P13_4", "P13_5", "P13_6", "P13_7", "P13_8"],
            "Reconocimiento del desempeño": ["P12_1", "P12_2", "P12_3", "P12_4", "P12_5", "P12_6"],
            "Insuficiente sentido de pertenencia e inestabilidad": ["P12_7", "P12_8", "P12_9", "P12_10"]
        }

        # Puntos de corte de niveles por dominio
        niveles_dominio_cortes = {
            "Condiciones en el ambiente de trabajo": {
                "Nulo o despreciable": lambda c: c < 3,
                "Bajo": lambda c: 3 <= c < 5,
                "Medio": lambda c: 5 <= c < 7,
                "Alto": lambda c: 7 <= c < 9,
                "Muy alto": lambda c: c >= 9
            },
            "Carga de trabajo": {
                "Nulo o despreciable": lambda c: c < 12,
                "Bajo": lambda c: 12 <= c < 16,
                "Medio": lambda c: 16 <= c < 20,
                "Alto": lambda c: 20 <= c < 24,
                "Muy alto": lambda c: c >= 24
            },
            "Falta de control sobre el trabajo": {
                "Nulo o despreciable": lambda c: c < 5,
                "Bajo": lambda c: 5 <= c < 8,
                "Medio": lambda c: 8 <= c < 11,
                "Alto": lambda c: 11 <= c < 14,
                "Muy alto": lambda c: c >= 14
            },
            "Jornada de trabajo": {
                "Nulo o despreciable": lambda c: c < 1,
                "Bajo": lambda c: 1 <= c < 2,
                "Medio": lambda c: 2 <= c < 4,
                "Alto": lambda c: 4 <= c < 6,
                "Muy alto": lambda c: c >= 6
            },
            "Interferencia en la relación trabajo-familia": {
                "Nulo o despreciable": lambda c: c < 1,
                "Bajo": lambda c: 1 <= c < 2,
                "Medio": lambda c: 2 <= c < 4,
                "Alto": lambda c: 4 <= c < 6,
                "Muy alto": lambda c: c >= 6
            },
            "Liderazgo": {
                "Nulo o despreciable": lambda c: c < 3,
                "Bajo": lambda c: 3 <= c < 5,
                "Medio": lambda c: 5 <= c < 8,
                "Alto": lambda c: 8 <= c < 11,
                "Muy alto": lambda c: c >= 11
            },
            "Relaciones en el trabajo": {
                "Nulo o despreciable": lambda c: c < 10,
                "Bajo": lambda c: 10 <= c < 13,
                "Medio": lambda c: 13 <= c < 17,
                "Alto": lambda c: 17 <= c < 21,
                "Muy alto": lambda c: c >= 21
            },
            "Violencia": {
                "Nulo o despreciable": lambda c: c < 7,
                "Bajo": lambda c: 7 <= c < 10,
                "Medio": lambda c: 10 <= c < 13,
                "Alto": lambda c: 13 <= c < 16,
                "Muy alto": lambda c: c >= 16
            },
            "Reconocimiento del desempeño": {
                "Nulo o despreciable": lambda c: c < 5,
                "Bajo": lambda c: 5 <= c < 8,
                "Medio": lambda c: 8 <= c < 11,
                "Alto": lambda c: 11 <= c < 14,
                "Muy alto": lambda c: c >= 14
            },
            "Insuficiente sentido de pertenencia e inestabilidad": {
                "Nulo o despreciable": lambda c: c < 7,
                "Bajo": lambda c: 7 <= c < 10,
                "Medio": lambda c: 10 <= c < 13,
                "Alto": lambda c: 13 <= c < 16,
                "Muy alto": lambda c: c >= 16
            }
        }



        
        
        st.title("Cálculo de Puntajes y Niveles de Riesgo por Dominio")

        # Crear un nuevo DataFrame con las columnas deseadas
        dominio_puntajes_niveles = []

        # Calcular puntajes y niveles de riesgo por dominio
        nuevo_df3_result_num = nuevo_df3_resultado_num.copy()

        for dominio, preguntas in dominios_reales.items():
            # Calcular el puntaje total por dominio
            nuevo_df3_result_num[dominio + "_Puntaje"] = nuevo_df3_result_num[preguntas].sum(axis=1)

            # Calcular el nivel de riesgo por dominio
            nuevo_df3_result_num[dominio + "_Nivel de Riesgo"] = nuevo_df3_result_num[dominio + "_Puntaje"].apply(
                lambda puntaje: next(
                    (nivel for nivel, condicion in niveles_dominio_cortes[dominio].items() if condicion(puntaje)),
                    "No determinado"
                )
            )

        # Seleccionar columnas relevantes para el nuevo DataFrame
        columnas_finales = ["Folio", "Calificación Total", "Nivel de Riesgo"] + [
            col for dominio in dominios_reales.keys() for col in [dominio + "_Puntaje", dominio + "_Nivel de Riesgo"]
        ]

        # Crear el nuevo DataFrame con los resultados por dominio
        nuevo_df3_resultado_dominios = nuevo_df3_result_num[columnas_finales]

        # Mostrar el DataFrame en Streamlit
        st.success("Cálculo de puntajes y niveles de riesgo por dominio completado")
        st.dataframe(nuevo_df3_resultado_dominios)

        # Permitir descarga del DataFrame con los datos por dominio
        @st.cache_data    
        def convertir_csv(df):
            return df.to_csv(index=False).encode("utf-8")

        archivo_csv_dominios = convertir_csv(nuevo_df3_resultado_dominios)

        st.download_button(
            label="Descargar datos de Puntajes y Niveles de Riesgo por Dominio (CSV)",
            data=archivo_csv_dominios,
            file_name="datos_puntajes_niveles_dominios.csv",
            mime="text/csv"
        )

        ###################

        st.title("Búsqueda de Empleado por Folio o CT")

        # Ingresar el número de Folio o CT para buscar
        criterio_busqueda = st.radio("Buscar empleado por:", ("Folio", "CT"))
        valor_busqueda = st.text_input(f"Ingrese el {criterio_busqueda} del empleado:")

        # Filtrar el DataFrame según la búsqueda
        if valor_busqueda:
            df_filtrado = nuevo_df3_resultado_dominios[nuevo_df3_resultado_dominios[criterio_busqueda].astype(str) == valor_busqueda]

            if not df_filtrado.empty:
                st.success(f"Empleado encontrado con {criterio_busqueda} = {valor_busqueda}")
                st.dataframe(df_filtrado)
            else:
                st.warning(f"No se encontró ningún empleado con {criterio_busqueda} = {valor_busqueda}")


        ########################

        import streamlit as st
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        # Mapeo de niveles de riesgo a valores numéricos
        nivel_riesgo_valores = {
            "Nulo o despreciable": 0,
            "Bajo": 1,
            "Medio": 2,
            "Alto": 3,
            "Muy alto": 4
        }

        st.title("Búsqueda de Empleado y Evaluación de Riesgo en Diagrama de Radar")

        # Ingresar el número de Folio o CT para buscar
        criterio_busqueda = st.radio("Buscar empleado por:", ("Folio", "CT"))
        valor_busqueda = st.text_input(f"Ingrese el {criterio_busqueda} del empleado:")

        if valor_busqueda:
            df_filtrado = nuevo_df3_resultado_dominios[nuevo_df3_resultado_dominios[criterio_busqueda].astype(str) == valor_busqueda]

            if not df_filtrado.empty:
                st.success(f"Empleado encontrado con {criterio_busqueda} = {valor_busqueda}")
                st.dataframe(df_filtrado)

                # Extraer los valores de nivel de riesgo por dominio y convertirlos a valores numéricos
                niveles_riesgo = []
                dominios = list(dominios_reales.keys())

                for dominio in dominios:
                    nivel_str = df_filtrado[f"{dominio}_Nivel de Riesgo"].values[0]
                    niveles_riesgo.append(nivel_riesgo_valores.get(nivel_str, 0))

                # Crear el gráfico de radar
                num_vars = len(dominios)

                # Ángulos de cada eje en el gráfico de radar
                angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
                niveles_riesgo += niveles_riesgo[:1]  # Cerrar el gráfico
                angles += angles[:1]

                # Crear la figura del radar
                fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
                ax.fill(angles, niveles_riesgo, color='red', alpha=0.25)
                ax.plot(angles, niveles_riesgo, color='red', linewidth=2)

                # Configurar los ejes
                ax.set_yticks(range(5))  # Rango de 0 a 4 (correspondiente a los niveles de riesgo)
                ax.set_yticklabels(["Nulo", "Bajo", "Medio", "Alto", "Muy Alto"], fontsize=10)
                ax.set_xticks(angles[:-1])
                ax.set_xticklabels(dominios, fontsize=10, rotation=45, ha="right")

                st.pyplot(fig)

            else:
                st.warning(f"No se encontró ningún empleado con {criterio_busqueda} = {valor_busqueda}")

        
        

        ##########
        
        
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

