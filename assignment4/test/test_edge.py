import unittest
from karger_algo import * 

class TestEdge(unittest.TestCase):
  def test_edge1(self):
    e1 = edge.Edge('n1', 'n2')
    self.assertEqual(e1.node1, "n1")
    self.assertEqual(e1.node2, "n2")

  def test_equal1(self):
    e1 = edge.Edge('n1', 'n2')
    e2 = edge.Edge('n1', 'n2')
    self.assertTrue(e1 == e2)
    
  def test_equal2(self):
    e1 = edge.Edge('n1', 'n2')
    e2 = edge.Edge('n2', 'n1')
    self.assertTrue(e1 == e2)
  
  def test_hash(self):
    a = {}
    e1 = edge.Edge('n1', 'n2')
    e2 = edge.Edge('n2', 'n1')
    a[e1] = 1
    a[e2] += 1
    self.assertEqual(a[e1], 2)
    self.assertEqual(a[e2], 2)

  
