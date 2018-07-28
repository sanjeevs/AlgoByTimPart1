import unittest
from karger_algo.graph import Graph 
from karger_algo.edge import Edge

class TestGraph2(unittest.TestCase):
  def setUp(self):
    ''' Create a fully connected graph with 3 nodes '''
    self.graph = Graph()
    self.graph.add_adj_line("1 2 3")
    self.graph.add_adj_line("2 1 3")
    self.graph.add_adj_line("3 1 2")

  def test_num_edges(self):
    self.assertEqual(self.graph.num_edges(), 3)

  def test_valid(self):
    self.assertEqual(self.graph.is_undirected(), True)

