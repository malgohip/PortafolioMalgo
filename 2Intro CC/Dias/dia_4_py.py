#Author: Sebastian Ochoa. Date: 02/15/2024
# -*- coding: utf-8 -*-

lst=[0,1,2,3,4,5,6,7,8,9]
#x=lst[0]
#print(x)
tpl=(9,8,7,6,5,4,3,2,1,0)
#y=tpl[1]
#print(y)
rng=range(0,20,2)
#z=rng[2]
#print(z)
x=["manzana","naranja","fresa"]
x.append("mango")
x.insert(4,"zapote")
#print(x)

import pandas as pd #pd corresponde a un alias o sigla para referenciar la librería pandas
Datos = { 'Nombre': ['Ana', 'Carlos', 'Luis', 'María', 'Sofía', 'Juan', 'Laura', 'Pedro', 'Elena', 'Diego'],
    'Edad': [25, 32, 28, 20, 29, 34, 22, 28, 26, 31],
    'Género': ['Femenino', 'Masculino', 'Masculino', 'Femenino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino'],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 'Bucaramanga', 'Manizales', 'Cúcuta', 'Pereira', 'Santa Marta'],
    'Profesión': ['Ingeniero', 'Abogado', 'Médico', 'Estudiante','Arquitecto', 'Profesor', 'Diseñador', 'Empresario','Periodista', 'Ingeniero']}
Tabla1 = pd.DataFrame(Datos) #observese que debe incluir el alias antes del comando DataFrane
Tabla1