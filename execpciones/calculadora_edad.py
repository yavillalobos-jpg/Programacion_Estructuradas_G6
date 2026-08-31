try:
   edad = int(input("Edad: "))
   print("Edad registrada:", edad)
except ValueError:
   print("Ingresar un valor numérico.")