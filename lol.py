import sqlite3
from faker import Faker
import random

# Inicializar Faker en español (opcional)
fake = Faker("es_ES")

# Conexión a la base de datos
conexion = sqlite3.connect("libros.db")
cursor = conexion.cursor()

# Función para generar un título más "literario"
def generar_titulo():
    palabras = fake.words(nb=random.randint(2, 5))
    titulo = " ".join(palabras).title()
    return titulo

# Insertar 1000 libros autogenerados
for _ in range(1000000):
    isbn = fake.isbn13(separator="-")
    titulo = generar_titulo()
    autor = fake.name()
    editorial = fake.company()
    fecha_publicacion = fake.date_between(start_date="-50y", end_date="today").isoformat()
    descripcion = fake.paragraph(nb_sentences=5)

    try:
        cursor.execute("""
            INSERT INTO libros (isbn, titulo, autor, editorial, fecha_publicacion, descripcion)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (isbn, titulo, autor, editorial, fecha_publicacion, descripcion))
    except sqlite3.IntegrityError:
        # Si se repite el ISBN, generamos otro y repetimos
        continue

conexion.commit()
conexion.close()

print("Se han insertado 1000 libros autogenerados correctamente.")
