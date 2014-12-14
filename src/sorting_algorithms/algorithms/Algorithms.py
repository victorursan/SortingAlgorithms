__author__ = 'victor'

from enum import unique, Enum
from sorting_algorithms.algorithms.BubbleSort import BubbleSort
from sorting_algorithms.algorithms.BubbleSort2 import BubbleSort2
from sorting_algorithms.algorithms.InsertionSort import InsertionSort
from sorting_algorithms.algorithms.InsertionSortRecursive import InsertionSortRecursive
from sorting_algorithms.algorithms.QuickSort import QuickSort
from sorting_algorithms.algorithms.MergeSort import MergeSort


@unique
class Algorithms(Enum):
  BUBBLE_SORT = BubbleSort
  BUBBLE_SORT2 = BubbleSort2
  INSERTION_SORT = InsertionSort
  INSERTION_SORT_REC = InsertionSortRecursive
  QUICK_SORT = QuickSort
  MERGE_SORT = MergeSort