from board import Board
from cell_symbol import Symbol
from player import Player


class Game:
  """Класс Игры
  
  Attributes
  ----------
  _player1 : Player
    первый игрок
  _player2 : Player
    второй игрок
  
  Чтобы начать игру - вызовите метод start
  """
  def __init__(self, player1:Player, player2:Player):
    self._player1 = player1
    self._player2 = player2  
    
  def start(self)->None:
    """Метод начала работы игры.

    Тут содержится главный цикл игры. По окончанию игры предлагает начать заново или закончить играть.
    """
    while True:
      self._start_new_game()    
      choice = input("Новая игра? y/n ")
      if choice != "y":
        break

    
  def _start_new_game(self)->None:
    """Метод начала новой игры.

    Создает новую доску. В цикле выводит состояние доски и запрашивает ввод игроков"""
    self._board = Board()
    while True:
      print(self._board)
      if self._move(self._player1, Symbol.CROSS):
        break
      print(self._board)
      if self._move(self._player2, Symbol.ZERO):
        break

  def _move(self, player:Player, symbol:Symbol):
    """Метод одного хода игры.

    Просит игрока ввести номер клетки.
    Проверяет, что клетка свободна.
    Проверяет условие победы/ничьи

    Attributes
    ----------
    player : Player
      игрок, который сейчас ходит
    symbol : Symbol
      символ, который присвоен игроку
    """
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


  