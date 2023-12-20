from readchar import readkey, key
import os

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""


def limpiar_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')


def printTablero(tablero: list):
  limpiar_terminal()
  for fila in tablero:
    string = ''.join(fila)
    print(string)


def coordenadasTablero(tablero: list):
  coordenada_inicial = (0, 0)
  coordenada_final = (len(tablero) - 1, len(tablero[0]) - 1)
  return coordenada_inicial, coordenada_final


def limiteCharacter(lista, x, y):
  return lista[x][y] != '#'


def limitesCordenadas(x: int, y: int, lista: list):
  coordenada_inicial, coordenada_final = coordenadasTablero(lista)
  if x < coordenada_inicial[0] or y < coordenada_inicial[1]:
    return False
  elif x == coordenada_final[0] and y == coordenada_final[1]:
    return limiteCharacter(lista, x, y)
  elif x > coordenada_final[0] or y > coordenada_final[1]:
    return False
  else:
    return limiteCharacter(lista, x, y)


def changeTablero(
    tecla_presionada: str, 
    laberinto_list: list, 
    px: int,
    py: int, 
    previous_key: str
):
  if (tecla_presionada == key.DOWN and limitesCordenadas(px + 1, py, laberinto_list)):
    laberinto_list[px][py] = previous_key
    previous_key = laberinto_list[px + 1][py]
    laberinto_list[px + 1][py] = 'P'
    px += 1
    return laberinto_list, px, py, previous_key
  elif (tecla_presionada == key.UP and limitesCordenadas(px - 1, py, laberinto_list)):
    laberinto_list[px][py] = previous_key
    previous_key = laberinto_list[px - 1][py]
    laberinto_list[px - 1][py] = 'P'
    px -= 1
    return laberinto_list, px, py, previous_key
  elif (tecla_presionada == key.LEFT and limitesCordenadas(px, py - 1, laberinto_list)):
    laberinto_list[px][py] = previous_key
    previous_key = laberinto_list[px][py - 1]
    laberinto_list[px][py - 1] = 'P'
    py -= 1
    return laberinto_list, px, py, previous_key
  elif (tecla_presionada == key.RIGHT and limitesCordenadas(px, py + 1, laberinto_list)):
    laberinto_list[px][py] = previous_key
    previous_key = laberinto_list[px][py + 1]
    laberinto_list[px][py + 1] = 'P'
    py += 1
    return laberinto_list, px, py, previous_key
  else:
    return laberinto_list, px, py, previous_key


def tableroGame(tablero: str):
  laberinto_list = tablero.split('\n')
  laberinto_list = [list(fila) for fila in laberinto_list]
  coordenada_inicial = coordenadasTablero(laberinto_list)
  px, py = coordenada_inicial
  previous_key = laberinto_list[px][py]
  laberinto_list[px][py] = 'P'
  printTablero(laberinto_list)
  while True:
    tecla_presionada = readkey()
    laberinto_list, px, py, previous_key = changeTablero(
        tecla_presionada, laberinto_list, px, py, previous_key)
    printTablero(laberinto_list)


tableroGame(laberinto)

