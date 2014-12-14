__author__ = 'victor'

from src.sorting_algorithms.GenericSort import GenericSort


class ShakeSort(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    self.col[:] = self.__shake_sort(self.col)

  def __shake_sort(self, l):
    return l