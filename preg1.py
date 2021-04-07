# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:17:04 2020

@author: Gedeon
"""

# Importar Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn


# IMPORTAR DATOS
df = pd.read_csv("AAPL_data.csv")
print(df)
df.describe()
mat=df.values
print (mat)
""" 
a) La media, Moda y la desviacion estandar por columna;
Explique que significa cada caso mediante python sin uso de librerias.

USAREMOS EL ALGORITMO DE MEDIA, MODA Y DESVIACION STANDARD PARA CADA LAS COLUMANAS:
    OPEN, HIGHT, LOW, CLOSE Y VOLUME

"""
print(" ")
print("a) La media, Moda y la desviacion estandar por columna; Explique que significa cada caso mediante python sin uso de librerias.")

print("")
# MEDIA = (Sumatoria de Xi)/n
vecprom=[]
for i in range(1,6):   
    prom=0.00
    for j in range(1259):
        prom=prom+float(mat[j][i])
      # print("[",j,"][",i,"]=",mat[j][i])
    promedio=prom/1259
    vecprom.append(promedio)
    print("La Media de la columna ",i," es=",promedio)
#print("vector promedio", vecprom)
    
"""
moda
vecmoda=[]
for i in range(1,6):
    for j in range(1259):
         vecmoda[1]=float(mat[j][i])
         cont=1
         for k in range(j+1,1259):
           #  if vevmoda[1]==float(mat[k][j]):
               #  cont=cont+1
       # print("Contar ", cont)
"""
#DESVIACION ESTANDAR dest= raiz cuadrada((sumatoria(Xi-prom)^2)/n)

for i in range(1,6): 
    sumatoria=0.00
    for j in range(1259):        
        aux=float(mat[j][i])-vecprom[i-1]
        aux=aux**2
        sumatoria=sumatoria+aux     
    print("La desviacion estandar de la columna ",i," es=",(sumatoria/1259)**(0.5))
"""
b) La media, Moda y la desviacion estandar con el uso de numpy y panda.   
    
"""  
print("")
print("b) La media, Moda y la desviacion estandar con el uso de numpy y panda.  ")
print("")

media1=df["open"].mean()
media2=df["high"].mean()
media3=df["low"].mean()
media4=df["close"].mean()
media5=df["volume"].mean()

print("Media Open=",media1)
print("Media high=",media2)
print("Media low=",media3)
print("Media close=",media4)
print("Media volume=",media5)


moda1=df["open"].mode()
moda2=df["high"].mode()
moda3=df["low"].mode()
moda4=df["close"].mode()
moda5=df["volume"].mode()

print("moda Open=",moda1)
print("moda high=",moda2)
print("moda low=",moda3)
print("moda close=",moda4)
print("moda volume=",moda5)

dest1=df["open"].std(ddof=0)
dest2=df["high"].std(ddof=0)
dest3=df["low"].std(ddof=0)
dest4=df["close"].std(ddof=0)
dest5=df["volume"].std(ddof=0)
print("Desviacion Estandar Open=",dest1)
print("Desviacion Estandar high=",dest2)
print("Desviacion Estandar low=",dest3)
print("Desviacion Estandar close=",dest4)
print("Desviacion Estandar volume=",dest5)

"""
c) Graficar los datos y explique   
    
""" 
# Apertura de precio del dia.

plt.figure(figsize=(16,8))
plt.title('Apple')
plt.xlabel('Días')
plt.ylabel('Precio de Apertura USD ($)')
plt.plot(df['open'])
plt.show()

# precio mas alto

plt.figure(figsize=(16,8))
plt.title('Apple')
plt.xlabel('Dias')
plt.ylabel('Precio de cierre USD ($)')
plt.plot(df['high'])
plt.show()

# precio mas bajo

plt.figure(figsize=(16,8))
plt.title('Apple')
plt.xlabel('Dias')
plt.ylabel('Precio de cierre USD ($)')
plt.plot(df['low'])
plt.show()

# precio de cierre

plt.figure(figsize=(16,8))
plt.title('Apple')
plt.xlabel('Dias')
plt.ylabel('Precio de cierre USD ($)')
plt.plot(df['close'])
plt.show()

# volumen

plt.figure(figsize=(16,8))
plt.title('Apple')
plt.xlabel('Dias')
plt.ylabel('Precio de cierre USD ($)')
plt.plot(df['volume'])
plt.show()
