palabra = input("Pon un palindromo: ")
palabraOk = palabra.lower().replace(" ", "") 
palin = palabraOk == palabraOk[::-1]

if palin is True:
    print("TOMAAA ES PALINDROMO")
else:
    print("...no...lo siento no lo es")