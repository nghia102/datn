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

model = Sequential()
model.add(LSTM(units = 128,input_shape = (50,1),return_sequences=True))
model.add(LSTM(units = 64))
model.add(Dropout(0.5))
model.add(Dense(1))
model.compile(loss ='mean_absolute_error',optimizer = 'adam')
print(model.summary())