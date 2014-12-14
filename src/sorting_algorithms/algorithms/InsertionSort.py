__author__ = 'victor'

from src.sorting_algorithms.GenericSort import GenericSort


class InsertionSort(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    self.col[:] = self.__ins_sort(self.col)

  def __ins_sort(self, l):
    for i in range(1, len(l)):
      p = l[i]
      j = i - 1
      while j >= 0 and self._in_order(p, l[j]):
        l[j + 1] = l[j]
        j -= 1
      l[j + 1] = p
    return l