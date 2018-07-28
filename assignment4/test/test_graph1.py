import unittest
from karger_algo import graph 
from karger_algo import edge 

class TestGraph1(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.graph = graph.Graph()
    cls.graph.load_from_file("kargerMinCut.txt")
    
  def test_num_nodes(self):
    self.assertEqual(TestGraph1.graph.num_nodes(), 200)

  def test_node_200(self):
    self.assertEqual(len(TestGraph1.graph.neighbors('200')), 24)
    self.assertEqual(TestGraph1.graph.neighbors('200')[0], '149')
    self.assertEqual(TestGraph1.graph.neighbors('200')[23], '35')

  def test_num_edges(self):
    self.assertEqual(TestGraph1.graph.num_edges(), 5034/2)

  def test_node_6(self):
    self.assertEqual(TestGraph1.graph.neighbors('6')[0], '155')
    self.assertEqual(TestGraph1.graph.neighbors('6')[1], '56')
    self.assertEqual(TestGraph1.graph.neighbors('6')[2], '52')

    
