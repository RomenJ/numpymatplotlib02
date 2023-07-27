import numpy as np
import matplotlib.pyplot as plt


print ('Prácticas de matrices muldidimensionales')
print ('Creación y descripción de matrices muldidimensionales')
print("MATRIZ de valores 10's  de 10x20x30 ")
# Array cuyos valores son todos el valor indicado como segundo parámetro de la función
g=np.full((10, 20, 30), 10)
print("La matriz de 10 es la siguiente:\n ",g)
print("Nº de elementos de la matriz 1 : ",g.size)
print("Lista de dimensioens  forma: ",g.shape)
h=np.full((50, 60), 10)
print("Nº de elementos de la matriz 2 : ",h.size)
print("Lista de dimensioens forma: ",h.shape)
plt.plot(h)
plt.show()
print("Matriz de elementos aleatorios de 3 x 4 ")
i=np.random.rand(3,4)
print(i)
print("Nº de elementos de la matriz 2 : ",i.size)
print("Lista de dimensiones forma: ",i.shape)
# Inicialización del Array utilizando una función personalizada
print("INICIALIZACIÓN DEL ARRAY COMO FUNCIÓN 1")

def func(x, y):
    return x + 2 * y

print(np.fromfunction(func, (3, 5)))
print("INICIALIZACIÓN DEL ARRAY COMO FUNCIÓN 2")

def myfunc(x, y):
    return x + 1 * y

print(np.fromfunction(myfunc, (2, 5)))
print("INICIALIZACIÓN DEL ARRAY COMO FUNCIÓN 3")

def yourfunc(x, y):
    return x + 8 * y

j=np.fromfunction(yourfunc, (3, 5))
print(j)

#acceso a los arrays unidimensionales #
print('ACCESO A LOS ARRAYS UNIDIMENSIONALES ')
arrayUniDim=np.array([34,5,6,77,8,44])
print('Array Unidimensional \n ',arrayUniDim)
print('Array Unidimensional elemento 1', arrayUniDim[0])
print('Array Unidimensional elemento 2',arrayUniDim[1])
print('Array Unidimensional elemento 3 ', arrayUniDim[3])
print('Array Unidimensional elemento 0 al 3 --> 0:3 ', arrayUniDim[0:3])
print('Array Unidimensional elemento 0 y el 3--> 0::3 ', arrayUniDim[0::3])
print('Array Unidimensional elemento  0 y el 4--> 0::4 ', arrayUniDim[0::4])
print('ACCESO A LOS ARRAYS MULTIMDENSIONALES ')
print('ARRAYS MULTIMDENSIONAL 1 ')
k=np.full((8,4,5),7)
print(k)
print(k[2,2])
j2=np.array([[2,3,4,5,6], [5,7,4,2,7 ]])
print('ARRAYS MULTIMDENSIONAL 2 \n', j2)
print("El valor a imprimir de j2 es el 0,4 cuyo valor es 6 ...", j2[0,4])
print("El valor a imprimir de j2 es el 1,3 cuyo valor es 2 ...", j2[1,3])
print("El valor a imprimir de j2  de la primera seginda fila...", j2[1,:])
#ARITMÉTICA DE  Array#
print('Modificación DE ARRAYS')
#Inicialización ARRAY de rangos #
m=np.arange(22)
print('Valores del array m\n',m)
mx=np.arange(22)
print('Valores del array m\n',mx)
xx=m+mx
print( 'Valores del array xx\n',xx)
xx[4]=544
print( 'NUEVA ASIGNACIÓN DE Valores del array xx--> xx[4]=544 \n',xx)
yy=m-mx
print( 'RESTA DE VALORES EN ARRAYS 1:\n',yy)
yy2=xx-m
print( 'RESTA DE VALORES EN ARRAYS 2:\n',yy2)
print( 'RESTA DE VALORES EN ARRAYS 2:\n',yy2)
hk=np.full((4,4),2)
print(' ARRAY hk')
print(hk)
hkmas=hk*2
print(' ARRAY hk con multiplicación\n',hkmas)
print(' ARRAY hk original')
print(hk)
hkmas=hkmas*2
print(' ARRAY hk con multiplicación kmas * 2\n',hkmas)


#Modificación de un Array#
print('Modificación DE ARRAYS')
# Creación de un Array unidimensional inicializado con el rango de elementos 0-27
array1 = np.arange(100)
print("Shape:", array1.shape)
print("Array 1:", array1)
array2=array1.reshape(20,5)
print('El array2 es: \n ', array2)
array3=array1.reshape(50,2)
print('El array3 es : \n ', array3)
#plt.plot(array3)#
#plt.show()#
arrayx2=np.full((4,4),6)
arrayx2[0,:]=233
arrayx3=arrayx2.reshape(8,2)
print("arrayx3:", arrayx3)
#print("arrayx2 1:", arrayx2.ravel())
####3Broadcasting##

arraya1 = np.arange(5)
arraya2 = np.array([3])
print("Shape Arraya1:", arraya1.shape)
print("Array a1:", arraya1)
print()
print("Shape Arraya 2:", arraya2.shape)
print("Array a2:", arraya2)
print("La suma de los vectores arrayas 1 y 2 es ",arraya1 + arraya2)

#ARANGE #
arraya3 = np.arange(2, 100, 2)
print("Arraya3\n",arraya3)
arraya4 = np.arange(0, 1000, 1)
print("Arraya4\n",arraya4)
arraya5=arraya4.reshape(100,10)
print("Arraya5\n",arraya5)
#Funciones estadísticas sobre Arrays#
#media #
print("Arraya5 media: \n",arraya5.mean())
print("Arraya4 media: \n",arraya4.mean())
arrayNotas=np.array([10,3,5,6,8,10,9,8])
print("Array Notas: ", arrayNotas)
print("La suma de todos los valores de la clase ",arrayNotas.sum())
print("La media de todos los valores de la clase ",arrayNotas.mean())
print("La suma de todos los valores del 1 al 1000",arraya4.sum())
unoacien=np.arange(0, 100, 1)
print('Vector de 1 a 100',unoacien)
unoacienenFila10=unoacien.reshape(10,10)
print('Vector de 1 a 100 en fila ',unoacienenFila10)
print('Matriz elevada al cuadrada ',unoacienenFila10)
print('Matriz elevada al cuadrada ')
print(np.square(unoacienenFila10))
print('Raíz cuadrada ')
print(np.sqrt(unoacienenFila10))
print('Exponencial ')
print(np.exp(unoacienenFila10))

#progesión geométrica#
arrex=np.geomspace(10, 1000, num=3)
print('El array exponencial de r 3',arrex)
# MISCELÁNEA #
print("MISC")
arrayy2=np.full((3,3),200)
print(array2)
arrayrange1=np.arange(1)
arrayrange2=np.arange(8)
arrayrange3=np.arange(6,18,2)
arrayrange4=np.arange(1,101,2)
print("Vector arrange 1",arrayrange1)
print("Size arrange 1",arrayrange1.size)
print("Shape arrange 1",arrayrange1.size)
print("Vector arrange 2",arrayrange2)
print("Size arrange 2",arrayrange2.size)
print("Shape arrange 3",arrayrange3)
print("Vector arrange 4",arrayrange4)
print("Vector arrange 4",arrayrange4.size)
arrayrange5=arrayrange4.reshape(25,2)

print("Vector arrange 5",arrayrange5)
plt.plot(arrayrange5)
plt.show()


