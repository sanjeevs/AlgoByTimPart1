from . import edge
import io
import sys
import random
import pprint

class Graph:
  def __init__(self):
    self.graph = {}

  def load_from_file(self, filename):
    ''' Load the graph from a file '''
    with open(filename) as fh:
      lines = [line.strip() for line in fh]
    self.load_from_adj_lst(lines)
    return self

  def load_from_string(self, string):
    ''' Load the graph from a string'''
    lines = []
    buf = io.StringIO(string)
    for l in buf.readlines():
      l = l.strip()
      if l != "":
        lines.append(l)
    self.load_from_adj_lst(lines)
    return self

  def load_from_adj_lst(self, lst):
    ''' Load the graph from a list of lines'''
    for line in lst:
      self.add_adj_line(line)
    return self

  def add_adj_line(self, line):
    nodes = line.strip().split()
    self.graph[nodes[0]] = nodes[1:]
    
  def num_nodes(self):
    ''' Return the number of nodes in the graph '''
    return int(len(self.graph))  

  def num_edges(self):
    ''' Return the number of edges in the graph '''
    total = 0
    for item in self.graph.values():
      total += len(item)
    return int(total/2)  #Edges are undirected

  def is_unconnected(self):
    ''' Return True if the graph is unconnected '''
    return (self.num_edges() == 0)

  def is_unconnected_node(self, node):
    ''' Return True if the node is unconnected '''
    return (len(self.graph[node]) == 0)

  def neighbors(self, node):
    ''' Return list of all the neighboring nodes '''
    return self.graph[node]

  def is_undirected(self):
    ''' Debug routines to check if the graph has all edges as undirected'''
    edges_cnt = {}
    for n1 in self.graph.keys():
      for n2 in self.graph[n1]:
        e1 = edge.Edge(n1, n2)
        if e1 not in edges_cnt:
          edges_cnt[e1] = 1
        else:
          edges_cnt[e1] += 1
    for cnt in edges_cnt.values():
      if(cnt % 2 != 0):
        return False
    return True

  def del_edge(self, e1):
    ''' Delete edge e1 from graph '''
    self.graph[e1.node1].remove(e1.node2)
    self.graph[e1.node2].remove(e1.node1)

  def pick_edge(self):
    ''' Return a random edge from the graph. '''
    if(self.is_unconnected()):
      raise ValueError('Graph is unconnected. No edges present')
    while True: 
      # Graph has already one node that has an edge. So keep trying.
      key = random.choice(list(self.graph.keys()))
      if(len(self.graph[key]) > 0):
        break
    idx2 = random.randint(0, len(self.graph[key]) -1)
    return edge.Edge(key, self.graph[key][idx2])

  def contract_nodes(self, n1, n2):
    ''' Contract the nodes n1 and n2 into n1_n2 '''
    new_node = n1 + "_" + n2
    if(new_node in self.graph):
      raise NameError("New node is already present")
    
    new_neighbors = self.graph[n1] + self.graph[n2]
    new_neighbors = [value for value in new_neighbors if value != n1]
    new_neighbors = [value for value in new_neighbors if value != n2]
    self.graph[new_node] = new_neighbors

    #Patch the rest of the graph nodes to point to super node.
    for node in new_neighbors:
      self.graph[node] = [new_node if x == n1 else x for x in self.graph[node]]
      self.graph[node] = [new_node if x == n2 else x for x in self.graph[node]]

    #Clean up by deleting the old nodes.
    del self.graph[n1]
    del self.graph[n2]
