import datetime
from pathlib import Path

import joblib
import pandas as pd
import yfinance as yf
from prophet import Prophet

BASE_DIR = Path(__file__).resolve(strict=True).parent
TODAY = datetime.date.today()


def train_portfolio():
    stocks = ["AAPL", "AMZN", "NVDA", "CRM", "ORCL", "MSFT", "V", "BAC", "ADBE", "MA"]
    for x in stocks:
        train(ticker=x)
        print("Trained model for ticker:",x)


def train(ticker="MSFT"):
    # data = yf.download("^GSPC", "2008-01-01", TODAY.strftime("%Y-%m-%d"))
    data = yf.download(ticker, "2015-01-01", TODAY.strftime("%Y-%m-%d"))
    data.head()
    data["Adj Close"].plot(title=f"{ticker} Stock Adjusted Closing Price")

    df_forecast = data.copy()
    df_forecast.reset_index(inplace=True)
    df_forecast["ds"] = df_forecast["Date"]
    df_forecast["y"] = df_forecast["Adj Close"]
    df_forecast = df_forecast[["ds", "y"]]
    df_forecast

    model = Prophet()
    model.fit(df_forecast)

    joblib.dump(model, Path(BASE_DIR).joinpath(f"{ticker}.joblib"))


def predict(ticker="MSFT", days=7):
    model_file = Path(BASE_DIR).joinpath(f"{ticker}.joblib")
    if not model_file.exists():
        return False
    

    model = joblib.load(model_file)

    future = TODAY + datetime.timedelta(days=days)

    dates = pd.date_range(start="2015-01-01", end=future.strftime("%m/%d/%Y"),)
    df = pd.DataFrame({"ds": dates})

    forecast = model.predict(df)

    # model.plot(forecast).savefig(f"{ticker}_plot.png")
    #model.plot_components(forecast).savefig(f"{ticker}_plot_components.png")

    return forecast.tail(days).to_dict("records")


def convert(prediction_list):
    output = {}
    output1 = {}
    output2 = {}
    output3 = {}
    output4 = {}
    for data in prediction_list:
        date = data["ds"].strftime("%m/%d/%Y")
        output1[date] = data["trend"]
        output2[date] = data["yhat"]
        output3[date] = data["yhat_upper"]
        output4[date] = data["yhat_lower"]
    output["trend"] = output1
    output["yhat"] = output2
    output["yhat_upper"] = output3
    output["yhat_lower"] = output4
    return output
