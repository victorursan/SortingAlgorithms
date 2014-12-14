__author__ = 'victor'

import unittest
from test.sorting_algorithms.algorithms.BubbleSort2TestCase import BubbleSort2TestCase
from test.sorting_algorithms.algorithms.BubbleSortTestCase import BubbleSortTestCase
from test.sorting_algorithms.algorithms.InsertionSortRecursiveTestCase import InsertionSortRecursiveTestCase
from test.sorting_algorithms.algorithms.InsertionSortTestCase import InsertionSortTestCase
from test.sorting_algorithms.algorithms.MergeSortTestCase import MergeSortTestCase
from test.sorting_algorithms.algorithms.QuickSortTestCase import QuickSortTestCase


def suite():
  suites = unittest.TestSuite()
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(BubbleSortTestCase))
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(BubbleSort2TestCase))
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(InsertionSortTestCase))
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(InsertionSortRecursiveTestCase))
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(MergeSortTestCase))
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(QuickSortTestCase))
  return suites