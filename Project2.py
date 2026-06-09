#Trabajo en equipo 
"""
#Libro:

Cada libro se representa como un diccionario con las siguientes claves:
• isbn: string único que identifica al libro.
• titulo: string con el título del libro.
• autor: string con el autor del libro.
• genero: string con el género del libro.
• ejemplares_totales: entero que indica la cantidad total de ejemplares
• ejemplares_disponibles: enteros que indican la cantidad de ejemplares
disponibles para préstamo.

Ejemplo: { “isbn”: “978-1”, “titulo”: “Cien años de soledad”,
 “autor”: “García Márquez”, “genero”: “Novela”,
 “ejemplares_totales”: 2, “ejemplares_disponibles”: 2 }
 """
def agregar_libro(catalogo, isbn, titulo, autor, genero, 
ejemplares):
    if isbn in Catalogo:
        print("El isbn ya existe")
    Catalogo = {
        "isbn" : none,
        "titulo" : none,
        "autor" : none,
        "genero" : none,
        "ejemplares_totales" : none,
        "ejemplares_disponibles" : none
        }

"""
#Usuario:

Cada usuario se representa como un diccionario con las siguientes claves:
{ “isbn”: “978-1”, “titulo”: “Cien años de soledad”,
 “autor”: “García Márquez”, “genero”: “Novela”,
 “ejemplares_totales”: 2, “ejemplares_disponibles”: 2 }
• numero_socio: entero que identifica al usuario.
• nombre: string con el nombre completo.
• prestamos_activos: lista de ISBNs de libros prestados actualmente al
usuario.

Ejemplo: { “numero_socio”: 1, “nombre”: “Ana García”,
 “prestamos_activos”: [“978-1”] }
"""
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

Observación: toda operación que modifique el estado del sistema debe quedar
persistida en el archivo correspondiente.
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