fecha_de_nacimiento = input('Fecha de Nacimiento en formato dd/mm/aaaa ')
fecha_actual = '28/04/2023'
lista_1= fecha_de_nacimiento.split("/")
lista_2 = fecha_actual.split("/")
edad = int(lista_2[2]) - int(lista_1[2])
print(f"su edad es {edad}")