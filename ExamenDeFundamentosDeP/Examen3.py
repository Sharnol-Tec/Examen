#Datosdeentrada
print("Ingrese el Sexo (H/M):")
sexo = input()
print("Ingrese la EdadSLLB:")
#proceso
edad = int(input())
if edad>=70:
  print("la vacuna es de tipo C")
if sexo=="H":
  edad>=16 and edad<=69
  print("la vacuna es de tipo A")
if sexo=="M":
  edad>=16 and edad<=69
  print("la vacuna es de tipo B")
if edad<=16:
  print("la vacuna es de tipo a")
