from builtins import print

import input.sentimeter as st
import algos.dense_forest as df
import input.timeseries as ts
import utils.GaugeUtil as gu
import trend as trend


# Where the csv file will live
LSTM_FILE_NAME = 'data/ltp_trends.csv'
FILE_NAME = 'data/historical.csv'
QUOTE = 'NASDAQ:MSFT'
DF_EPOCH_SIZE = 10
LSTM_EPOCH_SIZE= 10

#get Historical data save as csv
ts.get_historical_India_for_df(QUOTE, FILE_NAME)
ts.get_historical_India(QUOTE, LSTM_FILE_NAME)

# analyse trend
trend.getTrends(LSTM_FILE_NAME,LSTM_EPOCH_SIZE)
print(df.stock_prediction(FILE_NAME,DF_EPOCH_SIZE))



# analyse historical data

client = st.TwitterClient()
result = client.predict_stock_sentiment(quote='NSE:TCS', count=500)
print(result)
raw_data = {'sources': ['Twitter Feed', 'Market News'],
                'Positive': [result['tweet_sentiment']['positive_per'], result['news_sentiment']['positive_per']],
                'Negative': [result['tweet_sentiment']['negative_per'], result['news_sentiment']['negative_per']],
                'Neutral': [result['tweet_sentiment']['neutral_per'], result['news_sentiment']['neutral_per']]}

print(raw_data)
gu.plotSentiGraph(raw_data)






