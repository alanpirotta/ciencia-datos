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
