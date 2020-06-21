from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import roc_curve, auc
import numpy as np
import datetime
import umap
from .models import KPI, Machine
import joblib

import sqlite3
import pandas as pd

from .models import Measurements, Cnn_Model
from .serializers import MeasurementsSerializer

import json
from keras.models import load_model
from sklearn.preprocessing import StandardScaler, MinMaxScaler


class Calculations:

    def __init__(self):
        pass
    
    def perf_measure(y_actual, y_hat):
        TP = 0
        FP = 0
        TN = 0
        FN = 0

        for i in range(len(y_hat)): 
            if y_actual[i]==y_hat[i]==1:
                TP += 1
            if y_hat[i]==1 and y_actual[i]!=y_hat[i]:
                FP += 1
            if y_actual[i]==y_hat[i]==0:
                TN += 1
            if y_hat[i]==0 and y_actual[i]!=y_hat[i]:
                FN += 1
        return[TP, FP, TN, FN]
    def split_sequences(sequences, n_steps):
        X, y = list(), list()
        for i in range(len(sequences)):
            # find the end of this pattern
            end_ix = i + n_steps
            # check if we are beyond the dataset
            if end_ix > len(sequences):
                break
            # gather input and output parts of the pattern
            seq_x, seq_y = sequences[i:end_ix, :-1], sequences[end_ix-1, -1]
            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)

    def CalcUmap(params):
        print(params)
        print(float(params.get("treshold", 0)))
        # params = json.loads(params)
        nRowsRead = 1000 
        df1 = pd.read_csv('Control.csv', delimiter=',', nrows=nRowsRead)
        df2 = pd.read_csv('Quality.csv', delimiter='\t', nrows=nRowsRead)
        df1.dataframeName = 'Control.csv'
        df2.dataframeName = 'Quality.csv'
        df1.drop([col for col in df1.columns if col.startswith('Wickler')],
                 axis=1, inplace=True)
        df2 = df2[['Stippe_-3000','Unnamed: 0', 'date']]
        nRow, nCol = df1.shape

        print(df1.columns)
        # print(f'There are {nRow} rows and {nCol} columns')
        nRow, nCol = df2.shape
        # print(f'There are {nRow} rows and {nCol} columns')
        df_quality = df2
        df_control = df1
        df_quality = df_quality.drop(['Unnamed: 0'], axis=1)
        df_control = df_control.drop(['Unnamed: 0'], axis=1)
        arr_control = df_control.drop('date', axis=1)
        arr_quality = df_quality.set_index('date')
        stp_str = 'Stippe_-3000'
        treshold = 47.5
        if "treshold" in params and float(params.get("treshold")) > 0:
            treshold = float(params.get("treshold"))


        df_stippe = df_quality[stp_str]
        df_quality[df_quality[stp_str] > treshold][stp_str]
        color = np.where(df_quality[stp_str] > treshold ,'red','black')

        df_control = pd.DataFrame(arr_control, columns=df_control.columns, index= df_control.index)
        df_quality = pd.DataFrame(arr_quality, columns=df_quality.columns, index= df_quality.index)
        df_control = df_control.fillna(0)
        df_stippe = df_stippe.fillna(0)


        alphaP = 2
        if "alpha" in params and float(params.get("alpha")) > 0:
            alphaP = float(params.get("alpha"))

        lasso = linear_model.Lasso(alpha=alphaP, tol=0.2)
        lasso.fit(df_control, df_stippe)
        top_param_lasso = pd.DataFrame([df_control.columns, lasso.coef_]).T
        top_param_lasso.columns = ['param', 'coef']
        # print(top_param_lasso)
        top_param_lasso = top_param_lasso[top_param_lasso['coef'] > 0]
        # top_param_lasso.head()

        df_select_lasso = df_control[top_param_lasso['param']]
        # print(df_control.columns)

        n_neighborsP = 100
        if "n_neighbors" in params and float(params.get("n_neighbors")) > 0:
            alphaP = float(params.get("n_neighbors"))

        min_distP = 0.05
        if "min_dist" in params and float(params.get("min_dist")) > 0:
            min_distP = float(params.get("min_dist"))

        fit = umap.UMAP(n_neighbors=n_neighborsP, min_dist=min_distP, metric='euclidean', random_state=42)
        embedding = fit.fit_transform(df_select_lasso)
        # print(embedding[:1])
        ret = pd.DataFrame(data=embedding, columns=['x', 'y'])
        ret['color']=color
        # print(ret[ret['color']=='red']['x'])
        returns = {
            'basic_umap': {
                'black':{
                    'x': ret[ret['color']=='black']['x'],
                    'y': ret[ret['color']=='black']['y'],
                }, 
                'red':{
                    'x': ret[ret['color']=='red']['x'],
                    'y': ret[ret['color']=='red']['y'],
                }
            },            
        }
        # returns['params'] = {}

        # df_stippe = df_quality[stp_str]
        # df_control = df_control.fillna(0)
        # df_stippe = df_stippe.fillna(0)
        # lasso = linear_model.Lasso(alpha=10.0)
        # lasso.fit(df_control, df_stippe)
        # print(lasso.coef_)
        # print(df_stippe)


        returns['top_parametr_lasso'] = df_select_lasso.columns
        # df_stippe = pd.DataFrame(df_stippe)

        # filename = 'this_afterLasso_umap.sav'
        # embedding_lasso = joblib.load(filename)
        # embedding_lasso = fit.transform(df_select_lasso)
        # print(df_select_lasso.head())

        # fit = umap.UMAP(n_neighbors=50, min_dist = 0.99, random_state=42)
        # embedding_lasso = fit.fit_transform(df_select_lasso)
        # ret = pd.DataFrame(data=embedding_lasso, columns=['x', 'y'])
        # ret['color']=color
        # returns['lasso_umap']['black']['x'] = ret[ret['color']=='black']['x']
        # returns['lasso_umap']['black']['y'] = ret[ret['color']=='black']['y']
        # returns['lasso_umap']['red']['x'] = ret[ret['color']=='red']['x']
        # returns['lasso_umap']['red']['y'] = ret[ret['color']=='red']['y']

        
        return returns

    def CalcCNN(params):
        print(params)
        nRowsRead = 1000 
        df1 = pd.read_csv('Control.csv', delimiter=',', nrows=nRowsRead)
        df2 = pd.read_csv('Quality.csv', delimiter='\t', nrows=nRowsRead)
        df1.dataframeName = 'Control.csv' 
        df2.dataframeName = 'Quality.csv'
        df_control = df1
        df_quality = df2
        df_control = df_control.drop('Unnamed: 0', axis=1).set_index('date')
        df_quality = df_quality.drop('Unnamed: 0', axis=1).set_index('date')
        time = df_quality.index
        df_control.drop([col for col in df1.columns if col.startswith('Wickler')],
                 axis=1, inplace=True)
        df_quality['Stippe_-3000'] = df_quality['Stippe_-3000'].fillna(df_quality['Stippe_-3000'].median())
        # treshold = 47.5
        y = df_quality['Stippe_-3000'] > params.get("treshold", 47.5)
        print(params.get("treshold", 47.5))
        X = df_control
        y = pd.DataFrame(y)
        y['Stippe_-3000'] = y['Stippe_-3000'].astype(float)
        sc = StandardScaler()
        X = sc.fit_transform(X)
        X_df_scaller = pd.DataFrame(X, columns=df_control.columns, index=df_control.index)
        X_df_scaller = X_df_scaller.merge(y, left_index=True, right_index=True, how='outer')
        X = X_df_scaller.values
        n_steps = 4
        X, y = Calculations.split_sequences(X, n_steps)
        # model = load_model('cnn.h5', compile=False)
        yhat_02 = Cnn_Model.predict(X)
        # yhat_02 = model.predict(X)
        predicts02 = yhat_02[:,0]
        predicts02 = predicts02 > 0.5
        predicts02 = predicts02.astype(int)
        y = y.astype(int)   
        print(y, predicts02)
        fpr, tpr, threshold = roc_curve(predicts02, y)
        roc_auc = auc(fpr, tpr)
        
        returns = {
            'cnn': { 
                "false_positive_rate":fpr.tolist(),
                "true_postitve_rate":tpr.tolist(),
                "roc_auc":roc_auc.tolist(),
                "errors": Calculations.perf_measure(predicts02, y),
                "y_pred": predicts02,
                "y_orig": y,
                "date": X_df_scaller.index.values
            },            
        }
        return returns

    

    def Hist(self, params):

        machine = Machine.objects.get(pk=params)
        objects = KPI.objects.all().filter(werk=machine).filter(yields__lte=100)
        table = {'rezeptur': [], 'yield': [], 'material': [], 'kd_name': []}
        for object in objects:
            table['rezeptur'].append(object.rezeptur)
            table['yield'].append(object.yields)
            table['material'].append(object.material)
            table['kd_name'].append(object.kd_name)

        table = pd.DataFrame.from_dict(table)
        mean_rezeptur = table.groupby(['rezeptur']).mean().sort_values(by='yield', ascending=False)
        mean_material = table.groupby(['material']).mean().sort_values(by='yield', ascending=False)
        kd_name_size = table.groupby(['kd_name']).size().sort_values(ascending=False)
        yields_rez = []
        rezeptur = []
        yields_mat = []
        material = []
        number_orders = []
        kd_name = []
        for i,(index,row) in enumerate(mean_rezeptur.iterrows()):
            if i == 10:
                break
            yields_rez.append(int(row['yield']))
            rezeptur.append(index)

        for i,(index,row) in enumerate(mean_material.iterrows()):
            if i == 10:
                break
            yields_mat.append(int(row['yield']))
            material.append(index)

        for i, (index, row) in enumerate(kd_name_size.iteritems()):
            if i == 10:
                break
            kd_name.append(index)
            number_orders.append(row)
        ret = {
            "x_rez": yields_rez,
            "y_rez": rezeptur,
            "x_mat": yields_mat,
            "y_mat": material,
            'x_kd_name': number_orders,
            'y_kd': kd_name
        }
        return ret

    def LinearReg(self,params):
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


    