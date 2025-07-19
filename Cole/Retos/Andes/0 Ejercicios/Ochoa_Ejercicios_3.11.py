# -*- coding: utf-8 -*-

"""
Descripción del problema: 
Durante un juego de cartas, un apostador principiante desea hacer algo de trampa para mejorar su juego. Para esto tiene dos cartas escondidas y podrá tomar una de ellas dependiendo de la carta que ya tenga en la mano. Para escoger la carta con la que hará trampa, el apostador comparará la carta que tiene en la mano (carta_mano) con las dos opciones de cambio (opcion_1 y opcion_2). Al apostador le serviría una carta que tenga el mismo número de la carta que tiene en la mano o una que tenga el mismo palo.

Si las dos cartas escondidas le sirven, el apostador siempre escogerá la primera opción.

Si ninguna de las dos cartas escondidas tiene el mismo número o el mismo palo que la de la mano, entonces el apostador no hará trampa.

Usted debe construir una función que indique la opción que debería escoger el apostador: 1 para la primera carta escondida, 2 para la segunda carta escondida, o 0 si ninguna carta le ayuda al apostador. Cada carta será representada por un diccionario con las llaves "numero" y "palo". Tenga en cuenta que la llave "numero" también puede tener asociadas las letras 'J', 'Q', 'K' y 'A'.
"""

def trampa_cartas (carta_mano: dict, opcion_1: dict, opcion_2: dict)->int:
    """
    Hacer trampa en las cartas
    Retorna cual es la mejor opcion para hacer trampa en las cartas en base a la carta que ya posee y las que mantiene ocultas.
    Parámetros:
        carta_mano (dict): Indica mediante un diccionario con las llaves 'palo' y 'numero' el valor de la carta que posee en el juego.
        opcion_1 (dict): Indica mediante un diccionario con las llaves 'palo' y 'numero' el valor de la primera carta que mantiene oculta.
        opcion_2 (dict): Indica mediante un diccionario con las llaves 'palo' y 'numero' el valor de la segunda carta que mantiene oculta.
    Retorno:
        int: Valor entero que indica que opción le conviene más para ganar el juego siendo que:
             1 es para la primera carta escondida,
             2 es para la segunda carta escondida,
             0 es si ninguna carta le ayuda al apostador.
    """
    retorno=0
    if carta_mano['palo'] == opcion_1['palo'] and carta_mano['palo'] == opcion_2['palo'] or carta_mano['numero'] == opcion_1['numero'] and carta_mano['numero'] == opcion_2['numero'] or carta_mano['palo'] == opcion_1['palo'] and carta_mano['numero'] == opcion_2['numero'] or carta_mano['numero'] == opcion_1['numero'] and carta_mano['palo'] == opcion_2['palo']:
        retorno 1
    else:
        if carta_mano['palo'] == opcion_1['palo'] or carta_mano['numero'] == opcion_1['numero']:
            retorno 1
        elif carta_mano['palo'] == opcion_2['palo'] or carta_mano['numero'] == opcion_2['numero']:
            retorno 2
    return retorno 

"""
Descripción del problema: 
Los cajeros automáticos usualmente tienen restricciones sobre las claves (numéricas) que pueden usarse para retirar. Usted debe construir una función que diga si una clave dada (un número entero con 4 dígitos cuyo primer dígito no es el 0) es permitida de acuerdo a las siguientes reglas:

El mismo dígito no puede aparecer más de dos veces.

No puede haber dígitos consecutivos.

No puede haber números que empiecen por 19, 200 ni 201.

El número debe tener al menos tres dígitos diferentes.
"""

def clave_cajero(pin: int)->str:
    """
    clave cajero
    Indica si la clave de un cajero es valida con algunos parametros.
    Parámetros:
        pin (int): Pin del cajero que se quiere colocar.
    Retorno:
        str: Cadena de caracteres que indica si esta clave es valida.
    """
    respuesta='No esta permitida'
    lista=lista
    if len(lista) == 4:
        respuesta='Esta permitida'
    if lista[0] != '0':
        respuesta='Esta permitida'
    for x in lista:
        if lista.count(x) < 2:
            respuesta='Esta permitida'
    for x in range(1, 4):
        if lista[x] != lista[x-1] + 1:
            respuesta='Esta permitida'
    if not lista.startswith(('19', '200', '201')):
        respuesta='Esta permitida'
    if len(set(lista)) > 3:
        respuesta='Esta permitida'

"""
Descripción del problema: 
Usted ha sido encargado de escribir una función que decida si una contraseña es lo suficientemente segura para un nuevo sistema. Una contraseña segura debe tener al menos 10 caracteres y cumplir con al menos 3 de las siguientes restricciones adicionales:

Debe tener al menos una letra mayúscula y una letra minúscula.

Debe tener al menos un dígito.

Debe tener al menos uno de los siguientes caracteres: !"@$ %&/()=?#

No puede empezar ni terminar con un espacio.
"""

def tiene_mayusculas(valor: str)->bool:
    """ 
    tiene mayuculas
    Indica si una cadena de caracteres posee letras mayusculas.
    Parámetros:
        valor (str): Cadena de caracteres a revisar.
    Retorno:
        bool: Booleano que indica si tiene mayusculas.
    """
    respuesta=valor.islower()
    return respuesta 

def tiene_minusculas(valor: str)->bool:
    """ 
    tiene minusculas
    Indica si una cadena de caracteres posee letras minusculas.
    Parámetros:
        valor (str): Cadena de caracteres a revisar.
    Retorno:
        bool: Booleano que indica si tiene minusculas.
    """
    respuesta=valor.isupper()
    return respuesta 

def tiene_numeros(valor: str)->bool:
    """ tiene numeros
    Indica si una cadena de caracteres posee valores numericos.
    Parámetros:
        valor (str): Cadena de caracteres a revisar.
    Retorno:
        bool: Booleano que indica si tiene numeros.
    """
    respuesta=valor.isalpha()
    return respuesta 

def contrasena_segura(contrasena: str)->str:
    """ contrasena_nueva
    Indica si una contraseña es considerada segura para el sistema de seguridad.
    Parámetros:
        contraseña (str): Contraseña a revisar.
    Retorno:
        str: mensaje de el resultado del cambio.
    """

    mensaje = "La contraseña no es suficientemente segura"

    if len(contrasena) > 10:
        restricciones=0

        if not tiene_mayusculas(contrasena) and tiene_minusculas(contrasena):
            restricciones+=1

        if not tiene_numeros(contrasena):
            restriciones+=1
        
        caracteres='!"@$ %&/()=?#'
        cont_caracteres=0
        for c in caracteres:
            for x in contrasena:
                if c == x:
                    cont_caracteres+=1
        if cont_caracteres > 0:
            restricciones+=1
            
        if contrasena[0] != ' ' and contrasena[-1] != ' ':
            restricciones+=1

        if restricciones >= 3:
            mensaje="La contraseña es segura"

    return mensaje

"""
Descripción del problema: 
Escriba una función que reciba 3 diccionarios que representen las coordenadas de 3 puntos en el espacio. Cada diccionario tendrá dos llaves, "x" y "y", que tendrán asociadas los respectivos componentes de cada coordenada. Su función debe retornar un valor de verdad que indique si los tres puntos se encuentran sobre la misma recta o no.
"""

def puntos (punto_1: dict, punto_2: dict, punto_3: dict)->bool:
    """ puntos en la recta
    Indica si un grupo de 3 puntos se encuentran en la misma recta.
    Parámetros:
        punto_1 (dict): Primer el cual es posible que se encuentre en la misma recta que el resto.
        punto_2 (dict): Segundo el cual es posible que se encuentre en la misma recta que el resto.
        punto_3 (dict): Tercer el cual es posible que se encuentre en la misma recta que el resto.
    Retorno:
        bool: booleano que indica si los 3 puntos se encuentran en la misma recta
    """
    retorno=False
    pendiente_A=(punto_2['y']-punto_1['y'])/(punto_2['x']-punto_1['x'])
    pendiente_B=(punto_3['y']-punto_1['y'])/(punto_3['x']-punto_1['x'])
    pendiente_C=(punto_3['y']-punto_2['y'])/(punto_3['x']-punto_2['x'])
    if punto_1['x'] == punto_2['x'] and punto_1['x'] == punto_3['x'] and punto_2['x'] == punto_3['x'] or punto_1['y'] == punto_2['y'] and punto_1['y'] == punto_3['y'] and punto_2['y'] == punto_3['y'] or pendiente_A == pendiente_B and pendiente_A == pendiente_C and pendiente_B == pendiente_C:
        retorno = True
    return retorno

"""
Descripción del problema: 
El juego de las Picas y Fijas es un juego matemático muy sencillo, que consiste en adivinar un número de 4 cifras cuyos dígitos son todos diferentes. Para esto, el jugador que intenta adivinar deberá decir el número que cree está escondiendo el otro, y este deberá responder el número de picas y fijas que tiene ahora el jugador.

Una pica es un dígito que se encuentra en el número a adivinar pero no está en el lugar correcto, y una fija es un dígito correctamente colocado.

Por ejemplo, si el número a adivinar es 1234, y otro jugador dice 1325, tendrá dos picas y una fija.

Usted debe crear una función que devuelva un diccionario con las llaves "PICAS" y "FIJAS" que represente el resultado de la jugada si un jugador trata de adivinar el numero_secreto con el número intento.
"""

def separar (numero: int)->list:
    """
    separar
    Devuelve una listacon los digitos tras separar un número de 4 cifras.
    Parámetros:
        numero (int): Número el cual se desea separar (recibe valores entre 1000 a 9999).
    Retorno:
        list: lista que contiene los valores de sus cifras.
    """
    cifras=[]
    numero_1=numero//1000
    numero_2=(numero%1000)//100
    numero_3=(numero%100)//10
    numero_4=numero%10
    cifras.append(numero_1)
    cifras.append(numero_2)
    cifras.append(numero_3)
    cifras.append(numero_4)
    return cifras

def picas (numero_secreto: int, intento: int)->int:
    """
    picas
    Indica la cantidad de cifras iguales más no en el mismo lugar entre los 2 números a revisar.
    Parámetros:
        numero_secreto (int): Número el cual se desea adivinar (recibe valores entre 1000 a 9999).
        intento (int): Número el cual se cree es el secreto (recibe valores entre 1000 a 9999).
    Retorno:
        int: numero de picas que se encontraron en el número intento.
    """
    picas=0
    secreto=separar(numero_secreto)
    intento=separar(intento)
    if secreto[0] == intento[0] or secreto[0] == intento[1] or secreto[0] == intento[2] or secreto[0] == intento[3]:
        picas=+1
    if secreto[1] == intento[0] or secreto[1] == intento[1] or secreto[1] == intento[2] or secreto[1] == intento[3]:
        picas=+1
    if secreto[2] == intento[0] or secreto[2] == intento[1] or secreto[2] == intento[2] or secreto[2] == intento[3]:
        picas=+1
    if secreto[3] == intento[0] or secreto[3] == intento[1] or secreto[3] == intento[2] or secreto[3] == intento[3]:
        picas=+1
    return picas

def fijas (numero_secreto: int, intento: int)->int:
    """
    fijas
    Indica la cantidad de cifras iguales y en el mismo lugar entre los 2 números a revisar.
    Parámetros:
        numero_secreto (int): Número el cual se desea adivinar (recibe valores entre 1000 a 9999).
        intento (int): Número el cual se cree es el secreto (recibe valores entre 1000 a 9999).
    Retorno:
        int: numero de fijas que se encontraron en el número intento.
    """
    fijas=0
    secreto=separar(numero_secreto)
    intento=separar(intento)
    if secreto[0] == intento[0]:
        fijas=+1
    if intento[1] == secreto[1]:
        fijas=+1
    if secreto[2] == intento[2]:
        fijas=+1
    if secreto[3] == intento[3]:
        fijas=+1
    return fijas

def picas_y_fijas (numero_secreto: int, intento: int)->dict:
    """
    Picas y fijas
    Indica en un diccionario la cantidad de cifras iguales y en el mismo lugar y la cantidad de cifras iguales más no en el mismo lugar entre los 2 números a revisar.
    Parámetros:
        numero_secreto (int): Número el cual se desea adivinar (recibe valores entre 1000 a 9999).
        intento (int): Número el cual se cree es el secreto (recibe valores entre 1000 a 9999).
    Retorno:
        dict: diccionario que muestra los resultados del intento.
    """
    resultado={}
    picas=picas(numero_secreto,intento)
    fijas=fijas(numero_secreto,intento)
    resultado['PICAS']=picas
    resultado['FIJAS']=fijas
    return resultado