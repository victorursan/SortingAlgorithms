__author__ = 'victor'

from src.sorting_algorithms.GenericSort import GenericSort


class ShakeSort(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    self.col[:] = self.__shake_sort(self.col)

  def __shake_sort(self, l):
    up = range(len(l) - 1)
    while True:
      for indices in (up, reversed(up)):
        swapped = False
        for i in indices:
          if not self._in_order(l[i], l[i + 1]):
            l[i], l[i + 1] = l[i + 1], l[i]
            swapped = True
        if not swapped:
          return l