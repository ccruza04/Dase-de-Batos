import sqlite3

db_name = 'librosv3.db'

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
    def add_libros(self,libro):

        sql = """INSERT INTO libros (isbn, titulo, autor, editorial, fecha_publicacion)
                    VALUES (?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(sql, (libro[isbn], libro[titulo], libro[autor], libro[editorial], libro[fecha_publicacion]))
            self.conexion.commit()
            print("Libros cadastrados")
        except Exception as e:
            print(f"Error al añadir libro: {e}")
    def delete_libros(self,libro):

    def update_libros(self,libro):

    def get_libros(self,libro):

    def get_all_libros(self,libro):

    def close(self):

if __name__ == '__main__':
    libroDB = libroDB()
    libroDB.add_libros(libroDB)
    libroDB.crear_tablas()