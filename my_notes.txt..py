#Escritura del archivo my_notes.txt:
# Abre el archivo en modo escritura y se asegura de que se cierre automáticamente
with open('my_notes.txt', 'w') as file:
    file.write("Esta es mi primera nota.\n")
    file.write("Me gusta aprender Python.\n")
    file.write("Estoy practicando manejo de archivos.\n")

# No es necesario llamar a file.close() ya que el bloque 'with' lo cierra automáticamente.

#Lectura del archivo my_notes.txt:
# Abre el archivo en modo lectura y se asegura de que se cierre automáticamente
with open('my_notes.txt', 'r') as file:
    linea = file.readline()
    while linea:
        print(linea.strip())  # Imprime cada línea sin saltos de línea adicionales
        linea = file.readline()

# El archivo se cierra automáticamente al salir del bloque 'with'.
