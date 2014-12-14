__author__ = 'victor'

from src.sorting_algorithms.GenericSort import GenericSort


class SelectionSort(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    self.col[:] = self.__selection_sort(self.col)

  def __selection_sort(self, l):
    for i in range(len(l) - 1):
      i_min = i
      for j in range(i, len(l)):
        if self._in_order(l[j], l[i_min]):
          i_min = j
      if i_min != i:
        l[i], l[i_min] = l[i_min], l[i]
    return l