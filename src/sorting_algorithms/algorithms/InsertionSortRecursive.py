__author__ = 'victor'

from src.sorting_algorithms.GenericSort import GenericSort


class InsertionSortRecursive(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    self.col[:] = self.__ins_sort_rec(self.col)

  def __ins_sort_rec(self, l):
    if len(l) == 0:
      return []
    return self.__insert_elem(l[0], self.__ins_sort_rec(l[1:]))

  def __insert_elem(self, elem, l):
    if len(l) == 0:
      return [elem]
    if self._in_order(elem, l[0]):
      return [elem] + l
    return [l[0]] + self.__insert_elem(elem, l[1:])