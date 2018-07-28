from qsort.qsort import *
import unittest
from random import randint

class MyTest(unittest.TestCase):

  def test_qsort1(self):
    a = [3, 8, 2, 5, 1, 4, 7, 6]
    num_cmps = 0
    qsort(a, 0, len(a) -1, num_cmps)
    self.assertEqual([1,2,3,4,5,6,7,8], a)

  def test_rand1(self):
    randints = []
    for _ in range(1000):
      randints.append(randint(1,9999))
    a = randints.copy()
    num_cmps = 0
    qsort(a, 0, len(a) -1, num_cmps)
    randints.sort()
    self.assertEqual(a, randints)

  def test_txt(self):
    a = []
    with open('QuickSort.txt') as file:
      a = [int(x) for x in file]
    exp_arr = a.copy()
    exp_arr.sort()
    num_cmps = 0
    qsort(a, 0, len(a) -1, num_cmps)
    self.assertEqual(a, exp_arr)

if __name__ == "__main__":
  unittest.main()
