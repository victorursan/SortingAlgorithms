__author__ = 'victor'

import unittest
from src.sorting_algorithms.Sorting import Sorting
from src.sorting_algorithms.algorithms.Algorithms import Algorithms


class MergeSortTestCase(unittest.TestCase):
  def test_sort(self):
    l = [3, 4, 2, 1]
    Sorting.sort(l, algorithm=Algorithms.MERGE_SORT)
    self.assertEqual(l, [1, 2, 3, 4])