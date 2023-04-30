from django.shortcuts import render
import plotly.graph_objects as go
import pandas

def main(request):
    # データ元
   df = pandas.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

   fig = go.Figure(data=[go.Candlestick(
       x=df['Date'],
       open=df['AAPL.Open'],
       high=df['AAPL.High'],
       low=df['AAPL.Low'],
       close=df['AAPL.Close']
       )])

   plot_fig = fig.to_html(fig, include_plotlyjs=False)
   return render(request, "analysis/main.html", {"graph": plot_fig})