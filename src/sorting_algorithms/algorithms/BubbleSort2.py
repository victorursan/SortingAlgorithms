__author__ = 'victor'

from src.sorting_algorithms.GenericSort import GenericSort


class BubbleSort2(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    k = 0
    while True:
      sw = True
      k += 1
      for i in range(len(self.col) - k):
        if not self._in_order(self.col[i], self.col[i + 1]):
          self.col[i], self.col[i + 1] = self.col[i + 1], self.col[i]
          sw = False
      if sw:
        break