from enum import Enum


class Symbol(Enum):
  """Перечисление символов, которые могут быть внутри клетки

  NONE - пустая клетка,
  CROSS - крестик,
  ZERO - нолик
  """
  NONE = '_'
  CROSS = 'X'
  ZERO = 'O'

  #def __str__(self):
  #  return str(self.value)
