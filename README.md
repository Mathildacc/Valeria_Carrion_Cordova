# Proyecto de Renombrado de Archivos de Log

Este proyecto tiene como objetivo renombrar archivos de log en una carpeta específica. El script en Python proporcionado (`codigo.py`) busca archivos con la extensión `.log` en la carpeta `logs` y los renombra siguiendo un formato específico.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- **logs/**: Carpeta que contiene los archivos de log.
  - `archivo1.log`: Este archivo es un archivo de log de ejemplo que puede contener información de registro.
  - `archivo2.log`: Este archivo es otro archivo de log de ejemplo, similar al anterior.
  - `archivo3.log`: Este archivo también es un archivo de log de ejemplo.
  - `archivo4.log`: Este archivo es un cuarto archivo de log de ejemplo.
  - `archivo5.log`: Este archivo es un quinto archivo de log de ejemplo.
  
- **codigo.py**: Este archivo contiene el código en Python que renombra los archivos de log en la carpeta `logs`.

## Uso

1. Asegúrate de tener Python instalado en tu sistema.
2. Coloca los archivos de log en la carpeta `logs`.
3. Ejecuta el script `codigo.py` para renombrar los archivos de log.
4. Los archivos renombrados seguirán el formato `nombre_apellido_1.log`, `nombre_apellido_2.log`, etc.

## Notas

- Puedes modificar la variable `nombre_base` en `codigo.py` para cambiar el prefijo de los archivos renombrados.
- Asegúrate de que no haya conflictos de nombres al ejecutar el script.