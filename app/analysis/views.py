from django.shortcuts import render
import plotly.graph_objects as go
import pandas
import pandas_datareader.data  as pdr
import datetime

def main(request):
    # データ元
   df = pandas.read_csv('analysis/data/finance-charts-apple.csv')

   fig = go.Figure(data=[go.Candlestick(
       x=df['Date'],
       open=df['AAPL.Open'],
       high=df['AAPL.High'],
       low=df['AAPL.Low'],
       close=df['AAPL.Close']
       )])

   plot_fig = fig.to_html(fig, include_plotlyjs=False)
   return render(request, "analysis/main.html", {"graph": plot_fig})

# Exchange
def real_time_exchange_rate(pair):
    # 現在時刻
    dt_now = datetime.datetime.now()
    today = dt_now.strftime('%Y-%m-%d')
    start, end = today, today
    
    # 為替pairを所定の形に変更
    code = f'{pair}=X'

    # dataの取得
    data = pdr.get_data_yahoo(code, end, start)

    # 最終日（今日）の終値（リアルタイム値）を返す
    return data['Close'][-1]

# USDJPY = real_time_exchange_rate('USDJPY')
# print(USDJPY)

# Stock
def real_time_stock_price(ticker, source='yahoo'):
    # 現在時刻
    dt_now = datetime.datetime.now()
    today = dt_now.strftime('%Y-%m-%d')
    start, end = today, today
    
    # 株価の取得
    data = pdr.DataReader(ticker, source, end, start)
    
    # 最終日（今日）のdataを抽出
    data = data.tail(1)

    # indexをtickerシンボルに書き換える
    data = data.rename(index={data.index[0]: ticker})
    data.index.name='Ticker'

    # 余分な特徴量を削除する
    data = data.drop(['High', 'Low', 'Open', 'Close', 'Volume'], axis=1)
    return data

# data = real_time_stock_price('AAPL')
# print(data)