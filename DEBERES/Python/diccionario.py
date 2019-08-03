import random
import json
import datetime


secreto = random.randint(1, 50)
pregunta = 0
intentos= 0
usuario= input("¿Nombre?: ")
listafallos= []

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

while pregunta != secreto:
    pregunta = int(input("¿Cual es el número en el que estoy pensando? (entre 1 y 50): "))
    intentos += 1

    if pregunta == secreto:

        with open("score_list.txt", "w") as score_file:
            score_list.append({"Usuario": usuario, "Intentos": intentos, "Fecha": str(datetime.datetime.now()), "Fallos": listafallos, "Respuesta": secreto})
            score_file.write(json.dumps(score_list))
            print(score_list[:3])
        print("¡Ole, lo adivinaste!")

    elif pregunta > secreto:
        print("Tu respuesta no es correcta intenta algo menor")
        listafallos.append(pregunta)
    elif pregunta < secreto:
        print("Tu respuesta no es correcta intenta algo mayor")
        listafallos.append(pregunta)
    else
         print ("¿qué estás escribiendo?")