contactos = [ ]

def informacion_contacto ( ) :
    nombre = input ( "Ingresa el nombre:\n" )
    apellido = input ( "Ingresa el apellido:\n" )
    telefono = input ( "Ingresa el teléfono:\n" )
    correo = input ( "Ingresa el correo:\n" )
    sexo = input ( "Ingresa el sexo (M/F):\n" ) 
    direccion = input ( "Ingresa la dirección:\n" )
    contacto = { 
        "Nombre" : nombre,
        "Apellido" : apellido,
        "Teléfono" : telefono,
        "Correo" : correo, 
        "Sexo" : sexo, 
        "Dirección" : direccion
    }
    contactos.append ( contacto )

def buscar_contacto ( ) :
    apellido_buscar = input ( "Ingrese el apellido del contacto a buscar:\n" )
    for contacto in contactos : 
        if contacto["Apellido"].lower() == apellido_buscar.lower(): 
            print ("¡Contacto encontrado!")
            print ( "Nombre:", contacto [ "Nombre" ] )
            print ( "Apellido:", contacto [ "Apellido" ] )
            print ( "Teléfono:", contacto [ "Teléfono" ] )
            print ( "Correo:", contacto [ "Correo" ] )
            print ( "Sexo:", contacto [ "Sexo" ] )
            print ( "Dirección:", contacto [ "Dirección" ] )
            print ( "---" )
            return 
        else: 
            print ( "No se encontró el contacto.")

def eliminar_contacto ( apellido_buscar = None) :
    if apellido_buscar is None :
        apellido_buscar =  input ( "Ingrese el apellido del contacto a eliminar:\n")
    for contacto in contactos : 
        if contacto["Apellido"].lower() == apellido_buscar.lower(): 
            contactos.remove(contacto)
            print ( "Contacto eliminado con éxito." )
            return 
        else: 
            print ( "No se encontró el contacto." )

def editar_contacto ( ) : 
    apellido_buscar = input ( "Ingrese el apellido del contacto a editar:\n")
    for contacto in contactos : 
        if contacto ["Apellido"].lower() == apellido_buscar.lower() :
            eliminar_contacto ( apellido_buscar )
            informacion_contacto ( )
            print ( "Contacto editado con éxito." )
            return
        else: 
            print ( "No se encontró el contacto." )

def listar_contactos( ): 
    print ( "Lista de contactos:" )
    for contacto in contactos: 
        print ( "Nombre:", contacto [ "Nombre" ] )
        print ( "Apellido:", contacto [ "Apellido" ] )
        print ( "Teléfono:", contacto [ "Teléfono" ] )
        print ( "Correo:", contacto[ "Correo" ] )
        print ( "Sexo:", contacto [ "Sexo" ] )
        print ( "Dirección:", contacto [ "Dirección" ] )
        print ( "---" )

def menu_principal ( ) :
    while True : 
        print ("Menú Principal:\n" , "1. Agregar Contacto\n" , "2. Buscar un contacto por apellido\n", "3. Editar un contacto desde cero\n" , "4. Eliminar un contacto\n" , "5. Listar todos los contactos\n" , "6. Salir" )
        opcion = input ( "Ingrese la opción deseada: " )
        if opcion == "1" :
            informacion_contacto ()
        elif opcion == "2" :
            buscar_contacto ()
        elif opcion == "3" : 
            editar_contacto ()
        elif opcion == "4" : 
            eliminar_contacto ()
        elif opcion == "5" :
            listar_contactos ()
        elif opcion == "6" : 
            break 
        else : 
            print ( "Opción inválida. Intente nuevamente.")
        print(contactos)

menu_principal()