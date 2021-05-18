from diccionario import diccionario
import random
from quitar_tildes import quitar_tildes
import string

palabra = random.choice(diccionario)
palabra_sin_tildes = quitar_tildes(palabra)
vidas = 10
letras_usadas = set()
respuesta = set()
print(palabra)

while respuesta != set(palabra_sin_tildes) and vidas > 0:
    print('Vidas:', vidas)
    for letra in palabra_sin_tildes:
        palabra_escondida = ""
        if letra in respuesta:
            palabra_escondida += letra
        else:
            palabra_escondida += "_"
        print(palabra_escondida, end=" ")
    letra_usuario = input('\nIngresa una letra: ')
    while len(letra_usuario) > 1:
        letra_usuario = input('\nUna sola letra, por favor: ')
    while letra_usuario not in string.ascii_lowercase:
        letra_usuario = input('\nNo es una letra: ')
    letras_usadas.add(letra_usuario)
    print('Has usado estas letras: ', ', '.join(sorted(letras_usadas)), '\n')
    if letra_usuario in palabra_sin_tildes:
        respuesta.add(letra_usuario)
    else:
        vidas -= 1

if not vidas:
    print('Has perdido, la palabra era:', palabra.upper())
else:
    print('\n****** Ganaste! La palabra es:', palabra.upper(), '******')






