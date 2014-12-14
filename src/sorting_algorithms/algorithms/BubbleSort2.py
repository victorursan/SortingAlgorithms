__author__ = 'victor'

from src.sorting_algorithms.GenericSort import GenericSort


class BubbleSort2(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    self.col[:] = self.__bubble_sort_2(self.col)

  def __bubble_sort_2(self, l):
    k = 0
    while True:
      sw = True
      k += 1
      for i in range(len(l) - k):
        if not self._in_order(l[i], l[i + 1]):
          l[i], l[i + 1] = l[i + 1], l[i]
          sw = False
      if sw:
        break
    return l