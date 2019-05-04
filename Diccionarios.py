'''

Diccionarios: Colecciones pero su asignacion es con llaves {}

key: cualquier valor que de referencia al contenido

La rcomendacion es que las llaves con tipos de datos que no tengan mutuacion como tuplas

'''

#Sintaxis

#opcion 1.
mi_dict = {
'Llave 1' : 'valor1',
'Llave2' : 'valor2'
}

#opcion2

otra_dict = dict(llave1 = 'valor1',
    llave2 = 'valor2')

print(mi_dict['Llave 1']) #Para acceder al valor de el primer diccionaario

#Se pude cambiar el valor  ejemplo:

mi_dict['Llave2'] ='BUENOS DIAS'

print(mi_dict['Llave2'])  #se cambio elvalor a 'llave 2' se pueden cambiar por boleanos, tuplas

#listas dentro de diccionario no porque estas son mutables


pass