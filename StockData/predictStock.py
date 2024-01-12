from sklearn.preprocessing import MinMaxScaler # chuan hoa du lieu
import numpy as np
from tensorflow import keras
import os 
import pandas as pd
from sklearn.metrics import mean_absolute_error # do sai so tuyet doi trung binh
from sklearn.metrics import mean_absolute_percentage_error # do % sai so tuyet doi trung binh
path = os.path.dirname(__file__)

def predictstock(ticker) :
    data_result = pd.read_json(path+'/data/data_gia1/data_'+ticker+'.json')
    data = data_result['Close']

    # data1 = data

    data_predict = []
    final_model = keras.models.load_model(path+'/data/model_train/save_model_'+ticker+'.hdf5')

    for i in range(5) :
            # print(sc_train)
        data1 = data.values.reshape(-1,1)
        sc = MinMaxScaler(feature_range=(0,1))
        sc_train =sc.fit_transform(data1.reshape(-1,1))
        dudoan = []
        dudoan.append(sc_train[len(sc_train)-50:len(sc_train)])

        dudoan = np.array(dudoan)
        dudoan = np.reshape(dudoan,(dudoan.shape[0],dudoan.shape[1],1))

        result = final_model.predict(dudoan)
        result = sc.inverse_transform(result)

        data[len(data)] = result[0][0]   
        data_predict.append(result[0][0])
        print(result[0][0])
        # print(data)

    # print(data_predict)
    df = pd.DataFrame(data_predict)
    # le = [x for x in range(len(df))]
    # df.insert(1,"1",le,True)
    # print(df)
    df.to_json(path+"\data\closepredict\datapredict_"+ticker+".json",orient="records")

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
    try :
        predictstock(i)
    except : 
        df1 = pd.read_json(path+"\data\data_gia1\data_"+i+".json")

        temp = df1['Close'][len(df1)-1]
        df = pd.DataFrame([temp,temp,temp,temp,temp])
        df.to_json(path+"\data\closepredict\datapredict_"+i+".json",orient="records")

        pass
    

