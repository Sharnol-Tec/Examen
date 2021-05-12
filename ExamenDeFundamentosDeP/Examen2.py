#datos de entrada
puntos = float (input ('Ingresa el valor de puntosSLLB: '))
salario_minimo = float (input ('Ingresa el valor de salario minimoSLLB: '))
#proceso
bono=0
if puntos>=50 and puntos<=100:
    bono=salario_minimo*0.1
if puntos>101 and puntos<=150:
    bono=salario_minimo*0.4
if puntos>151:
    bono=salario_minimo*0.7
#salida   
print ('Valor de bonoSLLB: ' + repr (bono))
print ()