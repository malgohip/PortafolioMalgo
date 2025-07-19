"""
Descripcion del problema
Queremos escribir una función que nos diga quién ganará en el lanzamiento de una moneda. Escriba una función que reciba el nombre de la persona que pidió ‘cara’, el nombre de la persona que pidió ‘sello’ y el resultado del lanzamiento (‘cara’ o ‘sello’) y responda con el nombre de la persona que haya acertado.
"""

def moneda(nom_1: str, nom_2: str, resultado: str)->str:
  """ 
  Moneda
  Quien ganará en el lanzamiento de una moneda.
  Parámetros:
    nom_1 (str): Nombre de la persona que elegio cara.
    nom_2 (str): Nombre de la persona que elegio sello.
    resultado (str): Resultado del lanzamiento de la moneda (recibe cara o sello).
  Retorno:
    str: Nombre de la persona que acerto al resultado.
  """
  respuesta=''
  resultado_lower=resultado.lower()
  if resultado_lower == 'cara':
    respuesta=nom_1
  elif resultado_lower == 'sello':
    respuesta=nom_2
  else:
    respuesta='ninguno'
  return respuesta

"""
Descripción del problema
Modifique el programa que cambia la contraseña para que en caso de que no se pueda cambiar la contraseña se le informe al usuario no sólo las restricciones que no se cumplieron sino también las condiciones que sí se cumplieron.
"""

def longitud (valor: str)->int:
  """ longitud
  Indica la longitud de una cadena de caracteres.
  Parámetros:
    valor (str): Cadena de caracteres a revisar.
  Retorno:
    int: Valor de su longitud.
  """
  respuesta=len(valor)
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

def tiene_mayusculas(valor: str)->bool:
  """ tiene mayuculas
  Indica si una cadena de caracteres posee letras mayusculas.
  Parámetros:
    valor (str): Cadena de caracteres a revisar.
  Retorno:
    bool: Booleano que indica si tiene mayusculas.
  """
  respuesta=valor.islower()
  return respuesta 

def tiene_minusculas(valor: str)->bool:
  """ tiene minusculas
  Indica si una cadena de caracteres posee letras minusculas.
  Parámetros:
    valor (str): Cadena de caracteres a revisar.
  Retorno:
    bool: Booleano que indica si tiene minusculas.
  """
  respuesta=valor.isupper()
  return respuesta 

def contrasena_nueva(contrasena: str, nueva: str)->str:
  """ contrasena_nueva
  Indica si una contraseña puede ser cambiada a una nueva.
  Parámetros:
    contrasena (str): Contraseña original.
    nueva (str): Nueva constraseña que se quiere tener.
  Retorno:
    str: mensaje de el resultado del cambio.
  """
  contrasena_correcta = True
  mensaje = ""
  
  if longitud(nueva) < 8:
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos 8 caracteres" + "\n"
  else:
    mensaje += "La nueva contraseña tiene al menos 8 caracteres" + "\n"
      
  if nueva == contrasena:
    contrasena_correcta = False
    mensaje += "La nueva contraseña no puede ser igual a la anterior" + "\n"
  else:
    mensaje += "La nueva contraseña es diferente a la anterior" + "\n"
  
  if nueva.isalnum():
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener signos de puntuación" + "\n"
  else:
    mensaje += "La nueva contraseña tiene signos de puntuación" + "\n"
      
  if tiene_numeros(nueva):
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos un número" + "\n"
  else:
    mensaje += "La nueva contraseña tiene al menos un número" + "\n"
  
  if tiene_mayusculas(nueva):
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos una letra mayúscula" + "\n"
  else:
    mensaje += "La nueva contraseña tiene al menos una letra mayúscula" + "\n"
  
  if tiene_minusculas(nueva):
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos una letra minúscula" + "\n"
  else:
    mensaje += "La nueva contraseña tiene al menos una letra minúscula" + "\n"
  
  if contrasena_correcta:
    contrasena=nueva
    mensaje = "La contraseña se cambió exitosamente"
  
  return mensaje

"""
Descripcion del problema
El valor de un peaje depende del tipo de vehículo (categoría) que pase y de la cantidad de ejes que tenga: automóviles, camionetas y camperos (AUTO) deben pagar 10000; buses y busetas (BUS), 14300; camiones grandes de 2 ejes (CAMION), 16000; camiones de 3 y 4 ejes (CAMION), 28100; camiones de 5 ejes (CAMION), 37700; y camiones de 6 o más ejes (CAMION) deben pagar 41400. Adicionalmente, un vehículo podría tener un descuento especial del 15% por paso frecuente. Escriba una función que reciba el tipo de un vehículo (‘AUTO’, ‘BUS’ o ‘CAMION’) y si tiene descuento especial y calcule el valor que debe pagar en el peaje.
"""

def peaje(tipo: str, ejes:int, descuento: bool)->int:
  """ peaje
  Indica cuanto debe pagar un automovil en un peaje.
  Parámetros:
    tipo (str): Categoria en la que se encuentra el automovil (recibe auto, bus o camion).
    ejes (int): Cantidad de ejes del vehiculo (recibe valores mayores a 1).
    descuento (bool): Informacion si se aplica el descuento de paso frecuente.
  Retorno:
    int: Valor que debe pagar en el peaje.
  """
  valor=0
  tipo=tipo.upper()
  if tipo=='AUTO':
    valor=10000
  elif tipo=='BUS':
    valor=14300
  elif tipo=='CAMION':
    if ejes==2:
      valor=16000
    elif ejes==3 or ejes==4:
      valor=28100
    elif ejes==5:
      valor=37700
    elif ejes>=6:
      valor=41400
    else:
      print("El valor de la cantidad de ejes esta mal suministrado.")
  else:
    print("El valor del tipo de vehiculo esta mal suministrado.")
  if descuento:
    valor=valor-(valor*(15/100))
  return round(valor)

"""
Descripcion del problema 
Escriba una función que reciba por parámetro cuatro números enteros y devuelva el mayor de estos. Si hay dos o más iguales y mayores, retorna cualquiera de estos. La signatura de la función debe ser:
"""

def mayor (a: int, b: int, c:int, d:int)->int:
  """ mayor
  Indica cual de los números dados es el mayor.
  Parámetros:
    a (int): Primer número entero a comparar.
    b (int): Segundo número entero a comparar.
    c (int): Tercer número entero a comparar.
    d (int): Cuarto número entero a comparar.
  Retorno:
    int: Número el cual es más grande.
  """
  mayor=0
  if (a >= b) and (a >= c) and (a >= d):
    mayor=a
  elif (b >= a) and (b >= c) and (b >= d):
    mayor=b
  elif (c >= a) and (c >= b) and (c >= d):
    mayor=c
  else:
    mayor=d   
  return mayor

"""
Descripcion del problema
Escriba una función que reciba una cadena de caracteres tipo str y devuelva un entero. La función devuelve 1 si la cadena tiene numeros,  si toda la cadena es mayuscula devuelve 2, si la cadena solo es minuscula devuelve 3.
"""
def informacion_cadena(texto: str)->int:
  """
  información cadena
  Indica de las opciones dadas como es la cadena dada.
  Parametros:
    texto (str): Cadena de caracteres para revisar.
  Retorno
    int: Número que dicta la opción.
  """
  num=-1
  if not texto.isalpha():
    num=1
  elif texto.isupper():
    num=2
  elif texto.islower():
    num=3
  return num

"""
Descripción del problema:
Modifique el ejercicio que retorna el número mayor para que retorne el número del parámetro en el que se encuentra el número mayor. Si hay dos o más iguales y mayores, debe retornar el número de parámetro menor (ej. si el primer y el tercer parámetro eran los mayores, debe retornar el número 1).
"""

def mayor(a: int, b: int, c: int, d: int) -> int:
  """
  mayor
  Indica cual de los números dados es el mayor.
  Parámetros:
    a (int): Primer número el cual debemos comparar para encontrar el mayor.
    b (int): Segundo número el cual debemos comparar para encontrar el mayor.
    c (int): Tercer número el cual debemos comparar para encontrar el mayor.
    d (int): Cuarto número el cual debemos comparar para encontrar el mayor.
  Retorno:
    int: Posición de los valores ingresados en los que se encuentra el número mayor.
  """
  mayor = a
  posicion = 1
  if (b > mayor):
    mayor = b
    posicion = 2
  elif (c > mayor):
    mayor = c
    posicion = 3
  elif (d > mayor):
    mayor = d
    posicion = 4 
  return posicion
  
"""
Descripción del problema:
La calificación final de un estudiante en un curso depende de las calificaciones que obtenga en 3 exámenes, pero con unas reglas especiales. Si el estudiante sacó más de 4.0 sobre 5.0 en el tercer examen (el examen final), la nota en el curso será la nota del examen final. Si el estudiante saca menos de 2.0 en el examen final, ese examen valdrá el 50% de la nota y los otros dos exámenes valdrán el 25% cada uno. En cualquier otro caso, los exámenes pesarán lo mismo para calcular la nota final. Escriba una función que dadas las notas de los tres exámenes calcule la nota del estudiante en el curso.
"""

def calificacion_final(examen_1: float, examen_2: float, examen_3: float) -> float:
  """
  Calificación final
  Indica a calificación de un estudiante dependiendo de la nota de sus 3 parciales.
  Parámetros:
    examen_1 (float): Calificación del primer parcial realizado por el estudiante (Recibe valores entre 0.0 y 5.0).
    examen_2 (float): Calificación del segundo parcial realizado por el estudiante (Recibe valores entre 0.0 y 5.0).
    examen_3 (float): Calificación del examen final realizado por el estudiante (Recibe valores entre 0.0 y 5.0).
  Retorno:
    float: Nota final que el estudiante sacará con las notas de sus examenes.
  """
  final = 0.0
  if examen_3 > 4.0:
    final = examen_3
  if examen_3 < 2.0:
    final = (((examen_1 + examen_2)/2)*0.5) + (examen_3 * 0.5) 
  else:
    final = (examen_1 + examen_2 + examen_3) / 3
  return final
  
"""
Descripción del problema:
En muchos torneos de fútbol es usual que dos equipos jueguen dos partidos para definir cuál es el mejor de ellos: uno en el estadio del primer equipo y otro en el estadio del segundo equipo. También es usual que, en caso de empate en la cantidad de partidos ganados, los goles de los equipos visitantes cuenten por dos al momento de calcular la diferencia de goles. Escriba una función para calcular el ganador entre dos equipos. La función debe recibir el nombre del primer equipo (A), el nombre del segundo equipo (B), los goles que hizo A de local, los goles que hizo B de visitante, los goles que hizo A de visitante y los goles que hizo B de local. La función debe retornar el nombre del ganador de la serie o la cadena “EMPATE” si hubo un empate entre los equipos.
"""

def torneo_futbol(nombre_A: str, nombre_B: str, goles_local_A: int, goles_visitante_B: int, goles_visitante_A: int, goles_local_B: int)->str:
  """
  torneo fútbol
  Indica que equipo gana en base a la cantidad de goles metidos en cada fecha.
  Parámetros:
    nombre_A (str): Nombre del primer equipo que juega el torneo.
    nombre_B (str): Nombre del segundo equipo que juega el torneo.
    goles_local_A (int): Goles metidos en el primer partido por el quipo A (Recibe valores entre 0 y 31).
    goles_visitante_B (int): Goles metidos en el primer partido por el quipo B (Recibe valores entre 0 y 31).
    goles_visitante_A (int): Goles metidos en el segundo partido por el quipo A (Recibe valores entre 0 y 31).
    goles_local_B (int): Goles metidos en el segundo partido por el quipo B (Recibe valores entre 0 y 31).
  Retorno:
    str: Nombre del equipo ganador del torneo.
  """
  ganador='EMPATE'
  goles_A=goles_local_A + goles_visitante_A
  goles_B=goles_local_B + goles_visitante_B
  if goles_A > goles_B:
    ganador = nombre_A
  elif goles_A < goles_B:
    ganador = nombre_B
  else:
    goles_A_empate=goles_local_A + (goles_visitante_A*2)
    goles_B_empate=goles_local_B + (goles_visitante_B*2)
    if goles_A_empate > goles_B_empate:
      ganador = nombre_A
    elif goles_A_empate < goles_B_empate:
      ganador = nombre_B
    return ganador
  
"""
Descripción del problema:
Las denominaciones de las monedas actualmente disponibles en un país son: 20, 50, 100, 200, 500 y 1000. Escriba una función que reciba la cantidad de monedas de cada denominación que tiene una persona y el valor de un producto y le diga si es posible pagar el producto con el dinero en efectivo que tiene. Ayuda: tiene que revisar si tiene suficiente dinero y, si tiene más de lo necesario, si es posible que le den el cambio con las denominaciones de monedas que se encuentran en circulación.
"""

def pago (cantidad_20: int, cantidad_50: int, cantidad_100: int, cantidad_200: int, cantidad_500: int, cantidad_1000: int, precio_producto: int)->str:
  """
  pago
  Indica si se es capaz de pagar un producto y si se pasa si la cantidad de vueltas se pueden devolver con las monedas en circulación.
  Parámetros:
    cantidad 20 (int): Cantidad de monedas de valor de 20 que poseee el cliente.
    cantidad 50 (int): Cantidad de monedas de valor de 50 que poseee el cliente.
    cantidad 100 (int): Cantidad de monedas de valor de 100 que poseee el cliente.
    cantidad 200 (int): Cantidad de monedas de valor de 200 que poseee el cliente.
    cantidad 500 (int): Cantidad de monedas de valor de 500 que poseee el cliente.
    cantidad 1000 (int): Cantidad de monedas de valor de 1000 que poseee el cliente.
    precio_producto (int): Precio del producto que el cliente quiere comprar.
  Retorno:
    str: Texto que indica los booleanos de si es capaz de pagar el producto y si se le pueden dar vueltas con las monedad en circulación en caso de que tenga más dinero que el requerido.
  """
  puede_pagar=False
  vueltas=False
  presupuesto=(cantidad_20*20)+(cantidad_50*50)+(cantidad_100*100)+(cantidad_200*200)+(cantidad_500*500)+(cantidad_1000*1000)
  if precio_producto <= presupuesto:
    puede_pagar=True
    dinero_vueltas=precio_producto-presupuesto
    if (dinero_vueltas%20) == 0 or (dinero_vueltas%50) == 0 or (dinero_vueltas%100) == 0 or (dinero_vueltas%200) == 0 or (dinero_vueltas%500) == 0 or (dinero_vueltas%1000) == 0:
      vueltas=True
  pago='Que el consumidor pueda pagar el producto posee un valor de',puede_pagar,'y que se le puedan devolver vueltas con las monedas en circulación posee un valor de',vueltas
  return pago

"""
Descripción del problema:
Picas y Fijas es un juego en el que dos personas intentan adivinar un número de 4 dígitos que mantiene en secreto el otro jugador. En cada turno, un jugador propone un número de 4 dígitos y el otro jugador debe informar la cantidad de picas y la cantidad de fijas de ese número. Cada pica significa que en el número propuesto hay un dígito que también está en el número secreto, pero en una posición diferente. Cada fija significa que en el número propuesto hay un número que también está en el número secreto y que está en la misma posición. Por ejemplo, si el número secreto es 5678 y el número que el otro jugador propone es 6579, la respuesta sería *2 picas y 1 fija” porque 5 y 6 están en las posiciones equivocadas y porque el 7 está en la posición correcta. El ganador del juego es el jugador que encuentre el número del otro en la menor cantidad de intentos. En este ejercicio usted debe escribir dos funciones: la primera calculará la cantidad de picas dados un número secreto entre 1000 y 9999, y un número propuesto también entre 1000 y 9999; la segunda función calculará la cantidad de fijas y recibirá también un número secreto y un número propuesto.
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

def picas (numero_secreto: int, numero_propuesto: int)->int:
  """
  picas
  Indica la cantidad de cifras iguales más no en el mismo lugar entre los 2 números a revisar.
  Parámetros:
    numero_secreto (int): Número el cual se desea adivinar (recibe valores entre 1000 a 9999).
    numero_propuesto (int): Número el cual se cree es el secreto (recibe valores entre 1000 a 9999).
  Retorno:
    int: numero de picas que se encontraron en el número propuesto.
  """
  picas=0
  secreto=separar(numero_secreto)
  propuesto=separar(numero_propuesto)
  if secreto[0] == propuesto[0] or secreto[0] == propuesto[1] or secreto[0] == propuesto[2] or secreto[0] == propuesto[3]:
    picas=+1
  if secreto[1] == propuesto[0] or secreto[1] == propuesto[1] or secreto[1] == propuesto[2] or secreto[1] == propuesto[3]:
    picas=+1
  if secreto[2] == propuesto[0] or secreto[2] == propuesto[1] or secreto[2] == propuesto[2] or secreto[2] == propuesto[3]:
    picas=+1
  if secreto[3] == propuesto[0] or secreto[3] == propuesto[1] or secreto[3] == propuesto[2] or secreto[3] == propuesto[3]:
    picas=+1
  return picas

def fijas (numero_secreto: int, numero_propuesto: int)->int:
  """
  fijas
  Indica la cantidad de cifras iguales y en el mismo lugar entre los 2 números a revisar.
  Parámetros:
    numero_secreto (int): Número el cual se desea adivinar (recibe valores entre 1000 a 9999).
    numero_propuesto (int): Número el cual se cree es el secreto (recibe valores entre 1000 a 9999).
  Retorno:
    int: numero de fijas que se encontraron en el número propuesto.
  """
  fijas=0
  secreto=separar(numero_secreto)
  propuesto=separar(numero_propuesto)
  if secreto[0] == propuesto[0]:
    fijas=+1
  if propuesto[1] == secreto[1]:
    fijas=+1
  if secreto[2] == propuesto[2]:
    fijas=+1
  if secreto[3] == propuesto[3]:
    fijas=+1
  return fijas
  
"""
Descripción del problema:
Un número primo es un número que es divisible sólo por 1 y por sí mismo. Los primeros 10 números primos son 2, 3, 5, 7, 11, 13, 17, 19, 23 y 29. Escriba una función que dado un número diga cuál es el menor de los primeros diez números primos por el que es divisible o retorne -1 si no es divisible por ninguno de esos números.
"""

def divisible_primo(numero: int)->int:
  """
  divisible primo
  Indica si un numero es divisible por alguno de los 10 primeros números primos.
  Parámetros:
    numero (int): Número el cual se quiere evaluar entre cual de los primeros 10 primos es divisible.
  Retorno:
    int: Primero de los 10 primeros números primos el cual divida exactamente el número a evaluar. 
  """
  divisor=[-1]
  primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  for x in primos:
    if (numero%x)==0:
      divisor.append(x)
      if divisor[0]==-1:
        divisor.pop(0)
  return divisor[0]

"""
Descripción del problema:
En una competencia sólo pueden participar estudiantes universitarios que sean menores de 23 años o que cumplan 23 años durante el año en curso. Además, pueden participar todos los estudiantes universitarios que hayan cursado menos de 2 años de estudios en la Universidad. Escriba una función que reciba el año de nacimiento de una persona y el año de entrada a la universidad y retorne un valor de verdad indicando si la persona puede participar o no.
"""

def participar_competencia(año_nacimiento: int, año_ingreso: int)->bool:
  """
  participar competencia
  indica si una paersona puede ser invitado a una copetencia en base a su edad y años activos.
  Parámetros:
    año_nacimiento (int): Año en el cual el estudiante a evaluar si puede ingresar nacio (recibe valores entre 1907 y 2023).
    año_ingreso (int): Año en el cual el estudiante ingrso a la universidad (recibe valores entre 2013 y 2023).
  Retorno:
    bool: Booleano que informa que si el estudiante puede o no participar en la competencia.
  """
  participa=False
  if (2023-año_nacimiento)>=23 or (2023-año_ingreso)<2:
    participa=True
  return participa
  
"""
Descripción del problema:
En una ciudad existe una restricción de circulación para los vehículos que depende del número de la placa, del tipo de vehículo, del día de la semana y de la hora del día. Los vehículos particulares sólo tienen restricción de lunes a viernes, dependiendo del último dígito de su placa: los que terminen en un número par no podrán circular entre 6:00 y 8:30 y 15:00 y 19:30 en los días del mes que sean pares; los que terminen en un número impar no podrán circular en los mismos horarios, pero de los días del mes que sean impares. La restricción para los taxis va desde las 5:30 hasta las 21:30, de lunes a sábado: los taxis cuya placa termine en el mismo dígito en que termine el día del mes no podrán circular ese día. Escriba una función que diga si un vehículo puede circular o no dados: el tipo de vehículo (str, TAXI o PARTICULAR), la placa (str, por ejemplo DMZ042), el día del mes (int, entre 1 y 31), el día de la semana (str - Lunes, Martes, Miércoles, Jueves, Viernes, Sábado o Domingo), la hora (int, entre 0 y 23) y el minuto (int, entre 0 y 59).
"""

def restriccion_movilidad (tipo: str, placa: str, dia_mes: int, dia_semana: str, hora: int, minuto: int)->bool:
  """
  restricción movilidad
  Indica si un automovil o taxi posee una restriccion de movilidad en base al día.
  Parámetros:
    tipo (str): Cadena que indica que tipo de vehiculo es aquel que se quiere evaluar (recibe taxi o particular, sin signos de puntuación).
    placa (str): Cadena que indica la placa del vehiculo que se quiere evaluar (recibe en el formato AAA000).
    dia_mes (int): Número que indica en el día del mes en el cual nos encontremos (recibe valores entre 1 y 31).
    dia_semana (str): Cadena que indica el día de la semana en el cual nos encontramos (recibe valores de lunes, martes, miercoles, jueves, sabado o domingo, sin signos de puntuación).
    hora (int): Número que indica la hora en la cual nos encontremos, en un formato de 24 horas (recibe valores entre 1 y 24).
    minuto (int): Número que indica el minuto en el cual nos encontremos (recibe valores entre 0 y 59).
  Retorno:
    bool: Booleano que indica si el vehiculo posee alguna restricción en el momento dado.
  """
  restriccion=False
  tipo_mayus=tipo.upper()
  dia_semana_mayus=dia_semana.upper()
  digito_placa=int(placa[5])
  hora_reloj=hora+minuto/60
  if tipo_mayus == 'PARTICULAR':
    if dia_semana_mayus == 'LUNES' or dia_semana_mayus == 'MARTES' or dia_semana_mayus == 'MIERCOLES' or dia_semana_mayus == 'JUEVES' or dia_semana_mayus == 'VIERNES':
      if (dia_mes%2) == 0 and (digito_placa%2) == 0 or (dia_mes%2) == 1 and (digito_placa%2) == 1:
        if 6 <= hora_reloj <= 8.5 or 15 <= hora_reloj <= 19.5:
          restriccion=True
  if tipo_mayus == 'TAXI':
    if dia_semana_mayus == 'LUNES' or dia_semana_mayus == 'MARTES' or dia_semana_mayus == 'MIERCOLES' or dia_semana_mayus == 'JUEVES' or dia_semana_mayus == 'VIERNES' or dia_semana_mayus == 'SABADO':
      if (dia_mes%10) == digito_placa:
        if 5.5<= hora_reloj <= 21.5:
          restriccion=True
    return restriccion

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