from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import roc_curve, auc
import numpy as np

import sqlite3
import pandas as pd

from .models import Measurements
from .serializers import MeasurementsSerializer





class Calculations:

    def __init__(self):
        pass

    def Hist(params):
        ret = {
            "x": np.random.random_integers(1, 100, 10),
            "y": np.random.random_integers(1, 100, 10),            
        }
        return ret

    def LinearReg(params):
        #Сделал так потому что некогда разбираться как работают джанговские модели
        conn = sqlite3.connect('db.sqlite3')
        query = "SELECT * FROM dataanalysis_measurements where parameter_id=%s or parameter_id =%s"%(params['Control'][0], params['Quality'][0])
        
        df = pd.read_sql_query(query,conn)
        
        date_X = df[df['parameter_id'] == params['Control'][0]]['date']
        date_Y = df[df['parameter_id'] == params['Quality'][0]]['date']


        X = df[df['parameter_id'] == params['Control'][0]]
        X = X['value']
        y = df[df['parameter_id'] == params['Quality'][0]]
        y = y['value']


        X_train = X[:1000].values.reshape(-1,1)
        X_test = X[-1000:].values.reshape(-1,1)
        
        y_train = y[:1000].values.reshape(-1,1)
        y_test = y[-1000:].values.reshape(-1,1)


        #Не стал париться с подтягиванием уже обученой модельки. Для теста будем сразу по ходу обучать
        regr = linear_model.LinearRegression()
        regr.fit(X_train, y_train)
        y_pred = regr.predict(X_test)

        mse =  mean_squared_error(y_test, y_pred)
        print('Coefficients: \n', regr.coef_)
        print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
        
        print('Variance score: %.2f' % r2_score(y_test, y_pred))

        fpr, tpr, thresholds = roc_curve(y_test, y_pred, pos_label=2)
        roc_auc = auc(fpr, tpr)
        ret = {
            "coefc":regr.coef_.tolist(),
            "mean_squared_error": mse,
            "variance_score":r2_score(y_test, y_pred),
            "X_test":X_test.tolist(),
            "y_test":y_test.tolist(),
            "y_pred":y_pred.tolist(),
            "false_positive_rate":fpr.tolist(),
            "true_postitve_rate":tpr.tolist(),
            "roc_auc":roc_auc.tolist(),
            "date": date_X.tolist()
        }
        return ret
        pass
