import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd

def app():

    st.title("Aplicación de predicción de valor de acciones")



    START = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    st.header("Elige una de las siguientes acciones")
    st.write("Apple Inc. - AAPL")
    st.write("Amazon Inc. - AMZN")
    st.write("NVIDIA Corp. - NVIDIA")
    st.write("Salesforce Inc. - CRM")
    st.write("Oracle Corp. - ORCL")
    st.write("Microsoft Corp. - MSFT")
    st.write("Visa Inc. - V")
    st.write("Bank of America Corp. - BAC")
    st.write("Adobe Inc. - ADBE")
    st.write("Mastercard Inc. - MA")
    st.write(" ")

    stocks = ["AAPL", "AMZN", "NVIDIA", "CRM", "ORCL", "MSFT", "V", "BAC", "ADBE", "MA"]

    selected_stock = st.selectbox("Elige una acción para predecir su comportamiento futuro", stocks)


    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data = load_data(selected_stock)
    data_load_state = st.text("Cargando data... listo!")

    st.title("Información histórica de " + selected_stock)
    #st.write(data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
        fig.layout.update(title_text="Comportamiento de la acción. Desliza la barra de abajo para ver un periodo más corto.", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()



    #Forecasting
    st.title("Predicción de comportamiento futuro")

    n_semanas = st.slider("Semanas de predicción:", 1, 52)
    period = n_semanas * 7

    if st.checkbox('Predecir comportamiento futuro'):
        df_train = data[['Date', 'Close']]
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

        m = Prophet()
        m.fit(df_train)
        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)

        st.subheader("Predicción de " + selected_stock + " en un plazo de " + str(n_semanas) + " semanas.")
        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)

        st.subheader("Forecast data")
        st.write(forecast.tail())

        st.subheader('Componentes para la predicción')
        st.write("La primera gráfica muestra la tendencia que lleva la acción en el tiempo.")
        st.write("La segunda gráfica muestra el comportamiento regular de la acción según el día de la semana.")
        st.write("La tercera gráfica muestra el comportamiento regular de la acción en un año.")
        fig2 = m.plot_components(forecast)
        st.write(fig2)

        st.title("Ajustar futuro con datos externos")
        st.header("Noticias de Google")
        noticias_Google = pd.read_csv("google_news.csv")
        value_list = [selected_stock]
        boolean_series = noticias_Google.Stock.isin(value_list)
        noticias_filtradas = noticias_Google[boolean_series]
        st.write(noticias_filtradas)

        st.header("Si crees que la predicción debería ajustarse por las noticias más recientes, selecciona en qué sentido")
        if st.checkbox('Para mal'):
            df_train2 = data[['Date', 'Close']]
            df_train2 = df_train2.rename(columns={"Date": "ds", "Close": "y"})
            df_train2['y'].iloc[-20] -= 10
            df_train2['y'].iloc[-19] -= 14
            df_train2['y'].iloc[-18] -= 16
            df_train2['y'].iloc[-17] -= 18
            df_train2['y'].iloc[-16] -= 20
            df_train2['y'].iloc[-15] -= 22
            df_train2['y'].iloc[-14] -= 24
            df_train2['y'].iloc[-13] -= 26
            df_train2['y'].iloc[-12] -= 28
            df_train2['y'].iloc[-11] -= 30
            df_train2['y'].iloc[-10] -= 32
            df_train2['y'].iloc[-9] -= 32
            df_train2['y'].iloc[-8] -= 34
            df_train2['y'].iloc[-7] -= 36
            df_train2['y'].iloc[-6] -= 38
            df_train2['y'].iloc[-5] -= 40
            df_train2['y'].iloc[-4] -= 42
            df_train2['y'].iloc[-3] -= 44
            df_train2['y'].iloc[-2] -= 46
            df_train2['y'].iloc[-1] -= 50
            #df_train2['y'].iloc[0] = df_train2['y'].iloc[-30:].apply(lambda x:x-22)
            # df_train2['y'].iloc[-10] = df_train2['y'].iloc[-10].apply(lambda x:x-2)
            # df_train2['y'].iloc[-9] = df_train2['y'].iloc[-9].apply(lambda x:x-4)
            # df_train2['y'].iloc[-8] = df_train2['y'].iloc[-8].apply(lambda x:x-6)
            # df_train2['y'].iloc[-7] = df_train2['y'].iloc[-7].apply(lambda x:x-8)
            # df_train2['y'].iloc[-6] = df_train2['y'].iloc[-6].apply(lambda x:x-10)
            # df_train2['y'].iloc[-5] = df_train2['y'].iloc[-5].apply(lambda x:x-12)
            # df_train2['y'].iloc[-4] = df_train2['y'].iloc[-4].apply(lambda x:x-14)
            # df_train2['y'].iloc[-3] = df_train2['y'].iloc[-3].apply(lambda x:x-16)
            # df_train2['y'].iloc[-2] = df_train2['y'].iloc[-2].apply(lambda x:x-18)
            # df_train2['y'].iloc[-1] = df_train2['y'].iloc[-1].apply(lambda x:x-20)
            #df_train2['y'].iloc[0] = df_train2['y'].iloc[-30:].apply(lambda x:x-22)

            m2 = Prophet()
            m2.fit(df_train2)
            future2 = m2.make_future_dataframe(periods=period)
            forecast2 = m2.predict(future2)

            st.subheader("Predicción de " + selected_stock + " en un plazo de " + str(n_semanas) + " semanas.")
            fig2 = plot_plotly(m2, forecast2)
            st.plotly_chart(fig2)

            st.subheader("Forecast data")
            st.write(forecast2.tail())

            # st.subheader("Predicción afectada de " + selected_stock + " en un plazo de " + str(n_semanas) + " semanas.")
            # fig2 = plot_plotly(m, forecast_mal)
            # st.plotly_chart(fig2)
            #
            # st.subheader("Forecast data")
            # st.write(forecast_mal.tail())
