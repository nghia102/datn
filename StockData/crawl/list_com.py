from vnstock import stock_historical_data,listing_companies,company_overview,company_profile
import os
import pandas as pd
import time
list_com = [] #list_com crawl
listTicker = [] #list company ticker hose
listInfor = [] #thong tin
# print(listing_companies(live =True)['comGroupCode'])
list_com = listing_companies(live = True)
for i in range(0,len(list_com)) :
    if list_com['comGroupCode'][i] == "HOSE" :
        try :
            listTicker.append(list_com['ticker'][i])
        except(KeyError) :
            break
for i in listTicker :
    inf = company_profile(i).T[0]["companyProfile"]
    listInfor.append(inf)
    print(inf)
    time.sleep(0.5)
# print(compan
# y_profile('CDC').T)
# print(company_profile('CHP').T[0]["companyProfile"])


p1 = pd.DataFrame()
p1['info'] = listInfor
p1['ticker'] = listTicker

path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
p1.to_csv(path+"\data\list_com1.csv")
print(p1)