Dato_nombre =input("cual es tu nombre   :")
Dato_horas =int(input("cuántas horas planeas estudiar a la semana   :"))
totaldesemanas =int(68)

print(" desde hoy hasta enero del 2028, las horas acumuladas de estudio serán :") 
horasacumuladas = (Dato_horas*totaldesemanas)
print(horasacumuladas)

habilidades = []
usuario = False

while not usuario:
    entrada = input("¿Qué habilidad quieres aprender? (Escribe 'fin' para terminar): ")
    
    if entrada.lower().strip() == "fin":
        usuario = True
    else:
        habilidades.append(entrada)

print("\n--- Tu lista de habilidades ---")
for i, hab in enumerate(habilidades, 1):
    print(f"{i}. {hab}")
    