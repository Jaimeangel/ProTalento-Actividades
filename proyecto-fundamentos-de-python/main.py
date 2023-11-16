from readchar import readkey, key

jugador=input('Escribe tu nombre jugador: ')
print(f"Hola {jugador} bienvenido a esta aventura")
print(f"A continuacion podras jugar con tu teclado presionando cualquier tecla y podras visualizarla en pantalla")
print(f"Si quiere parar el juego presiona la tecla ↑")

while True:
  k = readkey()
  if k == key.UP:
    break
  print(k)
  
print(f"¡Gracias {jugador}, presionaste la tecla ↑, fin del juego! ")


