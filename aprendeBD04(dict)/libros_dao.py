import sqlite3
import logging

from libros_dao import LibrosDao

db_name = 'librosv3.db'

class LibrosDao:
    logger = logging.getLogger("LibrosDao")
    table_name='libros'
    SELECT = f"""SELECT id, isbn, titulo, autor, editorial"""
    def __init__(self):
        self.conexion = sqlite3.connect(db_name)
        self.conexion.row_factory = sqlite3.Row
        self.cursor = self.conexion.cursor()

        self.crear_tablas()

    def add(self, libro:dict) -> int:
        sql = f"""INSERT INTO {table_name} (isbn, titulo, autor, editorial, fecha_publicacion, descripcion)
                 VALUES (?, ?, ?, ?, ?, ?)"""

        try:
            with self.conn.execute:
            cur = self.conn.execute(sql, (
                libro["isbn"],
                libro["titulo"],
                libro["autor"],
                libro["editorial"],
                libro["fecha_publicacion"],
                libro.get("descripcion", None)
            ))
            self.logger.info(f"Se ha añadido el libro de isbn {libro.get('isbn', None)}")
            return cur.lastrowid
        except Exception as e:
            logging.error(e)
            print(f"Error al añadir libro: {e}")

    def delete_libro(self, id:int) -> bool:
        sql = f"DELETE FROM {table_name} WHERE id = ?"
        try:
            self.cursor.execute(sql, (id,))
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar libro: {e}")
            return False

    def update_libros(self, id:int, libro:dict):
        sql = f"""
        UPDATE {table_name}
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
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE isbn = ?", (isbn,))
        libro=self.cursor.fetchone()
        libro_dict=dict(libro) if libro else None
        return libro_dict

    def filter_by_autor(self, autor):
        libros = self.cursor.execute(f"SELECT * FROM {table_name} WHERE autor = ?", (autor,))
        libros_dict = [dict(libro) for libro in libros]
        return libros_dict

    def get_libro(self, id:int) -> dict:
        try:
            sql = "fSELECT id, isbn, titulo, autor, editorial, fecha_publicacion FROM {table_name} WHERE id = ?"
            self.cursor.execute(sql, (id,))

            libro_dict=dict(self.cursor.fetchone())
        except Exception as e:
            print(f"Error al obtener libro: {e}")
        return libro_dict

    def get_all_libros(self) -> list:
        self.cursor.execute(f"SELECT id, isbn, titulo, autor, editorial, fecha_publicacion, descripcion FROM {table_name}")
        libros=self.cursor.fetchall()
        libros_dict=[dict(libro) for libro in libros]
        return libros_dict

