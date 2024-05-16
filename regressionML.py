import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import math
from sklearn.datasets import load_diabetes

dbtData=load_diabetes()

x=dbtData.data
y=dbtData.target

x_train,x_test,y_train_y_test=train_test_split(x,y,test_size=0.2,random_state=21)