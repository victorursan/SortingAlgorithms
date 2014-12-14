__author__ = 'victor'

from src.sorting_algorithms.GenericSort import GenericSort


class BubbleSort(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    self.col[:] = self.__bubble_sort(self.col)

  def __bubble_sort(self, l):
    while True:
      sw = True
      for i in range(len(l) - 1):
        if not self._in_order(l[i], l[i + 1]):
          l[i], l[i + 1] = l[i + 1], l[i]
          sw = False
      if sw:
        break
    return l