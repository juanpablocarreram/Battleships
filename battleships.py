import random
import os
import time
import platform
import copy
ships_in_hidden_matrix_1_positions = []
ships_in_hidden_matrix_1 = []
ships_in_hidden_matrix_2_positions = []
ships_in_hidden_matrix_2 = []
has_someone_winned = [False , None]
def clear_terminal():
   """ Eliminar contenido en la terminal """
   if platform.system() == "Windows":
      os.system("cls")
   else:
      os.system("clear")
""" Obtener Nombres de Jugadores""" 
while True:
    clear_terminal()
    player_1_name = input("Ingresa el nombre del Jugador 1:").strip()
    player_2_name = input("Ingresa el nombre del Jugador 2:").strip()
    if player_1_name == player_2_name:
       print("El nombre del jugador es el mismo, intenta con otros:")
    else:
      break   
class matrix_of_coordinates:
  """ Objeto para guardar matrices y metodos relevantes """
  def __init__(self):
    """ Constructor de objeto"""
    """ Matrices Visibles"""
    self.matrix_1 = []
    self.matrix_2 = []
    """ Matrices con posiciones de barcos"""
    self.hidden_matrix_1 = []
    self.hidden_matrix_2 = []
    """ Crear matriz de 8x8 en 4 matrices"""
    for i in range(8):
      self.matrix_1.append(["⚪"] * 8)
      self.matrix_2.append(["⚪"] * 8)
      self.hidden_matrix_1.append([0] * 8)
      self.hidden_matrix_2.append([0] * 8)
  def print_rows(self, target):
    global player_2_attempts_left, player_1_attempts_left
    """Imprimir matriz target con buen formato"""
    for columns in range(len(target)):
      if columns == 0:
        print(f"    {columns}",end="")
      else:
        if len(str(columns))>1 and columns != len(target) - 1:
          print(f"   {columns}",end="")
        elif columns == len(target) - 1:
          print(f"   {columns}")
        else:
          print(f"    {columns}",end="")
    for i in range(len(target)):
      if len(str(i)) > 1:
        print(f"{i} ", end="")
      else:
        print(f"{i}  ", end="") 
      for j in range(len(target)):
        if j != len(target) - 1 or i != 0:
          print(f"{target[j][i]}   ",end="")
        else:
          print(f"{target[j][i]}", end="")
      print("")
    print("⚪ Significa que aun no has disparado en ese punto")
    print("🔴 Significa que ya has disparado en ese punto y no hay ninguna parte del barco")
    print("🔵 Significa que ya has disparado en ese punto y le diste a una parte del barco")
    print("🟢 Significa que ya has disparado en ese punto y ya completaste el barco")
  def choose_coordinates_of_ship(self,size,target,direction):
        """Crear lista con coordenadas sin que las coordenadas choquen""" 
        counter = 0
        list = []
        coordinate_X = None
        coordinate_Y = None
        while counter < size:
            if counter == 0:
              coordinate_Y = random.randint(0,7)
              coordinate_X = random.randint(0,7)
            if target[coordinate_Y][coordinate_X] == 0:
                list.append([coordinate_Y, coordinate_X])
                if direction == "vertical":
                    coordinate_Y+=1
                    counter+=1
                    if coordinate_Y > 7:
                       counter = 0
                       list = []
                       coordinate_X = None
                       coordinate_Y = None
                else:
                    coordinate_X+=1
                    counter+=1
                    if coordinate_X > 7:
                       counter = 0
                       list = []
                       coordinate_X = None
                       coordinate_Y = None
            else:
                counter = 0
                list = []
        return list
  def put_ships(self, target):
    """ Aplicar coordenadas del barco a las matrices"""
    global ships_in_hidden_matrix_2, ships_in_hidden_matrix_1, ships_in_hidden_matrix_1_positions, ships_in_hidden_matrix_2_positions
    ships =[2,2,3,4]
    for ship in ships:
      direction = ["vertical","horizontal"][random.randint(0,1)]
      list_of_coordinates = self.choose_coordinates_of_ship(ship,target,direction)
      if target is self.hidden_matrix_1:
         ships_in_hidden_matrix_1.append(list_of_coordinates)
         ships_in_hidden_matrix_1_positions = ships_in_hidden_matrix_1.copy()
      elif target is self.hidden_matrix_2:
         ships_in_hidden_matrix_2.append(list_of_coordinates)
         ships_in_hidden_matrix_2_positions = ships_in_hidden_matrix_2.copy()
      for coordinate in list_of_coordinates:
        target[coordinate[0]][coordinate[1]] = 1
  def make_a_turn(self,target):
     """ Hacer disparo """
     def check_guess(visible_matrix, hidden_matrix, player_number, array_of_guess, all_coordinates):
        """ Verificar si el disparo es valido"""
        for i in range(len(array_of_guess)):
           array_of_guess[i] = int(array_of_guess[i])
        if visible_matrix[array_of_guess[0]][array_of_guess[1]] != "⚪":
           print("Ya haz disparado ahí")
           self.make_a_turn(target)
        array_of_ships = None
        index_of_ship = None
        if player_number == 1:
          array_of_ships = copy.deepcopy(ships_in_hidden_matrix_1)
        else:
          array_of_ships = copy.deepcopy(ships_in_hidden_matrix_2)
        for ship_index in range(len(array_of_ships)):
           for ship_part_index in range(len(array_of_ships[ship_index])):
              if array_of_guess == array_of_ships[ship_index][ship_part_index]:
                 index_of_ship = ship_index
                 del array_of_ships[ship_index][ship_part_index]
                 break
        if index_of_ship == None:
           visible_matrix[array_of_guess[0]][array_of_guess[1]] = "🔴"
           print("Ja, no le diste")
           return 1
        if player_number == 1:
           ships_in_hidden_matrix_1[index_of_ship] = array_of_ships[index_of_ship]
        else:
           ships_in_hidden_matrix_2[index_of_ship] = array_of_ships[index_of_ship]
        if len(array_of_ships[index_of_ship]) == 0:
           for i in range(len(all_coordinates[index_of_ship])):
              visible_matrix[all_coordinates[index_of_ship][i][0]][all_coordinates[index_of_ship][i][1]] = "🟢"
           print("¡Derrumbaste el barco!")     
        else:
           visible_matrix[guess[0]][guess[1]] = "🔵"
           print("¡Acertaste al barco!")
     if target is game_map.hidden_matrix_1:
        player_matrix = 1
     else:
        player_matrix = 2
     guess = input("Ingresa a donde quieres disparar separado de coma (columna, fila):").split(",")
     if player_matrix == 1:
        check_guess(self.matrix_1, self.hidden_matrix_1, player_matrix, guess, ships_in_hidden_matrix_1_positions)
     else:
        check_guess(self.matrix_2, self.hidden_matrix_2,player_matrix, guess, ships_in_hidden_matrix_2_positions)
""" Crear objeto donde se guardan matrices y funciones del juego"""     
game_map = matrix_of_coordinates()
game_map.put_ships(game_map.hidden_matrix_1)
game_map.put_ships(game_map.hidden_matrix_2)
def check_game_status(target):
   """ Verificar si el juego ha terminado """
   counter = 0
   for ship in range(len(target)):
      if len(target[ship]) > 0:
         return 1
   return counter
def main():
  global game_map, player_1_attempts_left, player_2_attempts_left, ships_in_hidden_matrix_2, ships_in_hidden_matrix_1, player_1_name, player_2_name, has_someone_winned
  """ Bucle del juego"""
  while not has_someone_winned[0]:
     clear_terminal()
     print(f"Es turno de {player_1_name}")
     game_map.print_rows(game_map.matrix_1)
     game_map.make_a_turn(game_map.hidden_matrix_1)
     clear_terminal()
     game_map.print_rows(game_map.matrix_1)
     time.sleep(2)
     if check_game_status(ships_in_hidden_matrix_1) == 0:
       has_someone_winned[1] = player_1_name
       break
     clear_terminal()
     print(f"Es turno de {player_2_name}")
     game_map.print_rows(game_map.matrix_2)
     game_map.make_a_turn(game_map.hidden_matrix_2)
     clear_terminal()
     game_map.print_rows(game_map.matrix_2)
     time.sleep(2)
     if check_game_status(ships_in_hidden_matrix_2) == 0:
       has_someone_winned[1] = player_2_name
       break
  print(f"¡{has_someone_winned[1]} ha ganado el juego!")
main()
