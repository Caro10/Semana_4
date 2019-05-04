#colecciones de funciones, es una estrategia muy utilizada
suma= lambda x,y: x+y
resta= lambda x,y: x-y
multiplique = lambda  x,y : x*y
divide= lambda x,y : x/y
import math

potencia=lambda x,y: math.pow(x,y)
raiz = lambda x,y : math.pow(x,1/y)

x=3
y=2

lista_funciones = [suma,resta,multiplique,divide,potencia,raiz]

for mi_funcion in lista_funciones:
    print('resultado=', mi_funcion(x,y))

#crear un diccionario de funciones que sume, reste, dicide, mu etc

calculadora = {'suma': lambda x,y: x+y,
                'resta': resta,
                'multiplique': multiplique ,
                'divide': divide,
                'potencia': potencia ,
                'raiz': raiz
 }

print('usando dict')
for f in calculadora.values():
    print('resultado=', f(x,y))

pass
