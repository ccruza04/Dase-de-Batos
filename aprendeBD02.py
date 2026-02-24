import sqlite3

DATABASE_NAME = 'libros.db'
conexion = sqlite3.connect(DATABASE_NAME)
cursor = conexion.cursor()
isbn =input('Ingrese ISBN: ')
titulo = input('Ingrese titulo: ')
autor = input('Ingrese autor: ')
editorial = input('Ingrese editorial: ')
fecha_publicacion = input('Ingrese fecha_publicacion: ')

cursor.execute('''
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
sql = """INSERT INTO libros (isbn, titulo, autor, editorial, fecha_publicacion)
            VALUES (?, ?, ?, ?, ?)"""

try:
    cursor.execute(sql, (isbn, titulo, autor, editorial, fecha_publicacion) )
    conexion.commit()
    print("Libros cadastrados")
except Exception as e:
    print(f"Error al añadir libro: {e}")

# SELECT de todos los libros
cursor.execute("SELECT id, isbn, titulo, autor, editorial, fecha_publicacion, descripcion FROM libros")
libros = cursor.fetchall()

# Mostrar resultados
for libro in libros:
    print(libro)

for libro in libros:
    print(libro[0], libro[1], libro[2])

cursor.close()
conexion.close()
