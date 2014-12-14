__author__ = 'victor'

import unittest

from test.sorting_algorithms.algorithms import test_algorithms

all_suites = unittest.TestSuite([test_algorithms.suite()])

if __name__ == '__main__':
  unittest.TextTestRunner(verbosity=2).run(all_suites)