
from pykrx import stock
from datetime import date


today = date.today().strftime('%Y-%m-%d')
# print(today,type(today))
df = stock.get_index_ohlcv_by_date(today,today,'1001')
print(df['종가'].values[0])

