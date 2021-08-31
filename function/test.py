file = r'D:\duLieuVanHanh\server\data\Gang_test_ver3.csv'
import pandas as pd
from send import client_send

df = pd.read_csv(file)
for i in range(df.shape[0]):
    data = df.loc[i]
    strData = str(data[0])
    strData = strData.replace('[m.]', '')
    #print (strData)
    #print (type(strData))
    client_send(strData)
    strData = strData.split(";")
    #print (strData)