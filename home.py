
import streamlit as st
import yfinance as yf
#@st.cache_data
#def cargar_datos(ticker, periodo):
    #datos = yf.download(ticker, period=periodo)
    #return datos
#Titulo e introducción
st.set_page_config(page_title="Predicción de activos", page_icon="💲", layout="centered")
st.title("Predicción de criptoactivos")
st.write("En esta web podrás estar al día de la información de diversos criptoactivos y realizar predicciones sobre su cotización futura")
st.write("**¿Qué tipo de información quiere?**")
#Opciones
opcion = st.radio("**Seleccione el criptoactivo a analizar**",("Bitcoin", "Ethereum"), index=None)
if opcion is not None:
    ##Clica en BTC
    if opcion == "Bitcoin":
        activo="BTC-USD"
    ##Clica en ETH
    elif opcion == "Ethereum":
        activo="ETH-USD"
    #Extraemos los datos
    ticker=yf.Ticker(activo)
    df=ticker.history(period="max")['Close']
    #Crea un control deslizante para elegir el rango de años con el año mínimo y máximo del dataset para configurar el slider
    activo_min = df.index.min().to_pydatetime() # Convertimos los Timestamps a objetos date de Python
    activo_max = df.index.max().to_pydatetime()
    fecha_inicio, fecha_fin = st.slider(
        'Seleccione las fechas de estudio',
        min_value=activo_min,
        max_value=activo_max,
        value=[activo_min, activo_max]) # Valor inicial: el rango completo

    # Más espacios en blanco
    ''
    ''
    ''
    # Filtra el DataFrame original basándose en lo que el usuario eligió en los widgets
    df_filt=df[(df.index >= fecha_inicio) & (df.index <= fecha_fin)]
    # Crea un encabezado de sección con una línea divisoria gris
    st.header(f'Cotización bursatil de {opcion} (USD)', divider='gray')
    ''
    # Dibuja un gráfico de líneas interactivo usando el DataFrame filtrado
    st.line_chart(
        df_filt.reset_index(),
        x='Date',           # Eje horizontal
        y='Close'            # Eje vertical
        #color='Country Code', # Una línea de color distinto para cada activo
        )
    ''
    ''
    # Crea un encabezado de sección con una línea divisoria gris
    st.header('Métricas básicas', divider='gray')
    ''
    # Crea 3 columnas físicas para mostrar los datos en paralelo (horizontal)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Precio Actual", value=f'{round(df_filt.iloc[-1],2)} $')
    with col2:
        st.metric(label="Capitalización de mercado", value=f'{round(ticker.info['marketCap']/1000000000,3)} B$')
    with col3:
        st.metric(label="Volumen (24h)", value=f'{round(ticker.info['volume24Hr']/1000000000,3)} B$')
    ''
    ''
    # Crea un encabezado de sección con una línea divisoria gris
    st.header('Rentabilidades observadas', divider='gray')
    ''
    #Seleccionar rentabilidad
    option = st.selectbox(
        "Seleccione un período",
        ("1 mes", "1 año", "5 años")
        )
    #Calculo de los valores
    # Rentabilidad 1 mes (30 días)
    r30=(df_filt.iloc[-1]-df_filt.iloc[-30])/df_filt.iloc[-30]*100
    # Rentabilidad 1 año (360 días)
    r360=(df_filt.iloc[-1]-df_filt.iloc[-360])/df_filt.iloc[-360]*100
    # Rentabilidad 5 años (1800 días)
    r1800=(df_filt.iloc[-1]-df_filt.iloc[-1800])/df_filt.iloc[-1800]*100

    #Determinamos el valor a mostrar según la opción seleccionada
    if option == "1 mes":
        valor_mostrar = r30
    elif option == "1 año":
        valor_mostrar = r360
    else:
        valor_mostrar = r1800
    
    #Creamos la columna y mostramos la métrica con su label obligatorio
    col1, = st.columns(1)
    with col1:
        st.metric(label='', value=f"{round(valor_mostrar, 2)} %")
    
    # Local: python -m streamlit run home.py