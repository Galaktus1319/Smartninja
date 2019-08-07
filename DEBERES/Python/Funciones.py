
#Ejercicio 12.1

def funcionsuma (num1, num2):
    suma = num1 + num2
    return suma

print (funcionsuma(12,14))
print (funcionsuma(520,1928))



#Ejercicio 12.2 mejorando el juego del número secreto con funciones

import random
import json
import datetime

def nivel():
    preguntanivel = input ("¿Qué nivel quieres A)Fácil o B)Difícil?: ")
    if preguntanivel == "A":
        jugarpartida()

    if preguntanivel == "B":
        partidadificil()

def partidadificil():
    secreto = random.randint(1, 50)
    pregunta = 0
    intentos = 0
    listafallos = []
    score_list = []
    usuario = input("¿Nombre?: ")



    while pregunta != secreto:
        pregunta = int(input("¿Cual es el número en el que estoy pensando? (entre 1 y 50): "))
        intentos += 1

        if pregunta == secreto:

            with open("score_list.txt", "w") as score_file:
                score_list.append({"Usuario": usuario, "Intentos": intentos, "Fecha": str(datetime.datetime.now()),
                                   "Fallos": listafallos, "Respuesta": secreto})
                score_file.write(json.dumps(score_list))
                print(score_list[:3])
            print("¡Ole, lo adivinaste!")

        if intentos == 3:
            print ("Lo siento has excedido el número de intentos...")
            break

        else:
            print("Fallaste")


def jugarpartida():
    secreto = random.randint(1, 50)
    pregunta = 0
    intentos = 0
    usuario = input("¿Nombre?: ")
    listafallos = []
    score_list = []

    while pregunta != secreto:
        pregunta = int(input("¿Cual es el número en el que estoy pensando? (entre 1 y 50): "))
        intentos += 1

        if pregunta == secreto:

            with open("score_list.txt", "w") as score_file:
                score_list.append({"Usuario": usuario, "Intentos": intentos, "Fecha": str(datetime.datetime.now()),
                                   "Fallos": listafallos, "Respuesta": secreto})
                score_file.write(json.dumps(score_list))
                print(score_list[:3])
            print("¡Ole, lo adivinaste!")

        elif pregunta > secreto:
            print("Tu respuesta no es correcta intenta algo menor")
            listafallos.append(pregunta)
        elif pregunta < secreto:
            print("Tu respuesta no es correcta intenta algo mayor")
            listafallos.append(pregunta)
        else:
            print("¿qué estás escribiendo?")

def verscores():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        print("Top scores: " + str(score_list))

def vertopscores():
    score_list = verscores()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list


while True:
    eleccion = input("Quieres A) jugar una nueva partida, B) ver las puntuaciones, o C) salir?")

    if eleccion == "A":
        nivel()
    elif eleccion == "B":
        for score_dict in vertopscores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break


