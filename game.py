from board import Board
from cell_symbol import Symbol


class Game:
  def __init__(self, player1, player2):
    self._player1 = player1
    self._player2 = player2  
    
  def start(self):
    while True:
      self._start_new_game()    
      choice = input("Новая игра? y/n ")
      if choice != "y":
        break

    
  def _start_new_game(self):
    self._board = Board()
    while True:
      print(self._board)
      if self._move(self._player1, Symbol.CROSS):
        break
      print(self._board)
      if self._move(self._player2, Symbol.ZERO):
        break

  def _move(self, player, symbol):
    while True:
      num = player.make_move()
      if not self._board.change_cell_state(num, symbol):
        print("Клетка занята")
      else:
        break
    if self._board.is_end():
      print(self._board)
      print(f"Игрок {player.name} выиграл!")
      return True
    if self._board.is_all_busy():
      print(self._board)
      print(f"Ничья!")
      return True
    return False


  