from sklearn.preprocessing import MinMaxScaler # chuan hoa du lieu
import numpy as np
from tensorflow import keras
import os 
import pandas as pd
from sklearn.metrics import mean_absolute_error # do sai so tuyet doi trung binh
from sklearn.metrics import mean_absolute_percentage_error # do % sai so tuyet doi trung binh

path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
def predictdata(ticker) :
    data_result = pd.read_json
    data_result = pd.read_csv(path+'/data/data_gia1/data_'+ticker+'.csv')
    data_result = data_result.set_index('Date')
    data = data_result['Close']
    data1 = data

    df_test = pd.DataFrame(data1[len(data1)//2:])

    data = data.values.reshape(-1,1)
    sc = MinMaxScaler(feature_range=(0,1))
    sc_train =sc.fit_transform(data.reshape(-1,1))
    final_model = keras.models.load_model('save_model.hdf5')
    print(type(sc_train))
    for i in range(5) :
        # print(sc_train)
        dudoan = []

        dudoan.append(sc_train[len(sc_train)-50:len(sc_train)])

        dudoan = np.array(dudoan)
        dudoan = np.reshape(dudoan,(dudoan.shape[0],dudoan.shape[1],1))

        result = final_model.predict(dudoan)   
        print(result)
    result = sc.inverse_transform(result)
    print(f"thuc : {data[len(data)-1]} du doan tiep theo sau 3 ngay : {result}")
from vnstock import listing_companies
list_com = listing_companies(live=True)
listTicker = []
for i in range(0,len(list_com)) :
    if list_com['comGroupCode'][i] == "HOSE" :
        try :
            listTicker.append(list_com['ticker'][i])
        except(KeyError) :
            break

for i in listTicker : 
    predictdata(i)