from contextlib import suppress


class Player:
  def __init__(self, name, wins=0):
    self._name = name
    self._wins = wins

  def make_move(self):
    num = 0
    while num < 1 or num > 9:
      with suppress(ValueError):
        num = int(input(f"{self._name}, введите номер клетки: "))
    return num

  @property
  def name(self):
    return self._name
