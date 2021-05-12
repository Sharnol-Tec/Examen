#datos de entrada
PrimeraUnidadSLLB=float(input("Ingrese la nota de la PrimeraUnidadSLLB:  "))
SegundaUnidadSLLB=float(input("Ingrese la nota de la SegundaUnidadSLLB:  "))
TerceraUnidadSLLB=float(input("Ingrese la nota de la TerceraUnidadSLLB:  "))
TrabajoFinalSLLB=float(input("Ingrese la nota del TrabajoFinalSLLB:    "))
#proceso
nota=PrimeraUnidadSLLB*0.2 + SegundaUnidadSLLB*0.15 + TerceraUnidadSLLB*0.15 + TrabajoFinalSLLB*0.5
#salida
print("nota final del estudiante es:",nota)