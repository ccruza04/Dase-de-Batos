import sqlite3
import logging
from database import Database

if __name__ == '__main__':
    db = Database.connect()
    id = db.add_libros(
        {"isbn": "978-00-00-000001",
         "titulo":"El Quijote",
         "autor":"Cervantes",
         "editorial":"El Quijote",
         "fecha_publicacion":1600}
    )
    db.add_libros(libro)
    print(id)

    # Mostrar cada libro en una línea
    for l in db.get_all_libros():
        print(l)

    db.close()
