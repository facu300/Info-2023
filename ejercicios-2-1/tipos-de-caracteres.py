caracter = input("Escriba un caractér: ")
if caracter.isalpha() and caracter.isupper():
    print(f"El caractér {caracter} es una mayúscula")
elif caracter.isalpha():
    print(f"El caractér {caracter} es una minuscula")
elif caracter.isdigit():
    print(f"El caractér {caracter} es un número")
else:
    print(f"El {caracter} es un caractér especial")