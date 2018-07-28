import unittest
from karger_algo.graph import Graph 
from karger_algo.edge import Edge

class TestGraph3(unittest.TestCase):
  def setUp(self):
    ''' Setup a cyclic graph with 4 nodes '''
    str = '''
    1 2 3
    2 1 4
    3 1 4
    4 2 3
    '''
    self.g1 = Graph().load_from_string(str)
  
  def test_num_nodes(self):
    self.assertEqual(self.g1.num_nodes(), 4)

  def test_num_edges(self):
    self.assertEqual(self.g1.num_edges(), 4)

  def test_sanity(self):
    self.assertTrue(self.g1.is_undirected())

  def test_num_nodes(self):
    self.assertEqual(self.g1.num_nodes(), 4)

  def test_delete(self):
    self.g1.del_edge(Edge('1', '2'))
    self.assertEqual(self.g1.num_nodes(), 4)
    self.assertEqual(self.g1.num_edges(), 3)
    self.g1.del_edge(Edge('1', '3'))
    self.assertEqual(self.g1.num_nodes(), 4)
    self.assertEqual(self.g1.num_edges(), 2)
    self.assertTrue(self.g1.is_unconnected_node('1'))

  def test_pick_edge(self):
    e1 = self.g1.pick_edge()
    self.g1.del_edge(e1)
    self.assertEqual(self.g1.num_nodes(), 4)
    self.assertEqual(self.g1.num_edges(), 3)

  def test_del_all(self):
    n = self.g1.num_nodes()
    m = self.g1.num_edges()
    for i in range(m):
      e1 = self.g1.pick_edge()
      self.g1.del_edge(e1)
      self.assertEqual(self.g1.num_edges(), m - i -1)

