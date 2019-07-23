
nombre_usuario = input("¡Hola!¿Cómo te llamas?: ")

print("¡Hola " + nombre_usuario + "!")

estado_de_animo= input("¿Cómo te encuentras hoy?: ")

if estado_de_animo == "contento":
    print ("Me alegro" + " " + nombre_usuario + " " + " hay que ser feliz, pero tampoco vayas restregándolo por ahí, ¿ok?")
elif estado_de_animo == "triste":
    print (nombre_usuario + " " + "no te pongas triste, seguro que todo se solucionará")
elif estado_de_animo == "deprimido":
    print ("Quillo" + " " + nombre_usuario + " " + "no te pongas así por eso, anda, y juégate una partidita a la play o vete al poli a hacer algo de deporte")
elif estado_de_animo == "cansado":
    print ("pos mira," + " " + nombre_usuario + " " + "túmbate un rato y descansa macho, ¿qué quieres que te masajee los pies?")
elif estado_de_animo == "cagao":
    print ("¿Tienes miedo? ¿A quién? Que le parto la cara a quién se meta con mi" + " " + nombre_usuario)
else:
    print ("illo no sé de que me estás hablando, abe.")
