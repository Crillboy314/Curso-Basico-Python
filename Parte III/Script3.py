"""
Script 3: Manejo de paquetes externos para estadistica y presentacion
de datos de forma mas elegante
Autor: kevinrojas
"""

"""
Este archivo fue presentado mientrás se impartía el curso de python.
"""

# Importacion de las librerias que se requieren para los ejemplos

import numpy as np 
import pandas as pd

# Graficas de funciones en Numpy: para este ejemplo utilizamos las funciones
# seno, coseno y una componente de tiempo para darle sentido al eje de las
# abscisas con los valores correspondientes


t = np.arange(0,10,0.1) 
x = np.sin(t)
y = np.cos(t)
df = pd.DataFrame({'Time':t, 'sin':x, 'cos':y})

df.plot()

# Otras opciones de funciones disponibles:

# https://numpy.org/doc/stable/reference/routines.math.html

#Llamados de la columna especifica

print(df.Time)
print(df['Time'])

# Creacion de subconjuntos de la funcion anterior, si es que queremos 
# un mejor resultado de las graficas en cuestion

data = df[['sin', 'cos']]

data.plot()

### Ejemplo con datos mas "reales"

# Creeamos primero un data frame a partir de arreglos en numpy mismo

dfejemplo = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
      columns=['a', 'b', 'c'])

# Aniadir una columna a un dataframe

dffunciones = pd.DataFrame(x, columns = ["sin"])
dffunciones["cos"] = y
dffunciones["tiempo"] = t

print(dffunciones)

# Supongamos que quisieramos evaluar si existen diferencias
# significativas en una encuesta sobre el rendimiento de algo
# como por ejemplo de un grupo, entonces almacenamos los datos en 
# un marco de datos (dataframe) y trabajamos con ello.
# Notemos que en este caso, el data frame se construye desde cero



Percepcion_por_genero = pd.DataFrame({
'Gender': ['f', 'f', 'm', 'f', 'm',
'm', 'f', 'm', 'f', 'm', 'm'], 'rate': [8.4, 8.5, 7.6, 9.7, 9.1, 8.1,
6.1, 8.9, 7.0, 8.3, 9.2]
})


# Agrupar los datos
grouped = Percepcion_por_genero.groupby('Gender')
# Estadisticas descriptivas 
print(grouped.describe())
# Graficar los datos
grouped.boxplot() 


# Convertir en data frame
df_female = grouped.get_group('f')


# Ejercicio adicional con data frame y datos de calificaciones para
# un grupo de estudiantes, sobre los que se quiere visualizar
# el grupo de los aprobados o de los no aprobados

exam_data  = {'name': ['Ana', 'Daniel', 'Katherine', 'Joel', 'Emilia', 'Miguel', 'Marcos', 'Laura', 'Kevin', 'Jonas'],
        'puntaje': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'inscripcion': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'aprueba': ['si', 'no', 'si', 'no', 'no', 'si', 'si', 'no', 'no', 'si']}

labels = ['Est1', 'Est2', 'Est3', 'Est4', 'Est5', 'Est6', 'Est7', 'Est8', 'Est9', 'Est10']

df = pd.DataFrame(exam_data , index=labels)
print(df)

datos_notas = df[['puntaje', 'aprueba']]

## Agrupar los datos por calificacion

grupos = datos_notas.groupby('aprueba')

print(grupos.describe())
grupos.plot.density()

# Otras funciones del data frame pueden encontrarse en:

# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

##### Importación de archivos

#Algunas librerias adicionales

import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import os

os.getcwd()
os.chdir("/Users/kevinrojas/Desktop/Curso python/")

xls = pd.ExcelFile('Salarios.xls') 
datasalary = xls.parse('Sheet 1', index_col=None, na_values=['NA'])

print(datasalary.salary)

generos = datasalary.groupby("gender")

print(generos.describe())

datasalary.hist("salary")

# Otros graficos

datasalary.plot(kind='line',x='graduate',y='salary')

plt.savefig('salarios.png')

# graficas usando series (opcional)

s = pd.Series(datasalary.salary)
ax = s.plot.hist()
ax.figure.savefig('histo.png')
ay = s.plot.box()
ay.figure.savefig('boxplot.png')

##### Modelos de regresion (algo básico para entender el funcionamiento)

# Generate a noisy line, and save the data in a pandas-DataFrame 
x = np.arange(100)
y = 0.5*x - 20 + np.random.randn(len(x))
df = pd.DataFrame({'x':x, 'y':y})

# Fit a linear model, using the "formula" language # added by the package "patsy"
model = sm.ols('y~x', data=df).fit()
print( model.summary() )

