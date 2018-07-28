import unittest
from karger_algo import * 
import math
import copy

class TestKargerAlgo1(unittest.TestCase):
  ''' Take the graph from class example.
      1----2-----5----6
      | \ /|     | \/ | 
      |/ \ |     |/ \ |
      3----4-----7----8
  '''
  def setUp(self):
    self.s1 = '''
     1 2 3 4
     2 1 3 4 5
     3 1 2 4
     4 1 3 2 7
     5 2 7 8 6
     6 5 7 8
     7 4 5 6 8
     8 5 6 7
    '''
    self.graph = graph.Graph()
    self.graph.load_from_string(self.s1)

  def test_min_cut(self):
    min_crossover = self.graph.num_edges()
    n = self.graph.num_nodes()
    num_trials = int(n**2 * math.log(n))
    for i in range(num_trials):
      tmp = copy.deepcopy(self.graph)
      k = karger_algo.run(tmp)
      if k < min_crossover:
        min_crossover = k

    self.assertEqual(min_crossover, 2)

