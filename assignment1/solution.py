def kasturba(x,y):
  '''
    Implents the Kasturba Multiplication Algo.
  '''
  if(len(x) <= 1 and len(y) <= 1):
    return x[0] * y[0]
  else:
    n = len(x)
    a = x[0:int(n/2)]
    b = x[int(n/2):n]
    c = y[0:int(n/2)]
    d = y[int(n/2):n]
    return (10**n * kasturba(a,c) + 10**int(n/2) * (kasturba(a,d) + kasturba(b,c)) + kasturba(b,d))

x = [1,2,3,4]
y = [5,6,7,8]

x_lst = list("3141592653589793238462643383279502884197169399375105820974944592")
y_lst = list("2718281828459045235360287471352662497757247093699959574966967627")
x = list(map(int, list(x_lst)))
y = list(map(int, list(y_lst)))
print(kasturba(x,y))

