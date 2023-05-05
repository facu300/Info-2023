texto = input("Ingrese un texto, una frase o un articulo cualquiera: ")
letras = input("Ingrese tres letras: ")
texto = texto.lower()
texto_en_lista = texto.split(" ")
lista_de_letras = list(letras.lower())
letra1 = 0
letra2 = 0
letra3 = 0
for letras_en_texto in texto:
    if letras_en_texto == lista_de_letras[0]:
        letra1 += 1 
    elif letras_en_texto == lista_de_letras[1]:
        letra2 += 1   
    elif letras_en_texto == lista_de_letras[2]:
        letra3 += 1
print(f"la letra {lista_de_letras[0]} se repite {letra1}")
print(f"la letra {lista_de_letras[1]} se repite {letra2}")
print(f"la letra {lista_de_letras[2]} se repite {letra3}")

print(f"Su texto tiene {len(texto_en_lista)} palabras")

if texto[-1] == ".":
    print(f"la primera letra es la {texto[0]} y la ultima {texto[-2]}")
else:
    print(f"la primera letra es la {texto[0]} y la ultima {texto[-1]}")

print(f"Tu texto al reves es: {texto[::-1]}")

if "python" in texto:
    print("Continene la palabra python")
else:
    print("No contiene la palabra python")


    
    
    


