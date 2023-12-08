from contextlib import suppress


class Player:
  """Класс игрока.
  
  Attributes
  ----------
  _name : str
    имя игрока
  _wins : int
    количество побед игрока
  """
  def __init__(self, name:str, wins:int=0):
    self._name = name
    self._wins = wins

  def make_move(self) -> int:
    """Метод возвращает номер клетки, которую выбрал пользователь"""
    num = 0
    while num < 1 or num > 9:
      with suppress(ValueError):
        num = int(input(f"{self._name}, введите номер клетки: "))
    return num

  @property
  def name(self):
    return self._name
