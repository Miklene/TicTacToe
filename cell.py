from enum import Enum

from cell_symbol import Symbol


class Cell:
  """Класс игровой клетки поля
  
  Attributes
  ----------
  _number : int
    номер клетки
  _busy : bool
    состояние клетки. True - если занята(крестик или нолик), false - иначе
  _symbol : Symbol
    тип символа, который содержит клетка
  """
  def __init__(self, number:int, busy:bool=False, symbol:Symbol=Symbol.NONE):
    self._number = number
    self._busy = busy
    self._symbol = symbol

  @property
  def number(self)->int:
    return self._number

  @property
  def busy(self)->bool:
    return self._busy

  @property
  def symbol(self)->Symbol:
    return self._symbol

  @symbol.setter
  def symbol(self, symbol:Symbol):
    self._symbol = symbol
    #если клетка не пустая, то она busy
    if self._symbol != Symbol.NONE:
      self._busy = True
    else:
      self._busy = False
