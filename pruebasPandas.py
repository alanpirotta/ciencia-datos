# coding: utf-8
import pandas as pd
#creo los datos para el DtaraFrame en un diccionario
dict = {     'nombre': ['alan', 'daniela', 'melody'],     'apellido': ['pirotta','serra','pirotta'],     'edad': [33,34,31],     'jubilacion': [65,60,60] }
dict

df = pandas.df(dict)
df = pandas.DataFrame(dict)
df = pd.DataFrame(dict)
df
#Con el método lambda, agarra cada fila y le realiza TODAS las filas de la columna que le mando 
array = df.edad.apply(lambda p: p -df.jubilacion)
array
array = df.edad.map(lambda p: p -df.jubilacion)
array
array = df.edad.map(lambda p: p + df[jubilacion])
df.edad
df.jubilacion
df['edad']
df['jubilacion']
array = df.edad.map(lambda p: p + df['jubilacion'])
array
#La forma correcta de "unir" dos columnas y agregarlas al DataFrame
df['edad']+df['jubilacion']
df['años_restantes']= df['jubilacion']-df['edad']
df
