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

