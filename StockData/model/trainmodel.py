import os 
import pandas as pd
import datetime as dt
import numpy as np
from sklearn.preprocessing import MinMaxScaler # chuan hoa du lieu
from sklearn.metrics import r2_score # do muc do phu hop
from sklearn.metrics import mean_absolute_error # do sai so tuyet doi trung binh
from sklearn.metrics import mean_absolute_percentage_error # do % sai so tuyet doi trung binh

from keras.callbacks import ModelCheckpoint # luu huan luyen tot nhat
from keras.models import Sequential # dau vao du lieu cho model
from keras.layers import LSTM # hoc phu thuoc
from keras.layers import Dropout # tranh hoc tu
from keras.layers import Dense # Dau ra
import tensorflow as tf
from tensorflow import keras #load mohinh
from pickletools import optimize

import plotly.graph_objects as go
import plotly.express as px
def create_model(ticker):
    path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
        # data_result.to_json(path+"\data\data_gia\data_"+ticker_stock+".json",orient="records")
    # data_result = pd.read_json
    data_result = pd.read_json(path+'/data/data_gia1/data_'+ticker+'.json')
    data_result = data_result.set_index('Date')
    data = data_result['Close']
    data1 = data
    data = data.values.reshape(-1,1)
    train_data = data[:len(data)//2]
    sc = MinMaxScaler(feature_range=(0,1))
    sc_train =sc.fit_transform(data.reshape(-1,1))
    #tao cac gia tri de train

    x_train,y_train = [],[]
    for i in range(53,len(train_data)) :
        x_train.append(sc_train[i-50-3:i-3,0])
        y_train.append(sc_train[i])
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
    y_train = np.reshape(y_train,(y_train.shape[0],1))
    return [x_train,y_train]
def trainmodel(listxy,ticker) :
    x_train,y_train = listxy[0], listxy[1]
    #xay mo hinh

    model = Sequential()
    model.add(LSTM(units = 128,input_shape = (x_train.shape[1],1),return_sequences=True))
    model.add(LSTM(units = 64))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.compile(loss ='mean_absolute_error',optimizer = 'adam')

    #train and save model
    #train model
    path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
    save_model = path+'/data/model_train/'+'save_model_'+ticker+'.hdf5'
    best_model = ModelCheckpoint(save_model,monitor="loss",verbose=2,save_best_only=True,mode='auto')
    model.fit(x_train,y_train,epochs=50,batch_size=50,verbose=2,callbacks=[best_model])
from vnstock import stock_historical_data,listing_companies
list_com = listing_companies(live=True)
listTicker = []
for i in range(0,len(list_com)) :
    if list_com['comGroupCode'][i] == "HOSE" :
        try :
            listTicker.append(list_com['ticker'][i])
        except(KeyError) :
            break
for i in range(0,len(listTicker)) :
    try :
        trainmodel(create_model(listTicker[i]),listTicker[i])
    except IndexError :
        pass
    except :
        pass
# def compare_train_and_test(y_train) :
#     sc = MinMaxScaler(feature_range=(0,1))
#     y_train = sc.inverse_transform(y_train)
#     final_model = keras.models.load_model('save_model.hdf5')
#     y_train_predict = final_model.predict(x_train)
#     y_train_predict = sc.inverse_transform(y_train_predict) # gia du doan
#     predict_data = pd.DataFrame(data1[50:len(data1)//2])
#     predict_data['predict'] = y_train_predict
#     print(predict_data)

#     fig = px.line(predict_data, x=predict_data.index, y=["Close","predict"], title='Close data')
#     fig.show()

# # trainmodel()
# compare_train_and_test(y_train)