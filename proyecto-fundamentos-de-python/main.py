from readchar import readkey
import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def teclado_reactivo():
    limite = 50
    counter = 0
    while counter <= limite:
        tecla_presionada = readkey()
        if tecla_presionada == 'n':
            limpiar_terminal()
            print(counter)
            counter += 1
teclado_reactivo()

