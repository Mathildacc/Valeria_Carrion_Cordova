import os

# Asegurarse que la carpeta logs existe
if not os.path.exists("logs"):
    os.makedirs("logs")

# Crear archivos de prueba
for i in range(1, 6):
    with open(f"logs/archivo{i}.log", "w") as f:
        f.write(f"Este es el contenido del archivo {i}")

# Ruta donde se encuentran los archivos de log
ruta = "./logs"   # Puedes cambiar esta ruta según tu carpeta
nombre_base = "nombre_apellido"

# Listar los archivos de la carpeta
archivos = [f for f in os.listdir(ruta) if f.endswith(".log")]

# Enumerar y renombrar
contador = 1
for archivo in archivos:
    nuevo_nombre = f"{nombre_base}_{contador}.log"
    ruta_original = os.path.join(ruta, archivo)
    ruta_nueva = os.path.join(ruta, nuevo_nombre)
    
    os.rename(ruta_original, ruta_nueva)
    print(f"Renombrado: {archivo} -> {nuevo_nombre}")
    contador += 1