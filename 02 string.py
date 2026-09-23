usuario_quiere_salir = False
while not usuario_quiere_salir:
 print("Confirma que no eres un robot")
 respuesta = input("si eres un humano escribe- no  :")

 if respuesta == "no"  :
    usuario_quiere_salir = True
    print(" Has salido del bucle")

