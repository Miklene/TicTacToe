from enum import Enum

from cell_symbol import Symbol


class Cell:
  def __init__(self, number, busy=False, symbol=Symbol.NONE):
    self._number = number
    self._busy = busy
    self._symbol = symbol

  @property
  def number(self):
    return self._number

  @property
  def busy(self):
    return self._busy

  @property
  def symbol(self):
    return self._symbol

  @symbol.setter
  def symbol(self, symbol:Symbol):
    self._symbol = symbol
    if self._symbol != Symbol.NONE:
      self._busy = True
    else:
      self._busy = False
