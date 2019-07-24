import random

secreto = random.randint(1, 30)
pregunta = 0


while pregunta != secreto:
    pregunta = int(input("¿Cual es el número en el que estoy pensando? (entre 1 y 50): "))

    if pregunta == secreto:
        print("¡Ole, lo adivinaste!")
    elif pregunta > secreto:
        print("Tu respuesta no es correcta intenta algo menor")
    elif pregunta < secreto:
        print("Tu respuesta no es correcta intenta algo mayor")