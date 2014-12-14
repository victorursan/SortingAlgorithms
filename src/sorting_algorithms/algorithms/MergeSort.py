__author__ = 'victor'

from sorting_algorithms.GenericSort import GenericSort


class MergeSort(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    self.col[:] = self.__merge_sort(self.col)

  def __merge_sort(self, l):
    if len(l) <= 1:
      return l
    m = len(l) // 2
    left = self.__merge_sort(l[:m])
    right = self.__merge_sort(l[m:])
    return self.__merge(left, right)

  @staticmethod
  def __merge(left, right):
    rez = []
    while len(left) > 0 and len(right) > 0:
      if left[0] < right[0]:
        rez.append(left.pop(0))
      else:
        rez.append(right.pop(0))
    rez.extend(left + right)
    return rez