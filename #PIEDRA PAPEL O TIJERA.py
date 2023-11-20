#PIEDRA PAPEL O TIJERA
print ("¿te atreves a jugar PIEDRA, PAPEL o TIJERA contra LA MATRIX?")

import random

opciones = ("piedra", "papel", "tijera")
jugar = True

while jugar: 
    player1 = 0 
    matrix = random.choice (opciones)

    while player1 not in opciones:
        player1 = input ("Elegi una opción (piedra, papel o tijera): ")

    print (f"Player1: {player1}")
    print (f"La Matrix: {matrix} ")

    if player1 == matrix:
        print ('¡JUEGO EMPATADO!')
    elif player1 == "piedra" and matrix == "tijera":
        print ('¡LE GANASTE A LA MATRIX!')
    elif player1 == 'papel' and matrix == "piedra":
        print ('¡LE GANASTE A LA MATRIX!')
    elif player1 == 'tijera' and matrix == "papel":
        print ('¡LE GANASTE A LA MATRIX!')
    else:
        print ("¡PERDISTE!")
    if not input ('¿Queres jugar de nuevo? (si/no): ').lower () == 'si':
        jugar = False
print ("¡Gracias por jugar! ¡Espero que te hayas divertido!")

