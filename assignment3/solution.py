from qsort import qsort

a = []
with open('QuickSort.txt') as file:
  for line in file:
    a.append(int(line))

num_cmps = 0
num_cmps = qsort.qsort(a, 0, len(a) -1, num_cmps)

print("Number of comparions", num_cmps)
