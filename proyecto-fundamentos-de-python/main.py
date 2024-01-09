from copy import deepcopy
import random
from readchar import readkey, key
import os

class DataJugador:
  def dataJugador(self):
    print('Bienvenido al juego guerrero, tu mision es atravesar el campo de batalla')
    print('Debes llegar hasta la puerta de salida del campo de batalla')
    print('La puerta esta ubicada en la ultima fila')
    nombre_jugador_juego = input('Ingresa tu nombre: ')
    ficha = input(f'Ingresa la ficha con la que deseas jugar {nombre_jugador_juego}: ')
    return (nombre_jugador_juego,ficha)

class LeerMapa:
  TABLEROS_DIR = 'tableros/'

  def __init__(self):
    self.coordenada_inicial_x = None
    self.coordenada_inicial_y = None
    self.coordenada_x_final_juego = None
    self.coordenada_y_final_juego = None
    self.laberinto_list = None
    self.coordenada_final_x = None
    self.coordenada_final_y = None
    self._cargar_mapa()

  def _cargar_mapa(self):
    listas_mapas = random.choice(os.listdir(self.TABLEROS_DIR))
    ruta = os.path.join(self.TABLEROS_DIR, listas_mapas)

    with open(ruta, 'r', encoding='utf-8') as archivo:
      primera_linea = next(archivo)
      posicion_x, posicion_y, final_x, final_y = map(int,primera_linea.split())
      mapa = [list(linea.rstrip()) for linea in archivo]

      # inicializando atributos de clase
      self.coordenada_inicial_x = posicion_y
      self.coordenada_inicial_y = posicion_x
      self.coordenada_x_final_juego = final_y
      self.coordenada_y_final_juego = final_x
      self.laberinto_list = mapa
      self.coordenada_final_x = len(mapa) - 1
      self.coordenada_final_y = len(mapa[0]) - 1

  def obtener_datos_mapa(self):
    self._cargar_mapa()
    return (self.coordenada_inicial_x, self.coordenada_inicial_y,
            self.coordenada_x_final_juego, self.coordenada_y_final_juego,
            self.laberinto_list, self.coordenada_final_x,
            self.coordenada_final_y)

class ImprimirTablero:
  def limpiarTerminal(self):
    os.system('cls' if os.name == 'nt' else 'clear')

  def printTablero(self,tablero):
    self.limpiarTerminal()
    for fila in tablero:
      string = ' '.join(fila)
      print(string)

class LogicaJuego:
  PARED = '#'
  def __init__(
    self,
    laberinto,
    limite_tablero_x,
    limite_tablero_y,
    ficha,
    coordenada_x_final_juego,
    coordenada_y_final_juego,
    coordenada_inicial_x,
    coordenada_inicial_y
  ):
    self.laberinto = laberinto
    self.limite_tablero_x = limite_tablero_x
    self.limite_tablero_y = limite_tablero_y
    self.ficha = ficha
    self.coordenada_x_final_juego = coordenada_x_final_juego
    self.coordenada_y_final_juego = coordenada_y_final_juego
    self.x = coordenada_inicial_x
    self.y = coordenada_inicial_y

  def ponerFichaInicialTablero(self):
    nuevo_laberinto = deepcopy(self.laberinto)
    nuevo_laberinto[self.x][self.y] = self.ficha
    return nuevo_laberinto
  
  def limitePared(self, x: int, y: int):
    return self.laberinto[x][y] != self.PARED

  def limitesCoordenadas(self, x: int, y: int):
    if x < 0 or y < 0:
      return False
    elif x <= self.limite_tablero_x and y <= self.limite_tablero_y:
      return self.limitePared(x, y)
    elif x > self.limite_tablero_x or y > self.limite_tablero_y:
      return False

  def changeTablero(self, tecla_presionada: str):
    movimientos = {
        key.DOWN: (1, 0),
        key.UP: (-1, 0),
        key.LEFT: (0, -1),
        key.RIGHT: (0, 1)
    }

    if tecla_presionada in movimientos:
      dx, dy = movimientos[tecla_presionada]
      if self.limitesCoordenadas(self.x + dx, self.y + dy):
        nuevo_laberinto = deepcopy(self.laberinto)
        nuevo_laberinto[self.x + dx][self.y + dy] = self.ficha
        self.x += dx
        self.y += dy
        return nuevo_laberinto
      else:
        nuevo_laberinto = deepcopy(self.laberinto)
        nuevo_laberinto[self.x][self.y] = self.ficha
        return nuevo_laberinto

  def startGame(self):
    nuevo_laberinto = self.ponerFichaInicialTablero()
    ImprimirTablero().printTablero(nuevo_laberinto)
    while (self.x, self.y) != (self.coordenada_x_final_juego,
                                 self.coordenada_y_final_juego):
      tecla_presionada = readkey()
      tablero_actualizado = self.changeTablero(tecla_presionada)
      ImprimirTablero().printTablero(tablero_actualizado)

class Juego:

  def __init__(self):
    self.ficha_jugador = None
    self.nombre_jugador = None
    self.logicaGameInstancia = None
    self.informacionJugador()
    self.cargarDatosMapa()

  def informacionJugador(self):
    (
      self.nombre_jugador,
      self.ficha_jugador
    ) = DataJugador().dataJugador()
  
  def cargarDatosMapa(self):
    (
      coordenada_inicial_x,
      coordenada_inicial_y,
      coordenada_x_final_juego, 
      coordenada_y_final_juego,
      laberinto_list, 
      coordenada_final_x,
      coordenada_final_y
    ) = LeerMapa().obtener_datos_mapa()

    
    self.logicaGameInstancia = LogicaJuego(
      laberinto_list,
      coordenada_final_x,
      coordenada_final_y,
      self.ficha_jugador,
      coordenada_x_final_juego, 
      coordenada_y_final_juego,
      coordenada_inicial_x,
      coordenada_inicial_y
    )
  
  def Start(self):
    self.logicaGameInstancia.startGame()
    print(f"felicidades {self.nombre_jugador} has ganado")

game1 = Juego()
game1.Start()

