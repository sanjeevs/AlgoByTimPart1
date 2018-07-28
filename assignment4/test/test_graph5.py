import unittest
from karger_algo.graph import Graph 

class TestGraph5(unittest.TestCase):
  def setUp(self):
    s = '''
      1 2 2 3
      2 1 1 3
      3 1 2
      '''
    self.graph = Graph()
    self.graph.load_from_string(s)

  def test_contract(self):
    self.graph.contract_nodes('1', '2')
    self.assertEqual(self.graph.num_nodes(), 2)
    self.assertEqual(self.graph.num_edges(), 2)
    self.assertTrue(self.graph.is_undirected())

