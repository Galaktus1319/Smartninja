print ("Bienvenido a mi primera calculadora con Python")
user_name = input ("Por favor introduce tu nombre: ")
print ("¡Hola " + user_name + "!")

operation = input ("Introduce la operación que deseas realizar: +, -, *, /: ")

num1 = float(input("introduce la primera cifra"))
num2 = float(input("introduce la segunda cifra"))

if operation == "+":
    print ( num1 + num2 )
elif operation == "-":
    print ( num1 - num2 )
elif operation == "*":
    print ( num1 * num2 )
elif operation == "/":
    print ( num1 / num2 )
else :
    print ("Eyyyy, ¡no has hecho una operación apropiada!")

continuar = input ("¿quieres continuar calculando?: ")

while continuar == "sí":
    operation = input("Introduce la operación que desas realizar: +, -, *, /: ")
    if continuar == "no":
        print ("¡Gracias por usarme!")
        break
    num1 = float(input("introduce la primera cifra"))
    num2 = float(input("introduce la segunda cifra"))

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    else:
        print("Eyyyy, ¡no has hecho una operación apropiada!")
