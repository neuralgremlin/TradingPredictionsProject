import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd

def app():

    st.title("Selección de Stocks y descarga de datos")

    START = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    df_stocks = pd.read_csv("stocks.csv")
    
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
    
    stocks = df_stocks["Símbolo"]
    selected_stock = st.selectbox("Elige una acción para descargar su csv", stocks)

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data = load_data(selected_stock)
    data_load_state = st.text("Cargando data... listo!")

    if st.checkbox('Descargar data de la acción ' + selected_stock):
        data.to_csv(selected_stock+".csv")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.title("Data descargada!")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.header("Echa un vistazo a la data")
        st.subheader("Información de " + selected_stock)
        st.write(data.tail())

        def plot_raw_data():
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
            fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
            fig.layout.update(title_text="Comportamiento de la acción. Desliza la barra de abajo para ver un periodo más corto.", xaxis_rangeslider_visible=True)
            st.plotly_chart(fig)
        plot_raw_data()
