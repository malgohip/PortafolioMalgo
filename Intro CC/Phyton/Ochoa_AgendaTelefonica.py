#Author: Sebastian Ochoa. Date: 09/25/2024
# -*- coding: utf-8 -*-

"""
Problema: Agenda Telefónica y Datos de los Amigos

Se desea desarrollar un programa en Python que permita gestionar y manipular la información de los contactos personales, como los datos de amigos. El programa debe ser capaz de 
almacenar información detallada de cada contacto y brindar al usuario Ia posibilidad de interactuar con esta información a través de un menú.

Requisitos:
El programa debe iniciar con un menú principal, donde el usuario pueda elegir entre varias opciones.

Funciones que debe incluir:
    • Adicionar un nuevo contacto: se deben solicitar y almacenar los siguientes datos: nombre, apellido, teléfono, correo electrónico, sexo, y dirección.
    • Buscar un contacto por apellido: el usuario podrá buscar contactos ingresando el apellido para obtener la información almacenada.
    • Editar un contacto: permitir modificar los datos de un contacto existente.
    • Eliminar un contacto: dar Ia opción de eliminar un contacto de la lista.
    • Listar todos los contactos: mostrar la lista completa de contactos con todos sus detalles.

Los datos deben estar alojados entre diccionarios y listas, el ejemplo funcional se realizará
con 4 contactos aunque se pueda adicionar más,
"""

a = open('Ochoa_Agenda Telefonica.txt','r+')

def aniadir_contacto():
    print('Para añadir un nuevo contacto requiero los siguientes datos: \n')
    nombre=input('El nombre del nuevo contacto: ')
    apellido=input('El apellido del nuevo contacto: ')
    telefono=input('El telefono del nuevo contacto: ')
    correo=input('El correo del nuevo contacto: ') 
    sexo=input('El sexo del nuevo contacto: ')
    direccion=input('La dirección del nuevo contacto: ')
    L=a.readlines()
    num=len(L)//8+1
    a.write(f'{num}\nNombre: {nombre}\nApellido: {apellido}\nTelefono: {telefono}\nCorreo electronico: {correo}\nSexo: {sexo}\nDireccion: {direccion}\n\n')

def buscar_apellido(apellido: str):
    L=a.readlines()
    for x in range(2,len(L),8):
        if L[x].strip().split()[1]==apellido:
            for y in range(x-1,x+5):
                print(L[y].strip())
            break
    else:
        print('No existe este apellido entre tus contactos')

def editar_contacto():
    print('De los siguientes contactos: \n')
    L=a.readlines()
    for x in L:
        print(x.strip())
    cont=int(input('Cual deseas editar? (Dime su numero): '))
    dadt=int(input('QUe dato deseas editar? (Del 1 al 7): '))
    print(L[(cont-1)*8+dadt].strip().split()[1])

editar_contacto()