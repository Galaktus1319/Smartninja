import json

with open("adn.txt", "r") as adn:
    adn = json.loads(adn.read())

inputadn = input ("Introduce la cadena de adn: ")

if inputadn == "CCAGCAATCGC" in adn:
    print ("pelo negro")

if inputadn == "GCCAGTGCCG" in adn:
    print ("pelo marron")

if inputadn == "TTAGCTATCGC" in adn:
    print ("pelo rubio")

if inputadn == "TTGTGGTGGC" in adn:
    print ("ojos azules")

if inputadn == "GGGAGGTGGC" in adn:
    print ("ojos verdes")

if inputadn == "AAGTAGTGAC" in adn:
    print ("ojos marrones")

if inputadn == "GCCACGG" in adn:
    print("cara cuadrada")

if inputadn == "ACCACAA" in adn:
    print ("cara redonda")

if inputadn == "AGGCCTCA" in adn:
    print ("cara ovalada")

if inputadn == "TGAAGGACCTTC" in adn:
    print ("mujer")

if inputadn == "TGCAGGAACTTC" in adn:
    print ("hombre")

if inputadn == "AAAACCTCA" in adn:
    print ("raza blanca")

if inputadn == "CGACTACAG" in adn:
    print ("raza negra")

if inputadn == "CGCGGGCCG" in adn:
    print ("raza asiatica")
