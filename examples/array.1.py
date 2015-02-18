# Use I as an alias for IntSort()
I = IntSort()
# A is an array from integer to integer
A = Array('A', I, I)
x = Int('x')
print A[x]
print Select(A, x)
print Store(A, x, 10)
print simplify(Select(Store(A, 2, x+1), 2))

