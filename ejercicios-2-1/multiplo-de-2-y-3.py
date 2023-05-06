numero = int(input("Escriba un número: "))
multiplo_de_2 = numero % 2
multiplo_de_3 = numero % 3
if multiplo_de_2 == 0 and multiplo_de_3 == 0:
    print(f"el {numero} es multiplo de 2 y de 3")
else: 
    print(f"el {numero} no es multiplo de 2 y de 3")