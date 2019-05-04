#Crear una agenda de contactos con estructura diccionarios.
#Juan perez, telefono, email
# carlos rojas, telefono, email
# Ana marin, telefon, email
''''
mis_contactos= {
                   {'nombre1':'Juan perez','carlos rojas','ana marin'},
{'telefonos': '854652', '8568752', '8569544'},
{'correos': 'jperez@gmail.com', 'carro8547@gmail.com','anma568@gamail.com'}

}
#Mejora para acceder mejor a la informacion
'''
#RESPUESTA PROFESOR
#no poner coma como lo hice arriba, me hicienron falta los corchetes en la de arriba
#primer dicionario vacio
''''

agenda = {

    'juan perez': [83014256, 'jperez@gmail.com'] # una forma de hacerlo

}

'''
#otra forma de hacerlo

agenda = {
    'juan perez': {'telefono':83659852,
                   'correo':'jerewb@jhhf.com'},
    'Carlos rojas': {'telefono': 8695425,
                     'correo': 'crojas@gmj.com'},
    'Ana Marin':{'telefono': 8549758,
                 'correo':'marina5895@ hotmail.com'}
}


'''''
#cuantas personas hay en la agenda

print(len(agenda)) #no iterar, es mas productivo asi.

#Cuales son los nombres de los contactos que estan en la agenda

print(agenda.keys()) #retorna un diccionario s epuede transformar en listas o en tupla.

print(tuple(agenda.keys()))#se puede transformas en lsita o tupla)

#Usando la agenda imprima la informacion de cada contacto.
#metodos key()lista de keys items()lista de tuplas,key y valores values () lista de valores
'''''
#for i in agenda.values():
    #print(agenda)

#print(agenda.values())



#Respuesta

for persona in agenda.keys():
    print('nombre:', persona,
          'telefono:', agenda[persona]['telefono'],   #dicionarios de diccionarios
          'correo:',agenda[persona]['correo'])

#otra forma es con  items()

for persona, info in agenda.items():
    print('nombre:', persona,
          'telefono:', info['telefono'],
          'correo:', info['correo'])


#pregunta numero 5, suponga que juan perez cambio de telefono,ahora tiene 2 nuevos en total

agenda['juan perez'] ['telefono'] = ['6546455645','65454646456']
print(agenda)

#sexta pregunta, nuevo contacto llamado sofia, telefono 3333333, correo sof34@gmail.com. agregar el contactos.
#varias maneras de agrefar nuevo contacto.
#opcion 1 : crear diccionario para sofia
sofia = {'telefono': 333333,
         'correo': 'sofia@gmail.com'}
agenda ['sofia castro'] = sofia

#opcion 2

agenda.update({'sofia alfaro':sofia})
'''''
carolina = {'telefono': 89528030,
           'correo':'caro10@gmail.com'}
def agenda_2(h, z):
    for i in agenda:
         print(agenda.update({'carolina picado': carolina}))   


agenda_2(Carolina, 89528030)
''''

def agregar_contactos (nombre,telefono, correo):
    agenda.update({nombre:
                       {'telefono': telefono, #opcion 1
                        'correo':correo}})

agenda[nombre]= {'telefono': telefono, #opcion 2
                 'correo': correo}

agregar_contactos(nombre='felipe',
                  telefono= 32654,
                  correo=fbfb@ijfwrojg)

pass


