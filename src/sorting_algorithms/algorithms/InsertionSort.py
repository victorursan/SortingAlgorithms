__author__ = 'victor'

from sorting_algorithms.GenericSort import GenericSort


class InsertionSort(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    for i in range(1, len(self.col)):
      p = self.col[i]
      j = i - 1
      while j >= 0 and self._in_order(p, self.col[j]):
        self.col[j + 1] = self.col[j]
        j -= 1
      self.col[j + 1] = p