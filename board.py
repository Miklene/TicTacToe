from cell import Cell
from cell_symbol import Symbol


class Board:
  def __init__(self):
    self._cells = []
    for i in range (1, 10):
      self._cells.append(Cell(i))
  
  def change_cell_state(self, cell_num, symbol):
    for cell in self._cells:
      if cell.number == cell_num:
        if cell.busy:
          return False
        else:
          cell.symbol = symbol
          return True
    return False
  
  def is_end(self):
    for i in range(0, 9, 3):
      if self._cells[0 + i].symbol == self._cells[1 + i].symbol == self._cells[2 + i].symbol:
        if self._cells[0+i].symbol != Symbol.NONE:
          return True
    for i in range(0, 3, 1):
      if self._cells[0 + i].symbol == self._cells[3 + i].symbol == self._cells[6 + i].symbol:
        if self._cells[0+i].symbol != Symbol.NONE:
          return True
    if self._cells[0].symbol == self._cells[4].symbol == self._cells[8].symbol:
      if self._cells[0].symbol != Symbol.NONE:
        return True
    if self._cells[2].symbol == self._cells[4].symbol == self._cells[6].symbol:
      if self._cells[2].symbol != Symbol.NONE:
        return True
    return False

  def is_all_busy(self):
    for i in range(0, 9):
      if self._cells[i].symbol == Symbol.NONE:
        return False
    return True
  
  def __str__(self):
    board = ""
    for j in range(6, -1, -3):
      for i in range (0+j, 3+j): 
        board += str(self._cells[i].symbol.value)
        board += ' '
        if i == 2 or i == 5 or i == 8:
          board +="\n"
    return board
