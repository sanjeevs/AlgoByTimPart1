import pprint
def run(graph):
  ''' return the number of crossing edges in min cut'''
  while graph.num_nodes() > 2:
    e1 = graph.pick_edge()
    graph.contract_nodes(e1.node1, e1.node2)
  return graph.num_edges()

