# coding: utf-8
def suma(a,b):
    '''Retorna la suma de los dos parámtros'''
    return a + b 
    
get_ipython().run_line_magic('pinfo', 'suma')
suma(10,25)
num1= 5
num2=35
suma(num1,num2)
resultado=suma(num1,num2)
print(f'El resultado de la suma entre {num1} y {num2} es {resultado}')
