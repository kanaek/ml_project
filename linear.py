import pandas as pd
import numpy as np
from datetime import datetime
import pickle
import os.path
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn import metrics

linreg = linear_model.Lasso(alpha=0.4)
df_train = pd.read_csv("model/train2.csv")
df = df_train.copy()
feature_cols = ['store_nbr', 'item_nbr','date1j']
X = df[feature_cols]
y = df.log1p
linreg.fit(X, y)

df_test = pd.read_csv("model/test2.csv")
df_tt = df_test.copy()
X_test = df_tt[feature_cols]

y_pred = linreg.predict(X_test)
df_tt['log1p'] = y_pred
df_tt['units'] = np.rint((np.exp(y_pred)-1))
df_tt.to_csv("model/test_re.csv")
print 'finished'