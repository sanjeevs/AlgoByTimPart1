import unittest
from karger_algo.graph import Graph 

class TestGraph4(unittest.TestCase):
  ''' Example from lecture
      1---2
      |  /|
      | / |
      3---4
      
      Pick Edge 1_3

      1_3------2
       |-------|
       |
       4
  '''
  def setUp(self):
    s = '''
    1 2 3
    3 1 2 4
    2 1 3 4
    4 3 2
    '''
    self.graph = Graph()
    self.graph.load_from_string(s)

  def test_contract1(self):
    self.graph.contract_nodes('1', '3')
    self.assertEqual(self.graph.num_nodes(), 3)
    self.assertEqual(self.graph.num_edges(), 4)
    self.assertTrue(self.graph.is_undirected())
