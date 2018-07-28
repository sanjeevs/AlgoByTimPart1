from math import floor
def qsort(a, lhs, rhs, num_cmps):
  """ Sort the array and record the number of comparisons.
  >>> a = [2,1]
  >>> num_cmps = 0
  >>> qsort(a, 0, 1, num_cmps)
  1

  >>> print(a)
  [1, 2]

  """
  if((rhs - lhs) >= 1):
    num_cmps += (rhs - lhs) 
    pivot = partition(a, lhs, rhs)
    num_cmps = qsort(a, lhs, pivot -1, num_cmps)
    num_cmps = qsort(a, pivot + 1, rhs, num_cmps)

  return num_cmps

def partition(a, lhs, rhs):
  """ Return the correct position of the pivot element.
  >>> a = [1]
  >>> partition(a, 0, 0)
  0
  >>> a = [2,1]
  >>> partition(a, 0, 1)
  1
  >>> print(a)
  [1, 2]
  >>> a = [100,101,3,8,2,200,201]
  >>> partition(a, 2, 4)
  3
  >>> print(a)
  [100, 101, 2, 3, 8, 200, 201]
  """
  if(len(a) == 1):
    return 0
  else:
    #swap(a, lhs, rhs)
    idx = choose_median_pivot(a, lhs, rhs)
    swap(a, lhs, idx) 
    pivot = a[lhs]
    i = lhs + 1
    for j in range(lhs+1, rhs+1):
      if(a[j] < pivot):
        swap(a, i, j)
        i += 1
    swap(a, lhs, i -1)
    return i -1

def swap(a, i, j):
  """ Swap the elements of the arr.
  >>> a = [1,2,3]
  >>> swap(a, 1, 2)
  >>> print(a)
  [1, 3, 2]
  """
  a[i], a[j] = a[j], a[i]

def mid(a, lhs, rhs):
  """ Return the middle element of arr
  >>> a = [8,2,4,5,7,1]
  >>> mid(a, 0, 5)
  2
  >>> a = [8,2,4,5,7,1]
  >>> mid(a, 1, 5)
  3

  """
  mid = floor((lhs + rhs)/2)
  return mid 

def median_of_3(a):
  """ Return the median of 3 elements.
  >>> median_of_3([1, 4, 8])
  4
  >>> median_of_3([8, 1, 4])
  4

  """
  tmp = a.copy()
  tmp.sort()
  return tmp[1]

def choose_median_pivot(a, lhs, rhs):
  """ Choose the median of the value.
  Consider the first, last and middle value of array. Find the median
  an use that as the pivot.
  >>> choose_median_pivot([8,2,4,5,7,1], 0, 5)
  2
  
  >>> choose_median_pivot(list(range(10)), 1, 5)
  3
  
  >>> choose_median_pivot([2,1,4], 0, 2)
  0
  
  >>> choose_median_pivot([2,1,4,5], 0, 3)
  0

  """
  mid_idx = mid(a, lhs, rhs)
  choices = [a[lhs], a[mid_idx], a[rhs]]
  mid_value = median_of_3(choices)
  if(mid_value == a[lhs]):
    return lhs
  elif(mid_value == a[rhs]):
    return rhs
  else:
    return mid_idx

if __name__ == "__main__":
  import doctest
  doctest.testmod()
