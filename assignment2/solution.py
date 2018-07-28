def merge_and_count_inv(left_arr, right_arr):
  num_entries = len(left_arr) + len(right_arr)
  i = 0
  j = 0
  num_inversions = 0
  merge_arr = []
  for idx in range(num_entries):
    if(i == len(left_arr)):
      merge_arr = merge_arr + right_arr[j:]
      break
    elif(j == len(right_arr)):
      merge_arr = merge_arr + left_arr[i:]
      #num_inversions += (len(left_arr) - i)
      break
    elif (left_arr[i] <= right_arr[j]):
      merge_arr.append(left_arr[i])
      i += 1
    else:
      merge_arr.append(right_arr[j])
      j += 1
      num_inversions += (len(left_arr) - i) 

  return  (num_inversions, merge_arr)

def sort(arr):
  if(len(arr) == 0):
    return (0, [])
  elif(len(arr) == 1):
    return (0, arr)
  else:
    mid = int(len(arr)/2)
    (left_inv, left_sorted) = sort(arr[0:mid])
    (right_inv, right_sorted) = sort(arr[mid:])
    (split_inv, merge_arr) = merge_and_count_inv(left_sorted, right_sorted)
    return (left_inv + right_inv + split_inv, merge_arr)

sorted_arr = sort([4,5,6,4,1,2,3])
print(sorted_arr, sorted_arr)
'''
sorted_arr = sort([1,3,5,2,4,6])
print(sorted_arr, sorted_arr)

'''
def read_integers(filename):
  with open(filename) as f:
    return [int(x) for x in f]

arr = read_integers("IntegerArray.txt")
print("Read ", len(arr), "numbers from the file")
(num_inversions, sorted_arr) = sort(arr)
print("num inversions=", num_inversions)

