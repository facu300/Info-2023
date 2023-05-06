radio_de_un_circulo = input("Ingrese el Radio de un Circulo")
pi = 3.14159
diametro_de_un_circulo = 2 * int(radio_de_un_circulo)
circunferencia_de_un_circulo = pi * int(diametro_de_un_circulo)
area_de_un_circulo = pi * int(radio_de_un_circulo) ** 2
print(f"El diametro del circulo es {diametro_de_un_circulo}")
print(f"La circunferencia del circulo es {round(circunferencia_de_un_circulo)}")
print(f"El area del circulo es {round(area_de_un_circulo)}")