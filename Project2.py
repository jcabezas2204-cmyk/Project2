#Trabajo en equipo 

import json
catalogo={}
usuarios={}
prestamos=[]
ruta="Biblioteca.json"

#guardar_datos
def guardar_datos(catalogo, usuarios, prestamos, ruta):
    datos={
        "catalogo": catalogo,
        "usuarios": usuarios,
        "prestamos": prestamos
        }
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)
    
#cargar_datos(ruta)
def cargar_datos(ruta):
    with open(ruta, "r") as archivo:
        datos = json.load(archivo)
    return datos
    
try:

    datos = cargar_datos(ruta)

    catalogo = datos["catalogo"]

    usuarios = datos["usuarios"]

    prestamos = datos["prestamos"]

except:

    pass

def menu_principal():
    while True:

        print("Seleccione:")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Buscar libro")
        print("4. Registrar usuario")
        print("5. Dar de baja usuario")
        print("6. Historial usuario")
        print("7. Registrar préstamo")
        print("8. Registrar devolución")
        print("9. Listar vencidos")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            agregar_libro()

        elif opcion == "2":
            eliminar_libro()

        elif opcion == "3":
            buscar_libro()

        elif opcion == "4":
            registrar_usuario()

        elif opcion == "5":
            dar_baja_usuario()

        elif opcion == "6":
            historial_usuario()

        elif opcion == "7":
            registrar_prestamo()

        elif opcion == "8":
            registrar_devolucion()

        elif opcion == "9":
            listar_vencidos()

        elif opcion == "0":
            print("Programa finalizado")

            break

        else:
            print("Opción inválida")

#Libro:
#agregar libro
def agregar_libro():
    isbn = input("isbn: ")
    if isbn in catalogo:
        print(f"El isnb", (isbn),"ya existe")
        return

    libro = {
        "isbn": isbn,
        "titulo": input("Título: "),
        "autor": input("Autor: "),
        "genero": input("Género: "),
        "ejemplares_totales": int(input("Ejemplares totales: ")),
        "ejemplares_disponibles": int(input("Ejemplares disponibles: "))
    }
    if libro["ejemplares_disponibles"] <= libro["ejemplares_totales"]:
        catalogo[isbn] = libro
        guardar_datos(catalogo, usuarios, prestamos, ruta)
        print("Libro agregado")
        return catalogo
    else:
        print(f"Error: el valor de ejemplares disponibles es mayor a los totales")

#eliminar_libro
def eliminar_libro():
    isbn = input("isbn a eliminar: ")
    
    if isbn not in catalogo:
        print("El libro no existe")
        return
    
    for prestamo in prestamos:
        if prestamo["isbn"] == isbn and not prestamo["devuelto"]:
            print("El libro tiene préstamos activos")
            return

    del catalogo[isbn]
    guardar_datos(
        catalogo,
        usuarios,
        prestamos,
        ruta
    )
    print("Libro eliminado")

#buscar_libro
def buscar_libro():
    termino = input("Buscar: ").lower()
    for isbn in catalogo:
        libro = catalogo[isbn]
        if (
            termino in libro["isbn"].lower()
            or termino in libro["titulo"].lower()
            or termino in libro["autor"].lower()
            or termino in libro["genero"].lower()
        ):
            print(libro)

#Usuario:
#registrar_usuario
def registrar_usuario():
    numero_socio = input("numero de socio: ")
    if numero_socio in usuarios:
        print("El usuario ya existe")
        return

    nombre = input("nombre: ")
    usuario = {
        "numero_socio": numero_socio,
        "nombre": nombre,
        "prestamos_activos": []
    }
    usuarios[numero_socio] = usuario
    guardar_datos(catalogo, usuarios, prestamos, ruta)
    print("Usuario agregado")
    return usuarios	

#dar_baja_usuario
def dar_baja_usuario():
    numero_socio = input("numero de socio: ")
    
    if numero_socio not in usuarios:
        print("El usuario no existe")
        return

    if usuarios[numero_socio]["prestamos_activos"]:
        print("El usuario tiene préstamos activos")
        return

    del usuarios[numero_socio]
    guardar_datos(catalogo, usuarios, prestamos, ruta)
    print("Usuario eliminado")

#historial_usuario
def historial_usuario():
    numero_socio = input("numero de socio: ")

    for prestamo in prestamos:
        if prestamo["numero_socio"] == numero_socio:
            print(prestamo)

#registrar_prestamo
def registrar_prestamo():
    numero_socio = input("numero de socio: ")
    if numero_socio not in usuarios:
        print("El usuario no existe")
        return

    isbn = input("isbn: ")
    if isbn not in catalogo:
        print("El libro no existe")
        return

    if catalogo[isbn]["ejemplares_disponibles"] <= 0:
        print("No hay ejemplares disponibles")
        return

    fecha_prestamo = input("fecha del prestamo (dd/mm/aaaa): ")
    fecha_limite = input("fecha limite (dd/mm/aaaa): ") #Queda hacer (fecha_limite = fecha_prestamo + 7 días)(?
    prestamo = {
        "numero_socio": numero_socio,
        "isbn": isbn,
        "fecha_prestamo": fecha_prestamo,
        "fecha_limite": fecha_limite,
        "devuelto": False
    }
    prestamos.append(prestamo)
    usuarios[numero_socio]["prestamos_activos"].append(isbn)
    catalogo[isbn]["ejemplares_disponibles"] -= 1
    guardar_datos(
        catalogo,
        usuarios,
        prestamos,
        ruta
    )
    print("Prestamo registrado")

#registrar_devolucion
def registrar_devolucion():
    numero_socio = input("numero de socio: ")
    isbn = input("isbn: ")
    for prestamo in prestamos:
        if (
            prestamo["numero_socio"] == numero_socio
            and
            prestamo["isbn"] == isbn
            and
            not prestamo["devuelto"]
        ):
            prestamo["devuelto"] = True
            catalogo[isbn]["ejemplares_disponibles"] += 1
            usuarios[numero_socio]["prestamos_activos"].remove(isbn)
            guardar_datos(
                catalogo,
                usuarios,
                prestamos,
                ruta
            )
            print("Devolucion registrada")
            return

    print("Prestamo no encontrado")

#listar_vencidos
def listar_vencidos():
    fecha_actual = input("fecha actual (dd/mm/aaaa): ")
    hay_vencidos = False
    for prestamo in prestamos:
        if (
            prestamo["fecha_limite"] < fecha_actual
            and
            not prestamo["devuelto"]
        ):
            print(prestamo)
            hay_vencidos = True

    if not hay_vencidos:
        print("No hay prestamos vencidos")
        
#normalizar(texto)
def normalizar(texto):
    return texto.lower().strip()

menu_principal()