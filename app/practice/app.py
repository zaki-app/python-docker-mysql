import yfinance as yf 
import streamlit as st
import pandas as pd
import datetime

# header
st.write("""
# シンプルな株価アプリ

googleの終値と出来高です

""")

# 今日の日付
dt_now = datetime.datetime.now().strftime("%Y-%m-%d")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id', start='2010-5-31', end=dt_now)

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


