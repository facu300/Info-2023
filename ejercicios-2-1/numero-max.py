numero_1 = int(input("Escriba un número: "))
numero_2 = int(input("Escriba otro número: "))
numero_3 = int(input("Escriba otro número: "))
if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"El número {numero_1} es mayor que {numero_2} y {numero_3}")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"El número {numero_2} es mayor que {numero_1} y {numero_3}")
elif numero_3 > numero_1 and numero_3 > numero_2:
    print(f"El número {numero_3} es mayor que {numero_1} y {numero_2}")
elif numero_1 == numero_2 and numero_2 > numero_3:
    print(f"{numero_1} y {numero_2} son mayores que {numero_3}")
elif numero_1 == numero_3 and numero_1 > numero_2:
    print(f"{numero_1} y {numero_3} son mayores que {numero_2}")
elif numero_2 == numero_3 and numero_2 > numero_1:
    print(f"{numero_2} y {numero_3} son mayores que {numero_1}")
else:
    print("Los tres numeros son iguales")
    

