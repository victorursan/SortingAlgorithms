__author__ = 'victor'

from sorting_algorithms.algorithms.Algorithms import Algorithms


class Sorting(object):
  @staticmethod
  def sort(col, key=None, reverse=False, algorithm=Algorithms.BUBBLE_SORT):
    sorting_alg = algorithm.value(col, key, reverse)
    sorting_alg.sort()