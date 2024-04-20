#!/usr/bin/python3

import os

'''


    Nombre: ISBN-13 duplicados en Argentina

    Probar hipotesis: Un código ISBN se puede  duplicar

    Fuente de datos: Archivos CSV con un conjunto de 240 libros con su ISBN entre los datos

    Actualizacion: 10/04/2024 a las 17:37 por Nico Pauer

    Autores:

        * Nico Pauer (programación y edición de archivos)
'''

# Abro archivo con datos CSV en modo lectura
tabla = open('libros-argentinos.csv', 'r')
# Muestro pausadamente lineas del archivo 

lineas = tabla.readlines()

codigos = []

espera = 3

for linea in lineas:

    print('| %s |\n' % linea.replace(',', ' | ').replace('\n', ''))

    # LA ESPERA INICIA CON UNA CANTIDAD INICIAL SEGUNDOS Y SE VA ACORTANDO A MEDIDA QUE EL USUARIO PODRIA CANSARSE DE ESPERAR
    os.system('sleep %s' % espera)

    espera -= 1

    codigos.append(linea.split(',')[0])
# Busco duplicados 2 apariciones o mas
print('Hipotesis: ¿UN CÓDIGO ISBN SE PODRÍA REPETIR? ...')
for codigo in codigos:
    # Recciono distinto segun resultado    
    if (codigos.count(codigo) > 1):
        
        print('\tCódigo ISBN %s aparece %s veces por lo tanto si se demustra que un ISBN se pueda duplicar.\n' % (codigo,               codigos.count(codigo)))

        break

    elif (codigos.count(codigo) == 1):

        os.system('clear')
        print('------------------------------------------------------------------------------------------------------------------------------')
        print('\t¿Hipotesis: UN CÓDIGO ISBN SE PODRÍA REPETIR?\t\n')
        print('El Código ISBN %s  y otros mas aparecen solo una vez, por ahora con estos datos la hipotesis todavía no se demustra.\n' % codigo)
        print('------------------------------------------------------------------------------------------------------------------------------')
# Cierro el archivo para que esté disponible al sistema
tabla.close()
