usuario_quiere_salir = False
while not usuario_quiere_salir:
 Num = float(input("escribe un numero mayor a 10 si eres un humano   :"))
    
 if Num>10:
   print("Si eres un humano, saliste del bucle  ")
   usuario_quiere_salir = True 


 else:
  print("Escribe un numero mayor a 10.Inténtalo de nuevo")



 