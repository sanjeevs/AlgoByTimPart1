from karger_algo import * 
import math
import copy

def solution():
  g = graph.Graph()
  g.load_from_file("kargerMinCut.txt")
  n = g.num_nodes()
  num_trials = int(n**2 * math.log(n))
  num_trials = 100
  min_crossover = g.num_edges()
  print(">>Running for num_trials=", num_trials)
  for i in range(num_trials):
    tmp = copy.deepcopy(g)
    k = karger_algo.run(tmp)
    if k < min_crossover:
      min_crossover = k
      print("Trial#", i + 1, "Updated MinCrossEdges to ", min_crossover)

  print("Number of edges crossing the min cut=", min_crossover)

if __name__ == "__main__":
  solution()
