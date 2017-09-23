import requests
from numba.types import byte


def get_historical_India(quote, file_path):
    # Download our file from google finance
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + quote + '&apikey=3FGHYHL0CV6P6P04&datatype=csv'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=MSFT&apikey=3FGHYHL0CV6P6P04&outputsize=full&datatype=csv'
    r = requests.get(url, stream=True)

    if r.status_code != 400:
        with open(file_path, 'w') as f:
            for chunk in r:
                ltp = str(chunk).split(',')[4]
                if (ltp) != 'close':
                    if (float(ltp) != 0):
                        f.write(ltp + '\n')

        return True


def get_historical_India_for_df(quote, file_path):
    # Download our file from google finance
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + quote + '&apikey=3FGHYHL0CV6P6P04&datatype=csv&outputsize=full'
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=MSFT&apikey=3FGHYHL0CV6P6P04&outputsize=full&datatype=csv'
    r = requests.get(url, stream=True)

    if r.status_code != 400:
        with open(file_path, 'wb') as f:
            for chunk in r:
                f.write(chunk)
        return True

        # if __name__ == '__main__':
        #     get_historical_India('NSE:RELIANCE', 'histor.csv')
