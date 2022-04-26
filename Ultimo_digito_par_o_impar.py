"""Programa para determinar si el ultimo dgito de un numero es Par o Impar"""

print("-------------------------------")
print("---Ultimo digito Par o Impar---")
print("_______________________________")

# input
X=int(input(" Digite un numero: "))
# prossesing
n = X % 10

if n % 2 == 0:
    msj = "Par"
else:
    msj = "Impar"
# ouput
print("el ultimo numero de:",X, "es",n) 
print("Por tanto el ultimo digito de su numero es " + msj)
