# coding: utf-8
import numpy as np
a =  np.array ( [1,2,3,4,5,6,7,8,9,10] )
a.size
a.ndim
a.shape
b =  np.array ( [1,2,3,4,5,6,7,8,9,10] )
a+b
a+10
a*2
a*b
a/b
a.dtype
c=a/b
c
c.dtype
np.zeros(10)
np.zeros(10, dtype=int)
np.empty(10, dtype=int)
np.random.randint(0, 6, 10)
a = np.random.randint(0,10,10)
a[3]
a[-2]
a[-1] = 8
#Formas de generar subarreglos
a = np.random.randint(0,10,20)
a[0:5]
a[0:5:2]
a[:5:2]
a[5:]
a[5::2]
a[ [0,1,3]]
b = np.array([1,2,3,4,5])
b[[True,False,False,True,True]]
c= np.random.randint(0,10,20)
def operacion(valor):
    return (valor**2)+2
    
operacion(3)
for valor in c:
    print(operacion(valor))
    
    
vector = np.vectorize(operacion)
vector(c)
#cambia todos los numeros del array y le aplica la funcion
vector = np.vectorize(lambda valor: (valor**2)+2)
vector(c)
a = np.arange(0,10)
a
a.copy()
b= a.copy()
b
id(a)
id(b)
a is b
a===b
a==b
a.view()
c = a.view()
#a origina, b copia, c vista
id(c)
#Si modifica a, modifico todas las vistas pero no las copias
# otra forma de genera vistas
d = a[:]
d.base is a
c.base is a
b.base is a
A = np.array( [
[1,2,3,4,5],
[10,20,30,40,50],
[100,200,300,400,500]
])
#Matriz de 3 filas 5 columnas
A.ndim
#dimensiones
A.shape
#Forma del arreglo. Axi0= Filas Axi1= Columnas
#Forma de ubicar un elemento A[fila][columna]
#Alternativa A[fila,columna] PREFERIDA!
A[1,:4]
A[1,4:]
A[0,[1,3]]
#Lista de indice para indicar valores separados
A[1,4:8]
A.std()
A.sum()
A.min()
A.max()
A.mean()
#Métodos de agregación 
A[0].max()
#Transpose
B= A.T
B.shape
ran50 = np.random.randint(0,100,50)
ran50 > 50
ran50condicionado = ran50[ (ran50>50) & (ran50<80)]
ran50condicionado
np.all(ran50 >50)
np.all(ran50condicionado >50)
np.any(ran50condicionado <50)
np.any(ran50 <50)
calificaciones = np.random.randint(1, 11, 10)
calificaciones
#Se aprueba con 7 o más
aprobacion = np.where(
calificaciones >= 7,
'Felicidades, aprobaste!',
'La materia está reprobada')
aprobacion
condiciones = [
(calificaciones == 10),
( (calificaciones == 9) | (calificaciones == 8) ),
(calificaciones == 7),
(calificaciones < 7),
]
opciones = [
('Sobresaliente!'),
('Destacado'),
('Aprobado'),
('Desaprobado')
]
estado = np.select(condiciones, opciones)
estado
calificaciones  = np.append(calificaciones,7)
condiciones = [
(calificaciones == 10),
( (calificaciones == 9) | (calificaciones == 8) ),
(calificaciones == 7),
(calificaciones < 7),
]
estado = np.select(condiciones, opciones)
estado
# Crear y leer archivos
txt = np.random.randint(0,10,10)
txt
np.savetxt('desdeIPython.txt',txt)
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('load', 'desdeIPython.txt')
# %load desdeIPython.txt
9.000000000000000000e+00
7.000000000000000000e+00
0.000000000000000000e+00
9.000000000000000000e+00
3.000000000000000000e+00
1.000000000000000000e+00
5.000000000000000000e+00
4.000000000000000000e+00
9.000000000000000000e+00
9.000000000000000000e+00
np.savetxt('desdeIPython.txt',a, fmt='%i')
np.savetxt('desdeIPython.txt', txt, fmt='%i')
get_ipython().run_line_magic('load', 'desdeIPython.txt')
# %load desdeIPython.txt
9
7
0
9
3
1
5
4
9
9
#convierte los complejos en enteros
#leer un archivo dek sisstema
np.loadtxt('desdeIPython.txt')
txtCargado = np.loadtxt('desdeIPython.txt')
txtCargado
#para matrices trabajar con csv
txt.size
txt.reshape( (2,5) )
#convertí en matriz de 2 filas 5 columnas 
matriz = txt.reshape( (2,5) )
np.save('matriz.csv',matriz,delimeter=',')
np.savetxt('matriz.csv',matriz,delimeter=',')
np.savetxt('matriz.csv', matriz, delimiter=',')
get_ipython().run_line_magic('ls', '')
loadtxt('matriz.csv')
np.loadtxt('matriz.csv')
get_ipython().run_line_magic('load', 'matriz.csv')
# %load matriz.csv
9.000000000000000000e+00,7.000000000000000000e+00,0.000000000000000000e+00,9.000000000000000000e+00,3.000000000000000000e+00
1.000000000000000000e+00,5.000000000000000000e+00,4.000000000000000000e+00,9.000000000000000000e+00,9.000000000000000000e+00
np.savetxt('matriz.csv', matriz, delimiter=',', fmt='%i')
d = np.loadtxt('matriz.csv', delimiter=',')
d
#save-load para archivos binarios y savetxt-loadtxt texto plano
np.save('arreglo_binario.npy', txt)
get_ipython().run_line_magic('ls', '')
loadBinario = np.load('arreglo_binario.npy')
loadBinario
a = np.random.randint(0,10,10)
a.size
#los array son más rapidos que las listas al ser inmutables de longitud
# insert y append
np.insert(a, 0, 200)
#insert (array, index, valor)
np.append(a,200)
#Hay que guardarlos en una nueva variable (incluso sobreescribir la misma
a= np.append(a,200)
a
np.delete(a, -1)
a
a= np.delete(a, -1)
a
np.resize(a, 5)
np.resize(a, 5)
b = np.array([1,2,3,4,5])
np.concatenate(a,b)
np.concatenate( [a,b] )
np.concatenate( [b,a] )
a = np.random.randint(0,10,20)
a
a.sort()
a
a[::-1]
#ESto último es para ordenar al revés, pero genera uno nuevo
a = a[::-1]
a
b = np.random.randint(0,10,20)
b
np.sort(b)
#Esta funcion sort genera un nuevo arreglo, diferente al método sort
