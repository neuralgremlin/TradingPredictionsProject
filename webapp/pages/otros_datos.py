import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd

def app():

    #Generales
    START = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    #Criptomonedas
    st.title("Criptomonedas")
    cripto = ['BTC-USD','ETH-USD','LTC-USD','ADA-USD','DOGE-USD']
    selected_cripto = st.selectbox("Elige una acción para predecir su comportamiento futuro", cripto)

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data = load_data(selected_cripto)
    data_load_state = st.text("Cargando data... listo!")

    st.subheader("Información de " + selected_cripto)
    #st.write(data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
        fig.layout.update(title_text="Comportamiento de la acción. Desliza la barra de abajo para ver un periodo más corto.", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()

    #Forex
    st.title("Forex")
    forex = ['JPY=X','MXN=X','EURUSD=X','CNY=X','GBPUSD=X']
    selected_forex = st.selectbox("Elige una acción para predecir su comportamiento futuro", forex)

        #Data del stock
    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data = load_data(selected_forex)
    data_load_state = st.text("Cargando data... listo!")

    st.subheader("Información de " + selected_forex)
    #st.write(data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
        fig.layout.update(title_text="Comportamiento de la acción. Desliza la barra de abajo para ver un periodo más corto.", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()


    #Index
    st.title("Index")
    indexes = ['^GSPC','^DJI','^IXIC']
    selected_index = st.selectbox("Elige una acción para predecir su comportamiento futuro", indexes)

        #Data del stock
    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data = load_data(selected_index)
    data_load_state = st.text("Cargando data... listo!")

    st.subheader("Información de " + selected_index)
    #st.write(data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
        fig.layout.update(title_text="Comportamiento de la acción. Desliza la barra de abajo para ver un periodo más corto.", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()


    #Futuros
    st.title("Futuros")
    futures = ['CL=F','SI=F','GC=F','BZ=F']
    selected_futures = st.selectbox("Elige una acción para predecir su comportamiento futuro", futures)

        #Data del stock
    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data = load_data(selected_index)
    data_load_state = st.text("Cargando data... listo!")

    st.subheader("Información de " + selected_index)
    #st.write(data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
        fig.layout.update(title_text="Comportamiento de la acción. Desliza la barra de abajo para ver un periodo más corto.", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()
