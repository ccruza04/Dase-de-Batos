import sqlite3

db_name = 'librosv3.db'

# Ejemplo de libro válido
libro = {
    "isbn": "99888",
    "titulo": "8765",
    "autor": "Charles Dick",
    "editorial": "Editorial Y",
    "fecha_publicacion": "2024",
    "descripcion": "Libro de prueba"
}

class libroDB:
    def __init__(self):
        self.conexion = sqlite3.connect(db_name)
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            isbn VARCHAR(15) UNIQUE NOT NULL,
            titulo VARCHAR(255) NOT NULL,
            autor VARCHAR(100) NOT NULL,
            editorial VARCHAR(100) NOT NULL,
            fecha_publicacion VARCHAR(100) NOT NULL,
            descripcion TEXT
        )
        ''')
        self.conexion.commit()

    def add_libros(self, libro:dict):
        sql = """INSERT INTO libros (isbn, titulo, autor, editorial, fecha_publicacion, descripcion)
                 VALUES (?, ?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(sql, (
                libro["isbn"],
                libro["titulo"],
                libro["autor"],
                libro["editorial"],
                libro["fecha_publicacion"],
                libro.get("descripcion", None)
            ))
            self.conexion.commit()
            print("Libro añadido correctamente")
        except Exception as e:
            print(f"Error al añadir libro: {e}")

    def delete_libro(self, id:int) -> bool:
        sql = "DELETE FROM libros WHERE id = ?"
        try:
            self.cursor.execute(sql, (id,))
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar libro: {e}")
            return False

    def update_libros(self, id:int, libro:dict):
        sql = """
        UPDATE libros
        SET titulo = ?, autor = ?, editorial = ?, fecha_publicacion = ?, descripcion = ?
        WHERE id = ?
        """
        try:
            self.cursor.execute(sql, (
                libro["titulo"],
                libro["autor"],
                libro["editorial"],
                libro["fecha_publicacion"],
                libro.get("descripcion", None),
                id
            ))
            self.conexion.commit()
            print("Libro actualizado correctamente")
        except Exception as e:
            print(f"Error al actualizar libro: {e}")

    def get_by_isbn(self, isbn):
        self.cursor.execute("SELECT * FROM libros WHERE isbn = ?", (isbn,))
        return self.cursor.fetchone()

    def filter_by_autor(self, autor):
        self.cursor.execute("SELECT * FROM libros WHERE autor = ?", (autor,))
        return self.cursor.fetchall()

    def get_libro(self, id:int) -> dict:
        sql = "SELECT id, isbn, titulo, autor, editorial, fecha_publicacion FROM libros WHERE id = ?"
        self.cursor.execute(sql, (id,))
        libro_dict=dict(self.cursor.fetchone())
        return libro_dict

    def get_all_libros(self) -> list:
        self.cursor.execute("SELECT id, isbn, titulo, autor, editorial, fecha_publicacion, descripcion FROM libros")
        libros=self.cursor.fetchall()
        libros_dict=[dict(libro) for libro in libros]
        return libros_dict

    def close(self):
        self.cursor.close()
        self.conexion.close()


if __name__ == '__main__':
    db = libroDB()
    filtro_autor=db.filter_by_autor("Charles Dick")
    print(f"lalalalal {filtro_autor}")
    db.add_libros(libro)

    # Mostrar cada libro en una línea
    for l in db.get_all_libros():
        print(l)

    db.close()
