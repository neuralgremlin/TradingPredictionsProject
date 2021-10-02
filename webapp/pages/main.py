import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

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

    stocks = ["AAPL", "AMZN", "NVDA", "CRM", "ORCL", "MSFT", "V", "BAC", "ADBE", "MA"]

    selected_stock = st.selectbox("Elige una acción para predecir su comportamiento futuro", stocks)


    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data
        
    data_load_state = st.text("Cargando data... ")
    data1 = load_data(selected_stock)
    value_list = [selected_stock]
    sentimientos = pd.read_csv("sentimientos.csv")
    boolean_series = sentimientos.Stock.isin(value_list)
    sentimientos_filtrados = sentimientos[boolean_series]
    sentimientos_filtrados['date'] = pd.to_datetime(sentimientos_filtrados['date'], format='%Y-%m-%d')
    data= pd.merge(data1, sentimientos_filtrados, how= 'left', left_on="Date", right_on="date").fillna(0)
    #data['compound'] = data['compound'].apply(lambda x:(x*20)+100)
    data_load_state = st.text("Cargando data... listo!")

    st.title("Información histórica de " + selected_stock)
    #st.write(data.tail())

    def plot_raw_data():
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'),secondary_y=False)
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'),secondary_y=False)
        fig.add_trace(go.Scatter(x=data['Date'], y=data['compound'], name='news_sentiment'),secondary_y=True)
        fig.layout.update(title_text="Comportamiento de la acción. Desliza la barra de abajo para ver un periodo más corto.", 
                           yaxis_title= "Stock Price",
                           xaxis_rangeslider_visible=True)                           
        fig.update_yaxes(title_text="-    News Sentiment    + ", secondary_y=True)
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
        impacto = st.slider("Impacto en precio futuro:", -50, 50, value=0)
        if st.checkbox('Aplicar ajuste por impacto'):
            
            df_train2 = data[['Date', 'Close']]
            df_train2 = df_train2.rename(columns={"Date": "ds", "Close": "y"})
            

            m2 = Prophet()
            m2.fit(df_train2)
            future2 = m2.make_future_dataframe(periods=period)
            forecast2 = m2.predict(future2)
            forecast2['yhat']=np.where(forecast2['ds']>TODAY, forecast2['yhat'].apply(lambda x:x+impacto),forecast2['yhat'] )
            forecast2['yhat_lower']=np.where(forecast2['ds']>TODAY, forecast2['yhat_lower'].apply(lambda x:x+impacto),forecast2['yhat_lower'] )
            forecast2['yhat_upper']=np.where(forecast2['ds']>TODAY, forecast2['yhat_upper'].apply(lambda x:x+impacto),forecast2['yhat_upper'] )
            #forecast2['yhat']=forecast2['yhat'].apply(lambda x:x+impacto)
            #forecast2['yhat_lower']=forecast2['yhat_lower'].apply(lambda x:x+impacto)
            #forecast2['yhat_upper']=forecast2['yhat_upper'].apply(lambda x:x+impacto)

            st.subheader("Predicción de " + selected_stock + " en un plazo de " + str(n_semanas) + " semanas, con ajuste de "+ str(impacto) + " dolares.")
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
