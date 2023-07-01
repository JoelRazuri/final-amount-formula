""" 
Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa
de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula
a utilizar es:

𝐶𝑛 = 𝐶 × (1 + 𝑥/100) ** 𝑛

Donde 𝐶 es el capital inicial, 𝑥 es la tasa de interés y 𝑛 es el número de años a calcular.
"""

cant_pesos= float(input("Ingrese la cantidad de pesos:"))
tasa_interes=int(input("Ingrese la tasa de interes:"))
años=int(input("Ingrese el numero de años:"))

monto_final= cant_pesos * ((1 + tasa_interes/100)**años)

print("---------------------------------------------------------")
print(f"Capital inicial: ${cant_pesos}\nTasa de interes: {tasa_interes}%\nAños: {años}")
print("")
print(f"El monto final es : ${monto_final}")

