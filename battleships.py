import random
import os
import time

player_1_attempts_left = 10
player_2_attempts_left = 10
ships_in_hidden_matrix_1 = []
ships_in_hidden_matrix_2 = []
while True:
    player_1_name = input("Ingresa el nombre del Jugador 1:").strip()
    player_2_name = input("Ingresa el nombre del Jugador 2:").strip()
    if player_1_name == player_2_name:
       print("Same player name, try with different names")
       continue
    break   

class matrix_of_coordinates:
  def __init__(self):
    """ Matrices that are printed"""
    self.matrix_1 = []
    self.matrix_2 = []
    """ Matrices with ships places """
    self.hidden_matrix_1 = []
    self.hidden_matrix_2 = []
    """ Create 15x15 Matrix for both players"""
    for i in range(10):
      self.matrix_1.append(["⚪"] * 10)
      self.matrix_2.append(["⚪"] * 10)
      self.hidden_matrix_1.append([0] * 10)
      self.hidden_matrix_2.append([0] * 10)
  def print_rows(self, target):
    global player_2_attempts_left, player_1_attempts_left
    if target is self.matrix_1:
       print(f"Es turno de {player_1_name}")
    elif target is self.matrix_2:
       print(f"Es turno de {player_2_name}")
    """Print Columns Line of Target Matrix"""
    for columns in range(len(target)):
      if columns == 0:
        print(f"    {columns}",end="")
      else:
        if len(str(columns))>1 and columns != len(target) - 1:
          print(f"   {columns}",end="")
        elif columns == len(target) - 1:
          print(f"   {columns}                Intentos restantes de {player_1_name}: {player_1_attempts_left}")
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
          print(f"{target[j][i]}                Intentos restantes de {player_2_name}: {player_2_attempts_left}",end="")
      print("")
    print("⚪ Significa que aun no has disparado en ese punto")
    print("🔴 Significa que ya has disparado en ese punto y no hay ninguna parte del barco")
    print("🔵 Significa que ya has disparado en ese punto y le diste a una parte del barco")
    print("🟢 Significa que ya has disparado en ese punto y ya completaste el barco")
  def choose_coordinates_of_ship(self,size,target,direction):
        counter = 0
        list = []
        coordinate_X = None
        coordinate_Y = None
        while counter < size:
            if counter == 0:
              coordinate_Y = random.randint(0,9)
              coordinate_X = random.randint(0,9)
            if target[coordinate_Y][coordinate_X] == 0:
                list.append([coordinate_Y, coordinate_X])
                if direction == "vertical":
                    coordinate_Y+=1
                    counter+=1
                    if coordinate_Y > 9:
                       counter = 0
                       list = []
                       coordinate_X = None
                       coordinate_Y = None
                else:
                    coordinate_X+=1
                    counter+=1
                    if coordinate_X > 9:
                       counter = 0
                       list = []
                       coordinate_X = None
                       coordinate_Y = None
            else:
                counter = 0
                list = []
        return list
  """ Recuerda que debes guardar las coordenadas de cada barco separados por cada jugador en una lista"""
  def put_ships(self, target):
    global ships_in_hidden_matrix_2, ships_in_hidden_matrix_1
    ships =[2,2,3,4]
    for ship in ships:
      direction = ["vertical","horizontal"][random.randint(0,1)]
      list_of_coordinates = self.choose_coordinates_of_ship(ship,target,direction)
      if target is self.hidden_matrix_1:
         ships_in_hidden_matrix_1.append(list_of_coordinates)
      elif target is self.hidden_matrix_2:
         ships_in_hidden_matrix_2.append(list_of_coordinates)
      for coordinate in list_of_coordinates:
        target[coordinate[0]][coordinate[1]] = 1
      
        

      
    
          
game_map = matrix_of_coordinates()
game_map.put_ships(game_map.hidden_matrix_1)
game_map.put_ships(game_map.hidden_matrix_2)
game_map.print_rows(game_map.hidden_matrix_1)
game_map.print_rows(game_map.hidden_matrix_2)


def main():
  global game_map, player_1_attempts_left, player_2_attempts_left, ships_in_hidden_matrix_2, ships_in_hidden_matrix_1, player_1_name, player_2_name
 
main()
  

