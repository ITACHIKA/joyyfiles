import pandas as pd
df=pd.read_csv("data_short.csv")
file=open("result.txt","w")
df['UID']=df['UID'].astype(str)
df=df.drop("rowNumber",axis=1)
data=df.values
print(data)

def levelBasedOnMonthly(monthlyVal):
    if(monthlyVal>=40*1e5):
        return 5
    elif(monthlyVal>20*1e5):
        return 4
    elif(monthlyVal>8*1e5):
        return 3
    elif(monthlyVal>3*1e5):
        return 2
    elif(monthlyVal>1e5):
        return 1
    return 0

def levelBasedOnHistory(historyVal):
    if(historyVal>=40*1e6):
        return 5
    elif(historyVal>20*1e6):
        return 4
    elif(historyVal>8*1e6):
        return 3
    elif(historyVal>3*1e6):
        return 2
    elif(historyVal>1e6):
        return 1
    return 0

file.write("UID  Time  Level\n")

for i in range(1,len(data)):
    prevUID=data[i-1][0]
    prevTotal=data[i-1][2]
    curUID=data[i][0]
    curTotal=data[i][2]
    level=-1
    if(curUID==prevUID):
        if(prevTotal<1e6 and curTotal>=1e6):
            level=1
        if(prevTotal<3*1e6 and curTotal>= 3*1e6):
            level=2
        if(prevTotal<8*1e6 and curTotal>= 8*1e6):
            level=3
        if(prevTotal<20*1e6 and curTotal>= 20*1e6):
            level=4
        if(prevTotal<40*1e6 and curTotal>= 40*1e6):
            level=5
        if(level==-1):
            level=min(levelBasedOnHistory(curTotal),levelBasedOnMonthly(curTotal-prevTotal))
    prevUID=curUID
    prevTotal=curTotal
    #print(curUID+" "+data[i][1]+" "+str(level))
    file.write(curUID+" "+data[i][1]+" "+str(level)+"\n")