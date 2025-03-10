import streamlit as st
import pandas as pd



paginas = st.sidebar.radio("Secciones:",["Descripción","Cargar datos","Depuración","Análisis","Equipo de trabajo"])

st.title("Análisis de datos aplicado al riesgo laboral")

if paginas == "Descripción":
    
    
    st.subheader("""**Objetivo de la Aplicación**""")

    st.markdown("""
    <div class="justificado">

    Esta aplicación tiene como objetivo facilitar la identificación, análisis y prevención de los **factores de riesgo psicosocial** en los centros de trabajo, de acuerdo con los lineamientos establecidos en la **NOM-035-STPS-2018**. A través de la evaluación de respuestas a un cuestionario estandarizado, la aplicación permite:

    - **Automatizar la captura y procesamiento de datos** del cuestionario de evaluación.
    - **Generar reportes individuales y organizacionales** sobre niveles de riesgo psicosocial.
    - **Visualizar mapas de correlación y redes de relaciones** entre factores de riesgo.
    - **Identificar dominios críticos** y sugerir áreas de intervención para mejorar el entorno organizacional.
    - **Comparar clasificaciones y realizar análisis de reducción de preguntas**, facilitando una evaluación más eficiente.

    La herramienta está dirigida a **empresas, organizaciones y profesionales en seguridad laboral**, permitiendo tomar decisiones basadas en datos para la mejora del bienestar de los trabajadores.
    """, unsafe_allow_html=True)

elif paginas == "Cargar datos":

    st.subheader("Carga de arhivos")

    st.markdown("""
    En esta sección puede cargar los datos laborales a analizar. Estos deben tener el formato de la encuesta para la determinación del riesgo laboral.
    """)

    st.markdown("""
    Por favor suba aqui el archivo de **.xlsx** con los datos de la Encuesta para la Determinación de factores de riesgo laborales.
    """)

    # Cargar el archivo desde la interfaz de usuario
    archivo_excel = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

    #if archivo_excel is not None:
    #    try:
            # Leer el archivo Excel en un DataFrame
    df = pd.read_excel(archivo_excel)
    st.session_state['df'] = df
    st.success("Archivo cargado exitosamente")
        
    # Mostrar el DataFrame en la aplicación
    with st.expander("**Vista previa de los datos cargados**"):
        st.markdown("""A continuación se muestra el archivo con los datos cargados a la aplicación. Si da doble click en la columna esta se puede reordenar de manera ascendente o descendente.""")

        st.dataframe(df)
#        st.session_state['df'] = df


    if 'df' in st.session_state:
        df = st.session_state['df']
    st.subheader("**Depuración de datos**")
    st.markdown("""En esta sección se agrega la columna Folio, en la que se le asigna una clave alfanumérica ("part-##") como identificador a cada participante de la encuesta. Además se reemplaza el nombre de la columna "selecciona tu centro de trabajo" por "CT" por brevedad. De igual forma, los enunciados de cada pregunta se reemplazaron por una clave. Cada clave y su pregunta correspondiente se puede consultar en la siguiente tabla:   
    """)
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


    # Definición de escalas Likert y preguntas
    escala_likert_positiva = {"Siempre": 4, "Casi siempre": 3, "Algunas Veces": 2, "Casi nunca": 1, "Nunca": 0}
    escala_likert_negativa = {"Siempre": 0, "Casi siempre": 1, "Algunas Veces": 2, "Casi nunca": 3, "Nunca": 4}
            
    # Escalas Likert
    preguntas_likert_positiva = [
        "P2_1", "P2_4", "P7_1", "P7_2", "P7_3", "P7_4", "P7_5", "P7_6",
        "P8_2", "P9_1", "P9_2", "P9_3", "P9_4", "P9_5", "P9_6",
        "P10_1", "P10_2", "P10_3", "P10_4", "P10_5", "P11_1", "P11_2",
        "P11_3", "P11_4", "P11_5", "P12_1", "P12_2", "P12_3", "P12_4",
        "P12_5", "P12_6", "P12_7", "P12_8", "P12_9", "P12_10", "P13_1"
    ]

    preguntas_likert_negativa = [
        "P2_2", "P2_3", "P2_5", "P3_1", "P3_2", "P3_3", "P4_1", "P4_2",
        "P4_3", "P4_4", "P5_1", "P5_2", "P5_3", "P5_4", "P6_1", "P6_2",
        "P6_3", "P6_4", "P6_5", "P6_6", "P8_1", "P13_2", "P13_3", "P13_4",
        "P13_5", "P13_6", "P13_7", "P13_8", "P15_1", "P15_2", "P15_3",
        "P15_4", "P17_1", "P17_2", "P17_3", "P17_4"
    ]
    # Convertir a un DataFrame
    df_preguntas = pd.DataFrame(list(preguntas.items()), columns=["Clave de Pregunta", "Enunciado"])
    st.markdown("""Listado de preguntas en la encuesta y su clave alfanumérica:""")
    st.dataframe(df_preguntas)


    st.markdown("""Las preguntas están divididas en dos grupos: uno en el que la intensidad de las respuestas va en escala positiva y otro en el que van en escala negativa. A continuación de muestran agrupadas de acuerdo a su escala""")
    # Crear DataFrames para cada tipo de escala Likert
    df_likert_positiva = pd.DataFrame(
    [{"Clave de Pregunta": clave, "Enunciado": preguntas[clave]} for clave in preguntas_likert_positiva],
    columns=["Clave de Pregunta", "Enunciado"]
    )
    
    df_likert_negativa = pd.DataFrame(
    [{"Clave de Pregunta": clave, "Enunciado": preguntas[clave]} for clave in preguntas_likert_negativa],
    columns=["Clave de Pregunta", "Enunciado"]
    )

    # Agregar valores de las escalas Likert
    df_escala_positiva = pd.DataFrame(escala_likert_positiva.items(), columns=["Respuesta", "Valor"])
    df_escala_negativa = pd.DataFrame(escala_likert_negativa.items(), columns=["Respuesta", "Valor"])

            # Mostrar las tablas en Streamlit
            #st.title("Preguntas y Escalas Likert")

    st.markdown("**Preguntas en Escala Likert Positiva**")
    st.dataframe(df_likert_positiva)

    st.markdown("**Preguntas en Escala Likert Negativa**")
    st.dataframe(df_likert_negativa)

    st.markdown("""A continuación se muestran los valores de las escalas likert positiva y negativa:""")

            
    st.markdown("**Valores de Escala Likert Positiva**")
    st.table(df_escala_positiva)

    st.markdown("**Valores de Escala Likert Negativa**")
    st.table(df_escala_negativa)        # Invertir el diccionario para mapear nombres largos a claves cortas
        
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
        
elif paginas == "Depuración":        
    if 'df' in st.session_state:
        df = st.session_state['df']
    import pandas as pd

    # Cambiar los nombres de las columnas específicas
    df.rename(columns={
        "Selecciona tu centro de trabajo": "CT",
        "En caso de pertenecer a Oficinas Centrales Indica en cual de las siguientes áreas colaboras.": "Area"
    }, inplace=True)

    # Reorganizar las columnas para que "Folio" esté al inicio
    columnas_ordenadas = ["Folio"] + [col for col in df.columns if col != "Folio" and col != "Marca temporal"]
    df = df[columnas_ordenadas]


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
    filas_invalidas = df.map(es_valor_invalido).any(axis=1)

    # Crear un nuevo DataFrame excluyendo las filas con valores inválidos
    df = df[~filas_invalidas].copy()
        
    st.markdown("""**Este es el dataframe con el que se realizará el análisis de datos:**""")
        
    st.dataframe(df)
    # Mostrar el número de filas y columnas
    num_filas, num_columnas = df.shape
    st.markdown(f"""**El DataFrame tiene {num_filas} filas y {num_columnas} columnas.**""")

    import pandas as pd
    import streamlit as st
    from io import BytesIO

    # Función para convertir DataFrame a Excel
    def convertir_df_a_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Datos")
        processed_data = output.getvalue()
        return processed_data

    # Convertir DataFrame a archivo Excel
    excel_data = convertir_df_a_excel(df)

    # Botón de descarga
    st.download_button(
        label="📥 Descargar Excel",
        data=excel_data,
        file_name="dataframe.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


    st.subheader("Filtrar datos por Centro de trabajo, atención a clientes y puesto")
    st.markdown("""En esta sección se puede seleccionar el **Centro de trabajo** a analizar. Además es posible analizar por separado las respuestas tanto del personal que brinda **atención a clientes** y/o que está **a cargo de otros empleados**. En el siguiente menú desplegable, busque el centro de trabajo que desea analizar y, debajo de este menu, indique si el tipo de personal brinda atención a clientes y son jefes de otros trabajadores:""")
    # Crear un menú desplegable con los valores únicos de "CT"
    valores_ct = df["CT"].unique()
    valor_seleccionado = st.selectbox("Seleccione el **Centro de trabajo (CT)**:", valores_ct)

    # Filtrar el DataFrame según la selección
    nuevo_df = df[df["CT"] == valor_seleccionado]
    st.session_state['nuevo_df'] = nuevo_df

        #st.success(f"Mostrando datos filtrados para CT = {valor_seleccionado}")
        #st.dataframe(nuevo_df)
    

    # Opciones para P14
    opciones_p14 = {"Sí": "Si", "No": "No"}
    valor_p14 = st.radio("Indique si en su trabajo debe **brindar servicio a clientes o usuarios**:", list(opciones_p14.keys()))

    # Filtrar por la opción de P14
    valor_seleccionado = opciones_p14[valor_p14]
    nuevo_df2 = nuevo_df[nuevo_df["P14"] == valor_seleccionado].copy()

    # Si selecciona "No", asignar 0 a las columnas P15
    if valor_seleccionado == "No":
        columnas_p15 = ['P15_1', 'P15_2', 'P15_3', 'P15_4']
        for col in columnas_p15:
            if col in nuevo_df2.columns:
                nuevo_df2[col] = 0

        #st.success(f"Mostrando datos filtrados para P14 = {valor_seleccionado}")
        #st.dataframe(nuevo_df2)
        #########

        # Opciones para P16 (Ser jefe de otros trabajadores)
    opciones_p16 = {"Sí": "Si", "No": "No"}
    valor_p16 = st.radio("¿En su trabajo es **jefe de otros trabajadores**?", list(opciones_p16.keys()))

    # Filtrar por la opción seleccionada en P16
    valor_seleccionado_p16 = opciones_p16[valor_p16]
    nuevo_df3 = nuevo_df2[nuevo_df2["P16"] == valor_seleccionado_p16].copy()

    # Si selecciona "No" en P16, asignar 0 a las columnas P17
    if valor_seleccionado_p16 == "No":
        columnas_p17 = ['P17_1', 'P17_2', 'P17_3', 'P17_4']
        for col in columnas_p17:
            if col in nuevo_df3.columns:
                nuevo_df3[col] = 0

        #st.success(f"Mostrando datos filtrados para P16 = {valor_seleccionado_p16}")
        #st.dataframe(nuevo_df3)
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

            #st.success("Cálculo de Nivel de Riesgo Completado")
            #st.dataframe(nuevo_df3_resultado)
    st.session_state['nuevo_df3_resultado'] = nuevo_df3_resultado
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

    #st.success("Transformación de respuestas Likert a formato numérico completada")

    with st.expander("Sobre el riesgo laboral segun la NOM-035-STPS-2018"):
        st.markdown("""
        La **Norma Oficial Mexicana NOM-035-STPS-2018** establece los lineamientos para la identificación, análisis y prevención de factores de riesgo psicosocial en los centros de trabajo en México.

        ### Definición:
        El **nivel de riesgo laboral** se refiere a la **exposición de los trabajadores a factores de riesgo psicosocial**, tales como condiciones inseguras en el ambiente de trabajo, cargas excesivas de trabajo, falta de control sobre las tareas, liderazgo negativo, jornadas prolongadas, violencia laboral, entre otros.

        ### Cálculo del Nivel de Riesgo:
        Para determinar el nivel de riesgo psicosocial en un centro de trabajo, la NOM-035 establece la aplicación de cuestionarios específicos que evalúan distintos factores de riesgo. Con base en la puntuación obtenida, se clasifican los niveles de riesgo en:

        - **Nulo o despreciable:** No requiere intervención.
        - **Bajo:** Se recomienda mantener las medidas de control.
        - **Medio:** Se requieren intervenciones preventivas.
        - **Alto:** Se deben adoptar medidas correctivas y de intervención.
        - **Muy alto:** Se requiere una acción inmediata y un análisis profundo de las condiciones laborales.

        La norma también señala que los centros de trabajo con más de 50 trabajadores deben realizar **evaluaciones periódicas** para detectar y mitigar los factores de riesgo psicosocial.

        Fuente: *Norma Oficial Mexicana NOM-035-STPS-2018, Factores de riesgo psicosocial en el trabajo - Identificación, análisis y prevención*.
        """)
        
    st.markdown("""A Continuación se muestra el **dataframe filtrado** con las respuestas cambiadas a una escala numérica:""")
    st.dataframe(nuevo_df3_resultado_num)

    # Convertir DataFrame a archivo Excel
    excel_data_2 = convertir_df_a_excel(nuevo_df3_resultado_num)

    # Botón de descarga
    st.download_button(
        label="📥 Descarga Dataframe filtrado",
        data=excel_data_2,
        file_name="dataframe_filtrado.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
        
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
    with st.expander("Visualización de Escalas Likert Positiva y Negativa"):
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

        #st.subheader("Distribución de Niveles de Riesgo")

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


    st.markdown("""
    A continuación se evalua el nivel de riesgo en cada dominio definido por la NOM-035-STPS-2018
    """)
        
    with st.expander("Dominios del Cuestionario de Nivel de Riesgo según la NOM-035-STPS-2018"):
        st.markdown("""
        La **NOM-035-STPS-2018** evalúa el nivel de riesgo psicosocial en los centros de trabajo a través de los siguientes **dominios**:
        
        1. **Condiciones en el ambiente de trabajo**  
           Evaluación de condiciones físicas y ambientales del lugar de trabajo.

        2. **Carga de trabajo**  
           Análisis de cantidad, complejidad y tiempo disponible para realizar tareas.

        3. **Falta de control sobre el trabajo**  
           Medición de autonomía, participación y posibilidad de desarrollo.

        4. **Jornada de trabajo**  
           Evaluación del impacto de la duración y los cambios en los horarios laborales.

        5. **Interferencia en la relación trabajo-familia**  
           Análisis de cómo las exigencias laborales afectan la vida personal.

        6. **Liderazgo**  
           Relación entre superiores y subordinados, claridad en las funciones y reconocimiento.

        7. **Relaciones en el trabajo**  
           Evaluación de la convivencia laboral y existencia de conflictos.

        8. **Violencia laboral**  
           Identificación de acoso, hostigamiento, discriminación y violencia.

        9. **Reconocimiento del desempeño**  
           Nivel de valoración y reconocimiento de los esfuerzos laborales.

        10. **Insuficiente sentido de pertenencia e inestabilidad**  
           Análisis de la identificación del trabajador con la empresa y percepción de estabilidad.

        Cada uno de estos dominios permite identificar factores de riesgo psicosocial y diseñar estrategias para su prevención.

        **Fuente:** *Norma Oficial Mexicana NOM-035-STPS-2018*.
        """)


        
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
    st.session_state['nuevo_df3_resultado_dominios'] = nuevo_df3_resultado_dominios
    st.session_state['dominios_reales'] = dominios_reales


    # Mostrar el DataFrame en Streamlit
    #st.success("Cálculo de puntajes y niveles de riesgo por dominio completado")
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


elif paginas == "Análisis":
       
    if 'nuevo_df' in st.session_state:
        nuevo_df = st.session_state['nuevo_df']
    if 'nuevo_df3_resultado_dominios' in st.session_state:
        nuevo_df3_resultado_dominios = st.session_state['nuevo_df3_resultado_dominios']
    if 'dominios_reales' in st.session_state:
        dominios_reales = st.session_state['dominios_reales']
    if 'nuevo_df3_resultado' in st.session_state:
        nuevo_df3_resultado = st.session_state['nuevo_df3_resultado']
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

    st.subheader("Visualización del nivel de riesgo")

    st.markdown("""
    A continuación puede visualizar los **diagramas de radar** con los resultados para la evaluación del **nivel de riesgo laboral** de uno o mas participantes de la encuesta. A continuación seleccione si quiere visualizar los datos de un participante en particular (tecleando la clave alfa numérica que lo representa) o de todos aquellos que han sido clasificados con el mismo nivel de riesgo.
    """)
    # Seleccionar tipo de búsqueda
    tipo_busqueda = st.radio("Seleccione el tipo de búsqueda:", ("Por Empleado", "Por Nivel de Riesgo"))

    if tipo_busqueda == "Por Empleado":
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
                ax.set_xticklabels(dominios, fontsize=8, rotation=45, ha="right")

                st.pyplot(fig)

            else:
                st.warning(f"No se encontró ningún empleado con {criterio_busqueda} = {valor_busqueda}")

    elif tipo_busqueda == "Por Nivel de Riesgo":
        # Seleccionar un Nivel de Riesgo
        nivel_seleccionado = st.selectbox("Seleccione el Nivel de Riesgo a visualizar:", list(nivel_riesgo_valores.keys()))

        # Filtrar empleados con el Nivel de Riesgo seleccionado
        df_filtrado = nuevo_df3_resultado_dominios[nuevo_df3_resultado_dominios["Nivel de Riesgo"] == nivel_seleccionado]

        if not df_filtrado.empty:
            st.success(f"Se encontraron {len(df_filtrado)} empleados con Nivel de Riesgo: {nivel_seleccionado}")
            st.dataframe(df_filtrado[["Folio", "Nivel de Riesgo"]])

            # Definir el número de filas y columnas en la cuadrícula de gráficos
            num_empleados = len(df_filtrado)
            num_cols = 3  # Número de columnas por fila
            num_rows = -(-num_empleados // num_cols)  # Redondeo hacia arriba

            # Crear múltiples gráficos de radar en una cuadrícula
            fig, axes = plt.subplots(num_rows, num_cols, figsize=(num_cols * 5, num_rows * 5), subplot_kw=dict(polar=True))
            axes = np.array(axes).flatten()  # Asegurar que se puedan iterar en caso de que haya menos empleados

            for i, (_, empleado) in enumerate(df_filtrado.iterrows()):
                niveles_riesgo = []
                for dominio in dominios_reales.keys():
                    nivel_str = empleado[f"{dominio}_Nivel de Riesgo"]
                    niveles_riesgo.append(nivel_riesgo_valores.get(nivel_str, 0))

                # Ángulos del radar
                angles = np.linspace(0, 2 * np.pi, len(dominios_reales), endpoint=False).tolist()
                niveles_riesgo += niveles_riesgo[:1]  # Cerrar el gráfico
                angles += angles[:1]

                # Crear el gráfico de radar para el empleado
                ax = axes[i]
                ax.fill(angles, niveles_riesgo, color='red', alpha=0.25)
                ax.plot(angles, niveles_riesgo, color='red', linewidth=2)

                # Configurar los ejes
                ax.set_yticks(range(5))
                ax.set_yticklabels(["Nulo", "Bajo", "Medio", "Alto", "Muy Alto"], fontsize=7)
                ax.set_xticks(angles[:-1])
                ax.set_xticklabels(dominios_reales.keys(), fontsize=6, rotation=45, ha="right")
                ax.set_title(f"Empleado {empleado['Folio']}", fontsize=10, pad=10)

            # Ajustar el diseño del gráfico
            plt.tight_layout()
            st.pyplot(fig)

        else:
            st.warning(f"No se encontraron empleados con Nivel de Riesgo: {nivel_seleccionado}")

    with st.expander("**¿Qué es un gráfico de radar y cómo se interpreta?**"):
        st.markdown("""
        Un gráfico de radar, también conocido como gráfico de araña o gráfico polar, es una representación gráfica que permite visualizar datos multivariados en un formato bidimensional. Se utiliza para mostrar valores de diferentes variables en un sistema de coordenadas radiales, donde cada eje representa una variable.

        ### Características principales:
            - **Ejes radiales**: Cada eje radial corresponde a una variable o categoría específica.
            - **Escala común**: Todas las variables se representan en la misma escala, lo que facilita la comparación.
            - **Área sombreada**: El área delimitada por la línea que conecta los puntos representa el "perfil" de los datos.

            ### ¿Cómo interpretarlo?
            - **Forma del gráfico**: La forma del área sombreada indica cómo se distribuyen los valores de las variables. Por ejemplo, un gráfico equilibrado (simétrico) puede indicar uniformidad en las variables, mientras que un gráfico asimétrico resalta diferencias marcadas.
            - **Valores extremos**: Los puntos más alejados del centro representan valores altos, mientras que los más cercanos al centro indican valores bajos.
            - **Comparaciones**: Al superponer varios gráficos de radar, es posible comparar perfiles entre diferentes categorías, grupos o individuos.""")

        
    ####################

    st.subheader("Minimización de items del cuestionario y estudio de corrlaciones entre variables")

    def indiscernibility(attr, table):
        u_ind = {}  # un diccionario vacío para almacenar los elementos de la relación de indiscernibilidad (U/IND({conjunto de atributos}))
        attr_values = []  # una lista vacía para almacenar los valores de los atributos

        for i in table.index:
            attr_values = []
            for j in attr:
                attr_values.append(table.loc[i, j])  # encontrar el valor de la tabla en la fila correspondiente y el atributo deseado y agregarlo a la lista attr_values

            # convertir la lista en una cadena y verificar si ya es una clave en el diccionario
            key = ''.join(str(k) for k in attr_values)

            if key in u_ind:  # si la clave ya existe en el diccionario
                u_ind[key].add(i)
            else:  # si la clave aún no existe en el diccionario
                u_ind[key] = set()
                u_ind[key].add(i)

        # Ordenar la relación de indiscernibilidad por la longitud de cada conjunto
        u_ind_sorted = sorted(u_ind.values(), key=len, reverse=True)
        return u_ind_sorted


        ####################

    from itertools import combinations

    with st.expander("**¿Qué es el reducto de un cuestionario y cómo se calcula?**"):
            st.markdown("""
            ### ¿Qué es el reducto de un cuestionario?
            El reducto de un cuestionario es un conjunto mínimo de preguntas seleccionadas que conservan, de manera eficiente, la capacidad de clasificar o representar la información contenida en el cuestionario original. Es una herramienta útil en análisis de datos, ya que permite simplificar el instrumento manteniendo su representatividad y precisión.

            ### ¿Cómo se calcula el reducto en este código?
            El proceso de cálculo del reducto en el código proporcionado incluye los siguientes pasos:

            1. **Relación de indiscernibilidad (`indiscernibility`)**:
               - Agrupa las respuestas de las filas en conjuntos equivalentes basados en los valores de los atributos (preguntas) seleccionados.
               - Cada conjunto representa una partición de la tabla en base a las similitudes entre los datos.

            2. **Comparación de particiones (`compare_partitions`)**:
               - Compara la partición original (usando todas las preguntas del dominio) con particiones generadas por subconjuntos de preguntas.
               - La métrica de similitud utilizada es el índice de Jaccard, que mide la proporción de intersección entre dos conjuntos en relación con su unión.

            3. **Búsqueda del reducto (`find_reduct_for_domain`)**:
               - Explora todas las combinaciones posibles de preguntas dentro de un dominio.
               - Evalúa qué subconjunto alcanza un nivel de similitud (umbral) cercano o igual a la partición original.
               - Si un subconjunto cumple con el umbral, se considera el reducto para ese dominio.

            4. **Aplicación a dominios específicos**:
               - El cuestionario está dividido en dominios (como "Carga de trabajo" o "Liderazgo"), cada uno con un conjunto de preguntas asociadas.
               - El proceso se aplica individualmente a cada dominio para encontrar su reducto.

            ### Ejemplo práctico:
            Supongamos que un dominio tiene 10 preguntas, pero después del análisis, se identifica que solo 3 preguntas son suficientes para mantener la misma estructura de clasificación que las 10 originales. Estas 3 preguntas forman el reducto del dominio.

            ### ¿Por qué es importante?
            - **Optimización**: Reduce el número de preguntas sin perder la calidad de los datos.
            - **Menor carga cognitiva**: Facilita la administración del cuestionario.
            - **Eficiencia**: Acelera los procesos de análisis al trabajar con menos variables.

            ### Orden en el que se calculan las relaciones de indiscernibilidad:
            - Crea particiones basadas en valores de las preguntas seleccionadas.
            - Evalúa la similitud entre las particiones usando el índice de Jaccard.
            - El umbral (por defecto 0.9 o 90%) define qué tan representativo debe ser el reducto en comparación con el conjunto completo.

            Este enfoque es común en metodologías como la teoría de conjuntos aproximados (Rough Set Theory) y es particularmente útil en contextos donde la reducción de datos es esencial sin comprometer la calidad analítica.
            """)

    # Función para calcular la relación de indiscernibilidad
    @st.cache_data
    def indiscernibility(attr, table):
        u_ind = {}
        for i in table.index:
            attr_values = tuple(table.loc[i, attr])
            if attr_values in u_ind:
                u_ind[attr_values].add(i)
            else:
                u_ind[attr_values] = {i}
        return list(u_ind.values())

    # Función para calcular la similitud entre particiones usando Jaccard
    @st.cache_data
    def compare_partitions(original, test):
        score = 0
        for orig_set in original:
            best_match = 0
            for test_set in test:
                similarity = len(orig_set.intersection(test_set)) / len(orig_set.union(test_set))
                best_match = max(best_match, similarity)
            score += best_match * len(orig_set)
        total_size = sum(len(group) for group in original)
        return score / total_size if total_size > 0 else 0

    st.markdown("""A continuación se muestra el **reducto** para cada uno de los dominios en el cuestionario de **riesgo laboral**""")
        
    @st.cache_data
    # Función para encontrar el reducto para un dominio
    def find_reduct_for_domain(domain_questions, df, threshold=0.9):
        best_match = 0
        best_subset = None
        original_partition = indiscernibility(domain_questions, df)

        for i in range(1, len(domain_questions) + 1):
            for subset in combinations(domain_questions, i):
                test_partition = indiscernibility(list(subset), df)
                match_score = compare_partitions(original_partition, test_partition)
                if match_score > best_match:
                    best_match = match_score
                    best_subset = subset
                if best_match >= threshold:
                    st.write(f"Reducto encontrado para el dominio **{domain}** con umbral {threshold}: {best_subset} (**Coincidencia: {best_match:.2%})**")
                    return list(best_subset)

        st.write(f"No se encontró reducto con umbral {threshold}. Mejor coincidencia: {best_match:.2%}")
        return list(best_subset)

    # Diccionario de dominios y preguntas
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
        "Insuficiente sentido de pertenencia e inestabilidad": ["P12_7", "P12_9", "P12_10", "P12_8"]
    }

    # Aplicar el proceso de reducción para cada dominio
    #@st.cache_data    
        
    reductos = {}
    for domain, questions in dominios_reales.items():
        #print(f"Buscando reducto para el dominio: {domain}")
        reducto = find_reduct_for_domain(questions, nuevo_df3_resultado, threshold=0.9)
        reductos[domain] = reducto

        # Mostrar los reductos para cada dominio
        #for domain, reducto in reductos.items():
            #st.write(f"Dominio: {domain}, Reducto: {reducto}")
            #st.write(f"Reducto encontrado. **Coincidencia: {best_match:.2%}**")



        #########################


    import streamlit as st
    import matplotlib.pyplot as plt
    from matplotlib_venn import venn2

    @st.cache_data
    # Función para generar un diagrama de Venn comparando dos clasificaciones
    def generate_venn(original_partition, reduced_partition, domain_name):
        # Convertir particiones en conjuntos únicos
        original_sets = set(frozenset(group) for group in original_partition)
        reduced_sets = set(frozenset(group) for group in reduced_partition)

        # Intersección, solo en el original, solo en el reducido
        only_original = len(original_sets - reduced_sets)
        only_reduced = len(reduced_sets - original_sets)
        intersection = len(original_sets & reduced_sets)

        # Crear diagrama de Venn
        fig, ax = plt.subplots(figsize=(6, 6))
        venn = venn2(
            subsets=(only_original, only_reduced, intersection),
            set_labels=("Lista completa", "Reducto"),
            ax=ax
        )
        ax.set_title(f"Comparación: {domain_name}", fontsize=12)
    
        return fig

        #st.title("Comparación de Clasificaciones con Diagramas de Venn")
        
    st.markdown("""A continuación se muestran los diagramas de Venn para el grado de coincidencia entre los reductos de cada dominio y la lista completa de preguntas. En el siguiente menú puede seleccionar el dominio a visualizar y debajo se mostrará el diagrama de Venn, donde los numeros representa: la cantidad de indivios contenidos en el cuestionario completo, la intersección y el reducto""")
        
    # Selección del dominio para generar el diagrama
    dominio_seleccionado = st.selectbox("**Seleccione un dominio:**", list(dominios_reales.keys()))

    if dominio_seleccionado:
        # Obtener clasificaciones usando la lista completa de preguntas
        original_partition = indiscernibility(dominios_reales[dominio_seleccionado], nuevo_df3_resultado)

        # Obtener clasificaciones usando el reducto
        reduced_partition = indiscernibility(reductos[dominio_seleccionado], nuevo_df3_resultado)

        # Generar y mostrar el diagrama de Venn
        fig = generate_venn(original_partition, reduced_partition, dominio_seleccionado)
        st.pyplot(fig)

    st.markdown("""**El Cuestionario reducido se muestra a continuación:**""")
        
    # Crear un nuevo DataFrame con solo las preguntas que están en los reductos
    columnas_reducto = ["Folio", "CT", "Nivel de Riesgo"]  # Mantener las columnas clave
    for dominio, preguntas_reducto in reductos.items():
        columnas_reducto.extend(preguntas_reducto)

    # Verificar que las columnas existan en el DataFrame    
    columnas_existentes = [col for col in columnas_reducto if col in nuevo_df3_resultado.columns]

    # Filtrar el DataFrame con las preguntas seleccionadas en los reductos
    df_reductos = nuevo_df3_resultado[columnas_existentes].copy()

    # Mostrar el DataFrame en Streamlit
    st.success("Se ha generado el DataFrame con las preguntas reducidas por dominio.")
    st.dataframe(df_reductos)

    # Permitir descarga del DataFrame con los reductos
    @st.cache_data
    def convertir_csv(df):
        return df.to_csv(index=False).encode("utf-8")

    archivo_csv_reductos = convertir_csv(df_reductos)

    st.download_button(
        label="Descargar datos con preguntas reducidas (CSV)",
        data=archivo_csv_reductos,
        file_name="datos_reductos.csv",
        mime="text/csv"
    )



        ##################### mapa

    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns


#st.title("Mapa de Correlaciones")

    # Opciones para que el usuario elija el tipo de mapa de correlación
    opcion_mapa = st.radio(
        "Seleccione el mapa de correlaciones que desea visualizar:",
        ("Mapa de Correlaciones de Preguntas Reducidas", "Mapa de Correlaciones de Puntajes por Dominio")
    )

    if opcion_mapa == "Mapa de Correlaciones de Preguntas Reducidas":
        #@st.cache_data
        # Verificar si el DataFrame `df_reductos` está disponible y tiene datos
        if not df_reductos.empty:
            # Definir las escalas Likert positiva y negativa
            escala_likert_positiva = {"Siempre": 4, "Casi siempre": 3, "Algunas veces": 2, "Casi nunca": 1, "Nunca": 0}
            escala_likert_negativa = {"Siempre": 0, "Casi siempre": 1, "Algunas veces": 2, "Casi nunca": 3, "Nunca": 4}

            # Omitir las columnas "Folio" y "CT"
            df_reductos_numerico = df_reductos.drop(columns=["Folio", "CT", "Nivel de Riesgo"], errors="ignore").copy()

            # Convertir respuestas a valores numéricos según la escala correspondiente
            for columna in df_reductos_numerico.columns:
                if columna in preguntas_likert_positiva:
                    df_reductos_numerico[columna] = df_reductos_numerico[columna].map(escala_likert_positiva).fillna(np.nan)
                elif columna in preguntas_likert_negativa:
                    df_reductos_numerico[columna] = df_reductos_numerico[columna].map(escala_likert_negativa).fillna(np.nan)

            # Calcular la matriz de correlación
            correlaciones = df_reductos_numerico.corr()

            # Crear el mapa de correlaciones
            fig, ax = plt.subplots(figsize=(40, 32))
            sns.heatmap(
                correlaciones, 
                annot=True, 
                cmap="coolwarm", 
                fmt=".2f", 
                linewidths=0.5, 
                ax=ax
            )
            ax.set_title("Mapa de Correlaciones entre Preguntas Reducidas")

            # Mostrar la gráfica en Streamlit
            st.pyplot(fig)
        else:
            st.warning("No se ha generado el DataFrame con preguntas reducidas.")

    elif opcion_mapa == "Mapa de Correlaciones de Puntajes por Dominio":
        #@st.cache_data
        # Verificar si el DataFrame `nuevo_df3_resultado_dominios` está disponible y tiene datos
        if not nuevo_df3_resultado_dominios.empty:
            # Omitir columnas no numéricas ("Folio" y "Nivel de Riesgo")
            columnas_a_excluir = ["Folio"] + [col for col in nuevo_df3_resultado_dominios.columns if "Nivel de Riesgo" in col]
            df_puntajes_numerico = nuevo_df3_resultado_dominios.drop(columns=columnas_a_excluir, errors="ignore").copy()

            # Calcular la matriz de correlación
            correlaciones = df_puntajes_numerico.corr()

            # Crear el mapa de correlaciones
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(
                correlaciones, 
                annot=True, 
                cmap="coolwarm", 
                fmt=".2f", 
                linewidths=0.5, 
                ax=ax
            )
            ax.set_title("Mapa de Correlaciones entre Puntajes por Dominio")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

            # Mostrar la gráfica en Streamlit
            st.pyplot(fig)
        else:
            st.warning("No se ha generado el DataFrame con puntajes por dominio.")

#######################################################################################################################

    #################

    import streamlit as st
    import pandas as pd
    import numpy as np
    import networkx as nx
    import matplotlib.pyplot as plt

    st.markdown("Red de Correlaciones con Umbral Dinámico y Preguntas más Correlacionadas")

    # Input para el umbral de correlación
    umbral_correlacion = st.number_input(
        "Ingrese el umbral de correlación mínima:",
        min_value=0.0, max_value=1.0, value=0.5, step=0.05
    )


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

    # Escalas Likert
    preguntas_likert_positiva = [
            "P2_1", "P2_4", "P7_1", "P7_2", "P7_3", "P7_4", "P7_5", "P7_6",
            "P8_2", "P9_1", "P9_2", "P9_3", "P9_4", "P9_5", "P9_6",
            "P10_1", "P10_2", "P10_3", "P10_4", "P10_5", "P11_1", "P11_2",
            "P11_3", "P11_4", "P11_5", "P12_1", "P12_2", "P12_3", "P12_4",
            "P12_5", "P12_6", "P12_7", "P12_8", "P12_9", "P12_10", "P13_1"
    ]

    preguntas_likert_negativa = [
            "P2_2", "P2_3", "P2_5", "P3_1", "P3_2", "P3_3", "P4_1", "P4_2",
            "P4_3", "P4_4", "P5_1", "P5_2", "P5_3", "P5_4", "P6_1", "P6_2",
            "P6_3", "P6_4", "P6_5", "P6_6", "P8_1", "P13_2", "P13_3", "P13_4",
            "P13_5", "P13_6", "P13_7", "P13_8", "P15_1", "P15_2", "P15_3",
            "P15_4", "P17_1", "P17_2", "P17_3", "P17_4"
    ]
        
    # Verificar si el DataFrame `df_reductos` está disponible y tiene datos
    if not df_reductos.empty:
        # Convertir las respuestas a escala numérica
        df_reductos_numerico = df_reductos.drop(columns=["Folio", "CT", "Nivel de Riesgo"], errors="ignore").copy()
        for columna in df_reductos_numerico.columns:
            if columna in preguntas_likert_positiva:
                df_reductos_numerico[columna] = df_reductos_numerico[columna].map({
                    "Siempre": 4, "Casi siempre": 3, "Algunas veces": 2, "Casi nunca": 1, "Nunca": 0
                }).fillna(np.nan)
            elif columna in preguntas_likert_negativa:
                df_reductos_numerico[columna] = df_reductos_numerico[columna].map({
                    "Siempre": 0, "Casi siempre": 1, "Algunas veces": 2, "Casi nunca": 3, "Nunca": 4
                }).fillna(np.nan)

        # Calcular la matriz de correlación
        correlaciones = df_reductos_numerico.corr()

        # Crear la red de correlación
        G = nx.Graph()
        variables_relevantes = set()

        for i in correlaciones.columns:
            for j in correlaciones.columns:
                if i != j and abs(correlaciones.loc[i, j]) > umbral_correlacion:
                    G.add_edge(i, j, weight=correlaciones.loc[i, j])
                    variables_relevantes.add(i)
                    variables_relevantes.add(j)

        # Añadir nodos relevantes a la red
        G.add_nodes_from(variables_relevantes)

        # Crear lista de colores para los nodos
        node_colors = [
            "red" if nodo in preguntas_likert_negativa else "green"
            for nodo in G.nodes
        ]

        # Dibujar la red de correlación
        fig, ax = plt.subplots(figsize=(12, 10))
        pos = nx.spring_layout(G, seed=42)

        nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_colors, ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=10, ax=ax)

        # Dibujar bordes
        edges = G.edges(data=True)
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, d in edges], width=1.5, edge_color="gray", ax=ax)

        # Título
        ax.set_title(f"Red de Correlaciones (Umbral > {umbral_correlacion:.2f})", fontsize=14)
        plt.axis("off")

        # Mostrar la gráfica en Streamlit
        st.pyplot(fig)


        # Crear DataFrame con las preguntas más correlacionadas
        preguntas_correlacionadas = []
        pares_vistos = set()  # Para evitar duplicados

        for i in correlaciones.columns:
            for j in correlaciones.columns:
                if i != j and abs(correlaciones.loc[i, j]) > umbral_correlacion:
                    par = tuple(sorted([i, j]))
                    if par not in pares_vistos:
                        preguntas_correlacionadas.append({
                            "Pregunta 1": i,
                            "Pregunta 1 (Descripción)": preguntas.get(i, "Descripción no disponible"),
                            "Pregunta 2": j,
                            "Pregunta 2 (Descripción)": preguntas.get(j, "Descripción no disponible"),
                            "Índice de Correlación": correlaciones.loc[i, j]
                        })
                        pares_vistos.add(par)


            
        # Convertir a DataFrame
        df_preguntas_correlacionadas = pd.DataFrame(preguntas_correlacionadas).drop_duplicates(subset=["Pregunta 1", "Pregunta 2"])

        # Mostrar el DataFrame en Streamlit
        st.write("### Preguntas Más Correlacionadas")
        st.dataframe(df_preguntas_correlacionadas)

    else:
        st.warning("No se ha generado el DataFrame con preguntas reducidas.")


    ##########
        
        
    # Permitir descargar el DataFrame filtrado
    #@st.cache_data
    #def convertir_csv(df):
    #    return df.to_csv(index=False).encode("utf-8")

    #archivo_csv = convertir_csv(nuevo_df)

    #st.download_button(
   #     label="Descargar datos filtrados (CSV)",
   #     data=archivo_csv,
   #     file_name=f"datos_CT_{valor_seleccionado}.csv",
   #     mime="text/csv")


    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.tree import DecisionTreeClassifier, plot_tree
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score


    # Definir las escalas Likert
    escala_likert_positiva = {"Siempre": 4, "Casi siempre": 3, "Algunas Veces": 2, "Casi nunca": 1, "Nunca": 0}
    escala_likert_negativa = {"Siempre": 0, "Casi siempre": 1, "Algunas Veces": 2, "Casi nunca": 3, "Nunca": 4}

    # Preguntas en las escalas positiva y negativa
    preguntas_likert_positiva = [
        "P2_1", "P2_4", "P7_1", "P7_2", "P7_3", "P7_4", "P7_5", "P7_6",
        "P8_2", "P9_1", "P9_2", "P9_3", "P9_4", "P9_5", "P9_6",
        "P10_1", "P10_2", "P10_3", "P10_4", "P10_5", "P11_1", "P11_2",
        "P11_3", "P11_4", "P11_5", "P12_1", "P12_2", "P12_3", "P12_4",
        "P12_5", "P12_6", "P12_7", "P12_8", "P12_9", "P12_10", "P13_1"
    ]

    preguntas_likert_negativa = [
        "P2_2", "P2_3", "P2_5", "P3_1", "P3_2", "P3_3", "P4_1", "P4_2",
        "P4_3", "P4_4", "P5_1", "P5_2", "P5_3", "P5_4", "P6_1", "P6_2",
        "P6_3", "P6_4", "P6_5", "P6_6", "P8_1", "P13_2", "P13_3", "P13_4",
        "P13_5", "P13_6", "P13_7", "P13_8", "P15_1", "P15_2", "P15_3",
        "P15_4", "P17_1", "P17_2", "P17_3", "P17_4"
    ]

    st.title("Árbol de Decisión para Predecir el Nivel de Riesgo")

    # Verificar si el DataFrame `df_reductos` está disponible y tiene datos
    if not df_reductos.empty:
        # Excluir columnas irrelevantes
        columnas_a_excluir = ["Folio", "CT"]
        df_reductos_numerico = df_reductos.drop(columns=columnas_a_excluir, errors="ignore").copy()

        # Convertir preguntas a valores numéricos según la escala Likert correspondiente
        for columna in df_reductos_numerico.columns:
            if columna in preguntas_likert_positiva:
                df_reductos_numerico[columna] = df_reductos_numerico[columna].map(escala_likert_positiva).fillna(np.nan)
            elif columna in preguntas_likert_negativa:
                df_reductos_numerico[columna] = df_reductos_numerico[columna].map(escala_likert_negativa).fillna(np.nan)
        st.dataframe(df_reductos_numerico)
        # Verificar si la columna 'Nivel de Riesgo' está presente
        if "Nivel de Riesgo" in df_reductos_numerico.columns:
            # Separar características (X) y variable objetivo (y)
            X = df_reductos_numerico.drop(columns=["Nivel de Riesgo"])
            y = df_reductos_numerico["Nivel de Riesgo"]

            # Dividir los datos en conjuntos de entrenamiento y prueba
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            # Crear el modelo del árbol de decisión
            model = DecisionTreeClassifier(max_depth=4, random_state=42)
            model.fit(X_train, y_train)

            # Predecir en el conjunto de prueba
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            # Mostrar la precisión del modelo
            st.write(f"### Precisión del modelo en datos de prueba: {accuracy:.2%}")


            # Identificar las características utilizadas en el modelo
            features_importances = model.feature_importances_
            features_usadas = np.array(X.columns)[features_importances > 0]
            importances_usadas = features_importances[features_importances > 0]

            # Crear un DataFrame con las preguntas relevantes y su importancia
            preguntas_utilizadas = pd.DataFrame({
                "Pregunta": features_usadas,
                "Importancia": importances_usadas,
                "Descripción": [preguntas.get(col, "Descripción no disponible") for col in features_usadas]
            }).sort_values(by="Importancia", ascending=False)

            st.write("### Preguntas Utilizadas en el Modelo (Con Importancia)")
            st.dataframe(preguntas_utilizadas)

                
            # Visualizar el árbol de decisión
            fig, ax = plt.subplots(figsize=(12, 8))
            plot_tree(
                model,
                feature_names=X.columns,
                class_names=model.classes_.astype(str),
                filled=True,
                rounded=True,
                fontsize=8,
                ax=ax
            )
            ax.set_title("Árbol de Decisión para Predecir el Nivel de Riesgo")
            st.pyplot(fig)

            # Mostrar preguntas utilizadas
            preguntas_utilizadas = pd.DataFrame({
                "Pregunta": X.columns,
                "Descripción": [preguntas.get(col, "Descripción no disponible") for col in X.columns]
            })

            st.write("### Preguntas Utilizadas en el Modelo")
            st.dataframe(preguntas_utilizadas)

            # Descargar preguntas como CSV
            @st.cache_data
            def convertir_csv(df):
                return df.to_csv(index=False).encode("utf-8")

            archivo_csv = convertir_csv(preguntas_utilizadas)
            st.download_button(
                label="Descargar preguntas utilizadas (CSV)",
                data=archivo_csv,
                file_name="preguntas_utilizadas.csv",
                mime="text/csv"
            )
        else:
            st.warning("El DataFrame no contiene la columna 'Nivel de Riesgo'.")    
    else:
        st.warning("No se ha generado el DataFrame con preguntas reducidas.")


    ####################################

    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.tree import DecisionTreeClassifier, plot_tree
    import matplotlib.pyplot as plt

    # Escalas Likert
    escala_likert_positiva = {"Siempre": 4, "Casi siempre": 3, "Algunas Veces": 2, "Casi nunca": 1, "Nunca": 0}    
    escala_likert_negativa = {"Siempre": 0, "Casi siempre": 1, "Algunas Veces": 2, "Casi nunca": 3, "Nunca": 4}

    # Preguntas en las escalas Likert positiva y negativa
    preguntas_likert_positiva = [
            "P2_1", "P2_4", "P7_1", "P7_2", "P7_3", "P7_4", "P7_5", "P7_6",
            "P8_2", "P9_1", "P9_2", "P9_3", "P9_4", "P9_5", "P9_6",
            "P10_1", "P10_2", "P10_3", "P10_4", "P10_5", "P11_1", "P11_2",
            "P11_3", "P11_4", "P11_5", "P12_1", "P12_2", "P12_3", "P12_4",
            "P12_5", "P12_6", "P12_7", "P12_8", "P12_9", "P12_10", "P13_1"
    ]

    preguntas_likert_negativa = [
            "P2_2", "P2_3", "P2_5", "P3_1", "P3_2", "P3_3", "P4_1", "P4_2",
            "P4_3", "P4_4", "P5_1", "P5_2", "P5_3", "P5_4", "P6_1", "P6_2",
            "P6_3", "P6_4", "P6_5", "P6_6", "P8_1", "P13_2", "P13_3", "P13_4",
            "P13_5", "P13_6", "P13_7", "P13_8", "P15_1", "P15_2", "P15_3",
            "P15_4", "P17_1", "P17_2", "P17_3", "P17_4"
    ]

    # Diccionario de dominios
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
            "Insuficiente sentido de pertenencia e inestabilidad": ["P12_7", "P12_9", "P12_10", "P12_8"]
    }

    st.markdown("Árboles de Decisión para Predecir el Nivel de Riesgo por Dominio")

    # Selección del dominio
    dominio_seleccionado = st.selectbox("Seleccione un dominio:", list(dominios_reales.keys()))

    # Nombre de la columna objetivo en `nuevo_df3_resultado_dominios`
    columna_objetivo = f"{dominio_seleccionado}_Nivel de Riesgo"

    # Verificar si la columna objetivo está en `nuevo_df3_resultado_dominios`
    if columna_objetivo in nuevo_df3_resultado_dominios.columns:
        # Unir `df_reductos` con `nuevo_df3_resultado_dominios` por `Folio`
        df_combinado = df_reductos.merge(
            nuevo_df3_resultado_dominios[["Folio", columna_objetivo]], 
            on="Folio", 
            how="inner"
        )

        # Filtrar preguntas del dominio que están en `df_reductos`
        preguntas_dominio = [p for p in dominios_reales[dominio_seleccionado] if p in df_reductos.columns]

        if preguntas_dominio:
            df_dominio = df_combinado[preguntas_dominio + [columna_objetivo]].copy()

            # Convertir respuestas a escala numérica
            for columna in df_dominio.columns:
                if columna in preguntas_likert_positiva:
                    df_dominio[columna] = df_dominio[columna].map(escala_likert_positiva).fillna(0)
                elif columna in preguntas_likert_negativa:
                    df_dominio[columna] = df_dominio[columna].map(escala_likert_negativa).fillna(0)

            # Separar características (X) y variable objetivo (y)
            X = df_dominio.drop(columns=[columna_objetivo])
            y = df_dominio[columna_objetivo]

            # Crear el modelo del árbol de decisión
            model = DecisionTreeClassifier(max_depth=4, random_state=42)
            model.fit(X, y)
            
            # Visualizar el árbol de decisión
            fig, ax = plt.subplots(figsize=(12, 8))
            plot_tree(
                model,
                feature_names=X.columns,
                class_names=model.classes_.astype(str),
                filled=True,
                rounded=True,
                fontsize=10,
                ax=ax
            )
            ax.set_title(f"Árbol de Decisión - {dominio_seleccionado}")
            st.pyplot(fig)
        else:
            st.warning(f"No hay preguntas disponibles para el dominio '{dominio_seleccionado}' en el DataFrame.")
    else:
        st.warning(f"La columna '{columna_objetivo}' no está en `nuevo_df3_resultado_dominios`.")


    ########################

    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.tree import DecisionTreeClassifier, plot_tree
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    import matplotlib.pyplot as plt

    # Escalas Likert
    #escala_likert_positiva = {"Siempre": 4, "Casi siempre": 3, "Algunas Veces": 2, "Casi nunca": 1, "Nunca": 0}
    #escala_likert_negativa = {"Siempre": 0, "Casi siempre": 1, "Algunas Veces": 2, "Casi nunca": 3, "Nunca": 4}

    st.title("Árboles de Decisión para Predecir el Nivel de Riesgo por Dominio")

    if not df_reductos.empty:
        columnas_a_excluir = ["Folio", "CT"]
        df_reductos_numerico = df_reductos.drop(columns=columnas_a_excluir, errors="ignore").copy()

        # Convertir respuestas a escala numérica
        for columna in df_reductos_numerico.columns:
            if columna in preguntas_likert_positiva:
                df_reductos_numerico[columna] = df_reductos_numerico[columna].map(escala_likert_positiva).fillna(0)
            elif columna in preguntas_likert_negativa:
                df_reductos_numerico[columna] = df_reductos_numerico[columna].map(escala_likert_negativa).fillna(0)

        if "Nivel de Riesgo" in df_reductos_numerico.columns:
            modelos_dominios = {}
            precisiones_dominios = {}


            for dominio, preguntas in dominios_reales.items():
                preguntas_validas = [p for p in preguntas if p in df_reductos_numerico.columns]
                if not preguntas_validas:
                    st.warning(f"No hay preguntas disponibles para el dominio '{dominio}'. Omitiendo...")
                    continue

                st.subheader(f"📊 Modelo para: {dominio}")

                df_dominio = df_reductos_numerico[preguntas_validas + ["Nivel de Riesgo"]].dropna().copy()

                # Separar características y variable objetivo
                X = df_dominio.drop(columns=["Nivel de Riesgo"])
                y = df_dominio["Nivel de Riesgo"]

                # **Verificar si `y` tiene al menos dos clases**
                if len(y.unique()) < 2:
                    st.warning(f"El dominio '{dominio}' no tiene suficiente variabilidad en la variable objetivo. Omitiendo...")
                    continue

                # Dividir datos en entrenamiento y prueba
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

                # **Verificar que X_train no esté vacío**
                if X_train.empty or y_train.empty:
                    st.warning(f"No hay suficientes datos para entrenar el modelo de '{dominio}'. Omitiendo...")
                    continue

                # Entrenar modelo
                model = DecisionTreeClassifier(max_depth=4, random_state=42)
                model.fit(X_train, y_train)
                modelos_dominios[dominio] = model

                # Evaluar el modelo
                y_pred = model.predict(X_test)
                accuracy = accuracy_score(y_test, y_pred)
                precisiones_dominios[dominio] = accuracy  # Guardar precisión
                st.write(f"**Precisión del modelo**: {accuracy:.2%}")

                # Visualizar árbol de decisión
                fig, ax = plt.subplots(figsize=(10, 6))
                plot_tree(model, feature_names=X.columns, class_names=model.classes_.astype(str), filled=True, rounded=True, ax=ax)
                st.pyplot(fig)

            st.success("Modelos generados correctamente.")

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

            
            # ==============================
            # 🔹 FORMULARIO DE DIAGNÓSTICO 🔹
            # ==============================
            st.subheader("📝 Formulario de Evaluación de Riesgo")

            with st.form("form_diagnostico"):
                respuestas_usuario = {}
                for dominio, modelo in modelos_dominios.items():
                    st.subheader(f"{dominio}")
                    respuestas_usuario[dominio] = {}
                    for pregunta in modelo.feature_names_in_:
                        enunciado = preguntas.get(pregunta, pregunta)  # Obtener el enunciado o clave si no está en el diccionario
                        respuestas_usuario[dominio][pregunta] = st.radio(
                            f"{enunciado}", ["Siempre", "Casi siempre", "Algunas veces", "Casi nunca", "Nunca"],
                            key=f"{dominio}_{pregunta}"
                        )

                submit_button = st.form_submit_button("Generar Diagnóstico")
            
            if submit_button:
                diagnosticos = {}

                for dominio, modelo in modelos_dominios.items():
                    respuestas_procesadas = {
                        pregunta: escala_likert_positiva.get(respuesta, np.nan) if pregunta in preguntas_likert_positiva
                        else escala_likert_negativa.get(respuesta, np.nan)
                        for pregunta, respuesta in respuestas_usuario[dominio].items()
                    }

                    df_usuario = pd.DataFrame([respuestas_procesadas])

                    # **Asegurar que las columnas coincidan con las del modelo**
                    missing_cols = set(modelo.feature_names_in_) - set(df_usuario.columns)
                    for col in missing_cols:
                        df_usuario[col] = 0  # Rellenar columnas faltantes con 0

                    df_usuario = df_usuario[modelo.feature_names_in_]  # Reordenar las columnas

                    diagnosticos[dominio] = modelo.predict(df_usuario)[0] if modelo else "No disponible"

                # ==============================
                # 🔹 RESULTADOS DEL DIAGNÓSTICO 🔹
                # ==============================
                st.subheader("📊 Diagnóstico de Riesgo por Dominio")
                for dominio, riesgo in diagnosticos.items():
                    precision_modelo = precisiones_dominios.get(dominio, "No disponible")
                    st.write(f"**{dominio}:** Nivel de riesgo predicho: `{riesgo}`  |  🎯 **Precisión del modelo:** `{precision_modelo:.2%}`")

                # 🔹 **Riesgo Total Promedio**
                #riesgo_total = np.mean([valor for valor in diagnosticos.values() if isinstance(valor, (int, float))])
                #st.write(f"🟡 **Riesgo Total Promedio:** `{riesgo_total:.2f}`")

        else:
            st.warning("El DataFrame no contiene la columna 'Nivel de Riesgo'.")
    else:
        st.warning("No se ha generado el DataFrame con preguntas reducidas.")



        






        #################












    
#    except Exception as e:
#        st.error(f"Se produjo un error al cargar el archivo: {e}")
#else:
#    st.warning("Por favor, sube un archivo Excel para continuar.")

