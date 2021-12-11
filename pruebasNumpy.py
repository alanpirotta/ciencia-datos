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
