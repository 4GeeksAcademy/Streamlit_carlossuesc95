import streamlit as st
import yfinance as yf

#@st.cache_data


st.set_page_config(page_title="Predicción de activos", page_icon="💲", layout="centered")
st.title("Predicción de criptoactivos")
st.write("A través de esta app podrás estar al día de la información de diversos criptoactivos y,además, realizar predicciones sobre su cotización futura")
st.write("**¿Qué tipo de información quiere?**")
#Espacio entre las opciones
''
''
#Opciones
st.write("**Seleccione el criptoactivo a analizar**")
opcion = st.radio(("Bitcoin", "Ethereum"), index=None)
##Clica en BTC
if opcion == "Bitcoin":
    ticker=yf.Ticker("BTC-USD")
    df_btc=ticker.history(period="max")['Close']
    #Crea un control deslizante para elegir el rango de años
    # Obtiene el año mínimo y máximo del dataset para configurar el slider
    btc_min = df_btc.index.min()
    btc_max = df_btc.index.max()
    fecha_inicio, fecha_fin = st.slider(
    'Seleccione las fechas de estudio',
    min_value=btc_min,
    max_value=btc_max,
    value=[btc_min, btc_max]) # Valor inicial: el rango completo

    # Más espacios en blanco
    ''
    ''
    ''
    # Filtra el DataFrame original basándose en lo que el usuario eligió en los widgets
    df_btc_filt=df_btc[(df_btc.index >= fecha_inicio) & (df_btc.index <= fecha_fin)]
    # Crea un encabezado de sección con una línea divisoria gris
    st.header('Cotización bursatil de Bitcoin (USD)', divider='gray')
    ''
    # Dibuja un gráfico de líneas interactivo usando el DataFrame filtrado
    st.line_chart(
        df_btc_filt.reset_index(),
        x='Date',           # Eje horizontal
        y='Close'            # Eje vertical
        #color='Country Code', # Una línea de color distinto para cada país
    )
    ''
    ''
    # Crea un encabezado de sección con una línea divisoria gris
    st.header('Métricas básicas', divider='gray')
    ''
    # Crea 3 columnas físicas para mostrar los datos en paralelo (horizontal)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Precio Actual", value=f'{round(df_btc_filt["Close"].iloc[-1],2)} $')
    with col2:
        st.metric(label="Capitalización de mercado", value=f'{round(ticker.info['marketCap']/1000000000,3)} B$')
    with col3:
        st.metric(label="Volumen (24h)", value=f'{round(ticker.info['volume24Hr']/1000000000,3)} B$')
    ''
    ''
    #Seleccionar rentabilidad
    option = st.selectbox(
        "Seleccione el periodo de rentabilidad",
        ("1 mes", "1 año", "5 años")
    )
    #Calculo de los valores
    # Rentabilidad 1 mes (30 días)
    r30=(df_btc_filt['Close'].iloc[-1]-df_btc_filt['Close'].iloc[-30])/df_btc_filt['Close'].iloc[-30]*100
    # Rentabilidad 1 año (360 días)
    r360=(df_btc_filt['Close'].iloc[-1]-df_btc_filt['Close'].iloc[-360])/df_btc_filt['Close'].iloc[-360]*100
    # Rentabilidad 5 años (1800 días)
    r1800=(df_btc_filt['Close'].iloc[-1]-df_btc_filt['Close'].iloc[-1800])/df_btc_filt['Close'].iloc[-1800]*100

    st.write("Haz seleccionado:", option)
        #Mostramos resultado en una columna
    col = st.columns(1)

    if option=="1 mes":
        with col:
            st.metric(value=f'{round(r30,2)} %')
    elif option=="1 año":
        with col:
            st.metric(value=f'{round(r360,2)} %')  
    else:
        with col:
            st.metric(value=f'{round(r1800,2)} %')
    





