import pandas as pd
import numpy as np

df=pd.read_csv('./share_bike.csv')

df['datetime']=pd.to_datetime(df['datetime'])
#df['datetime']=df['datetime'].dt.hour
#df.rename(columns={'datetime':'hours'},inplace=True)


pd.options.mode.copy_on_write = True
for i in range(len(df)):
    data=df.iloc[i]
    #print(type(data))
    #print(data)
    df.loc[i,"holiday"]=0
    df.loc[i,"workingday"]=1
    print(df.loc[i,"datetime"].dayofweek)
    if(df.loc[i,"datetime"].dayofweek == 5 or df.loc[i,"datetime"].dayofweek == 6):
        df.loc[i,"workingday"]=0
        df.loc[i,"holiday"]=1
