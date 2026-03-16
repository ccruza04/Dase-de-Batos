import sqlite3
import logging
from database import Database
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    filename="error.log")
if __name__ == '__main__':
    db = Database.connect()
    id = db.add_libros(
        {"isbn": "978-00-00-000001",
         "titulo":"El Quijote",
         "autor":"Cervantes",
         "editorial":"El Quijote",
         "fecha_publicacion":1600}
    )
    if id > 0:
        print("El id es:", id)
        libro = db.get_libro(id)
        print(libro)
    else:
        print("El id no existe")
    # db.add_libros(libro)
    # print(id)
    #
    # # Mostrar cada libro en una línea
    # for l in db.get_all_libros():
    #     print(l)
    #
    # db.close()
