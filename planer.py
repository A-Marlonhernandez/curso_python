import json

# 1. Función para cargar habilidades guardadas previamente
def cargar_habilidades():
    try:
        with open("habilidades.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# 2. Función para guardar la lista actualizada en el disco
def guardar_habilidades(lista):
    with open("habilidades.json", "w") as archivo:
        json.dump(lista, archivo, indent=4)

# --- INICIO DEL PROGRAMA ---
Dato_nombre = input("¿Cuál es tu nombre?: ")
Dato_horas = int(input("¿Cuántas horas planeas estudiar a la semana?: "))
totaldesemanas = 68

horasacumuladas = Dato_horas * totaldesemanas
print(f"\n{Dato_nombre}, desde hoy hasta enero de 2028, tus horas acumuladas serán: {horasacumuladas} hrs\n")

# Cargar datos existentes
habilidades = cargar_habilidades()

if habilidades:
    print(f"Habilidades registradas anteriormente: {', '.join(habilidades)}")
else:
    print("No hay habilidades registradas aún.")

# Bucle para agregar nuevas habilidades
while True:
    entrada = input("\n¿Qué habilidad quieres aprender? (Escribe 'fin' para terminar): ").strip()
    
    if entrada.lower() == "fin":
        break
    
    if entrada and entrada not in habilidades:
        habilidades.append(entrada)
        print(f"-> '{entrada}' agregada a la lista.")

# Guardar los cambios automáticamente
guardar_habilidades(habilidades)
print(f"\n¡Lista final guardada con éxito en 'habilidades.json'! ({len(habilidades)} habilidades en total)")
    