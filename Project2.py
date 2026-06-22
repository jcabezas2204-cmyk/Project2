#Trabajo en equipo 
catalogo={}
prestamos=[]
usuarios={}
#Libro:
#agregar libro
def agregar_libro(catalogo, isbn, titulo, autor, genero, ejemplares):
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

    catalogo[isbn] = libro
    print("Libro agregado")
    return catalogo

#eliminar_libro
def eliminar_libro(catalogo, prestamos, isbn):
    pass

#buscar_libro
def buscar_libro(catalogo, termino):
    pass

#Usuario:
#registrar_usuario
def registrar_usuario(usuarios, numero_socio, nombre):
    diccUsuario={
    "numero_socio": input("numero de socio: "),
    "nombre": input("nombre: "),
    "prestamos_activos": []
    }
    pass

#dar_baja_usuario
def dar_baja_usuario(usuarios, prestamos, 
numero_socio):
    pass

#historial_usuario
def historial_usuario(prestamos, numero_socio):
    pass
"""
#Préstamo:

Cada préstamo se representa como un diccionario con las siguientes claves:
• numero_socio: identifica al usuario que realizó el préstamo.
• isbn: identifica el libro prestado.
• fecha_prestamo: string que representa la fecha del préstamo.
• fecha_limite: string que representa la fecha máxima de devolución del libro.
Es la fecha_prestamo más 7 días.
• devuelto: booleano que indica si el libro ya fue devuelto.

Ejemplo: { “numero_socio”: 1, “isbn”: “978-1”,
 “fecha_prestamo”: ”02/06/2026”,
 “fecha_limite”: “09/06/2026”, “devuelto”: False }
 """
#registrar_prestamo
def registrar_prestamo(catalogo, usuarios, prestamos, 
numero_socio, isbn, fecha_prestamo):
    pass
    
#registrar_devolucion
def registrar_devolucion(catalogo, prestamos, 
numero_socio, isbn):
    pass
    
#listar_vencidos
def listar_vencidos(prestamos, fecha_actual):
    pass

"""
#Estructuras globales:

El estado completo del sistema se mantiene en tres estructuras, que se pasan como
parámetro en cada función:
• catalogo: diccionario cuya clave es el ISBN y cuyo valor es el diccionario del
libro.
• usuarios: diccionario cuya clave es el número de socio y cuyo valor es el
diccionario del usuario.
• prestamos: lista de diccionarios, donde cada uno corresponde a un préstamo
registrado
"""
"""
#Bonus (opcional):

Dado un número de socio, el sistema debe analizar el historial de préstamos del
usuario, identificar los géneros que más ha leído y retornar una lista de libros
disponibles que sean de esos géneros y que no los haya tomado prestado
anteriormente.
La función debe llamarse recomendar_libros(catalogo, prestamos,
numero_socio, n) y retornar una lista con hasta n libros recomendados, ordenados
por ejemplares disponibles de mayor a menor.
"""
#guardar_datos
def guardar_datos(catalogo, usuarios, prestamos, ruta):
    pass
    
#cargar_datos(ruta)
def cargar_datos(ruta):
    pass
    
#normalizar(texto)
def normalizar(texto):
    pass
