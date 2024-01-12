from vnstock import stock_historical_data,listing_companies,company_overview,company_profile
import os
import pandas as pd
list_com = listing_companies(live = True)
listTicker = []
for i in range(100,len(list_com)) :
    if list_com['comGroupCode'][i] == "HOSE" :
        listTicker.append(list_com['ticker'][i])

print(listTicker)
