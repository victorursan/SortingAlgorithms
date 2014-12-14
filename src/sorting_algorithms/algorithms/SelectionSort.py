__author__ = 'victor'

from src.sorting_algorithms.GenericSort import GenericSort


class SelectionSort(GenericSort):
  def __init__(self, col, key, reverse):
    super().__init__(col, key, reverse)

  def sort(self):
    pass