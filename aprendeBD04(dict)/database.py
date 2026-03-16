import sqlite3
import logging
db_name = 'librosv3.db'
class Database:
    logger = logging.getLogger("Database")

    _conn = None
    _dbname = db_name
    def __new__(cls):
            raise TypeError("Database es un singleton")

    @classmethod
    def _create_table(cls):
        cursor = cls._conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    isbn VARCHAR(25) UNIQUE NOT NULL,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(100) NOT NULL,
                    editorial VARCHAR(100) NOT NULL,
                    fecha_publicacion VARCHAR(100) NOT NULL,
                    descripcion TEXT
                )
                ''')
        conexion.commit()

    @classmethod
    def connect(cls):
        if cls._conn is None:
            cls._conn = sqlite3.connect(cls._db_name)
            cls._conn.row_factory = sqlite3.Row
        with cls._conn:
            cursor = cls._conn.cursor()
            cursor.execute("PRAGMA foreing_keys = ON")
        return cls._conn.cursor()

    @classmethod
    def close(cls):
        pass

    def close(self):
        self.cursor.close()
        self.conexion.close()