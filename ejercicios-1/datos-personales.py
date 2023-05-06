datos_personales = input("Nombre: , Edad: , Ciudad de residencia")
nombre, edad, ciudad_de_residencia = datos_personales.split(",")
print(f'''
      Nombre: {nombre} 
      Edad: {edad} 
      Ciudad de residencia: {ciudad_de_residencia}''')