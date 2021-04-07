# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 00:37:04 2021

@author: Gedeon
"""

# Importar Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn


# IMPORTAR DATOS  Y SEPARACION DE VARIALBLES INDEPENDIENTES Y DEPENDIENTES
dataset = pd.read_csv('AAPL_data.csv')
print(dataset)
x = dataset.iloc[:, :6].values
y = dataset.iloc[:, 6].values

# vamos a resolver los datos categoricos de la columna datos
from sklearn.preprocessing import LabelEncoder
labelencoder_x=LabelEncoder()
x[:,0]=labelencoder_x.fit_transform(x[:,0])

#  vamos a resolver Datos categoricos de la columna NAME
labelencoder_y= LabelEncoder()
y=labelencoder_y.fit_transform(y)

print(dataset)

# Imputacion de datos faltantes
# corrige los datos con "nan" con medias de los datos

from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan, strategy='mean')

imp = imp.fit(x[:, 1:6])
x[:, 1:6] = imp.transform(x[:, 1:6])

print(x[:, 0:7])


# Estandarizacion de escalas

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x=scaler.fit_transform(x)
# Nomalizacion de datos
from sklearn import preprocessing
matriz_normal=preprocessing.normalize(x[:, 0:7])
print(matriz_normal)
