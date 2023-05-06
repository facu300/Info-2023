nombre = 10
bienvenida = f"Hola {nombre} como estas"
print("juan" in bienvenida)
#operadores de pertenencia (in / not in)

lista = [1,2,3]
lista.sort() #se utiliza para ordenar una lista
lista.reverse() # cambia el orden al reves de la lista
lista.append(4) # agregar elemento a la lista 
lista.pop() # elimina el ultimo elemento o el del indice indicado
lista.remove() # elimina el elemento que seleciono,saca por valor

# para cambiar un valor en una tupla primero convertirlo en lista con list()


#estructuras de control
#estructuras condicionales
a = 2
b = 2
#if(a==b):
 #   print("b y a son iguales")

#estructuras repetitivas
# repetitivas con contador, rep. con condicional a priori
#for X in range (1, 10): # con contador
 #   print(x)

#for X in "hola como estas":
   # print(x)
    
#a = 0
#while(a!=10)
#print(a) # para detener un programa q no para es crl + c


tupla = ([1, 2], 4, 5)
tupla[0].append(31) #para ingresar un elemento a una lista dentro de una tupla
tupla[0].pop(1)# para sacar un elemento de la lista dentro de tupla
tupla[0][0]= 44 #para modificar un elemento de la lista dentro de la tupla
print(tupla)

#lista[-1] para ingresar al ultimo elemento de la lista