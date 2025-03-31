# Diccionario en Python para representar información estructurada

# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Dayana",
    "edad": 30,
    "ciudad": "Otavalo",
    "profesion": "Arquitecta"
}

# Acceder y modificar el valor de 'ciudad'
informacion_personal["ciudad"] = "Ibarra"

# Agregar una nueva clave
informacion_personal["profesion"] = "Contadora"

# Verificar si 'telefono' existe en el diccionario, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987620012"

# Eliminar la clave 'edad'
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
