x = BitVec('x', 16)
y = BitVec('y', 16)
print x + 2
# Internal representation
print (x + 2).sexpr()

# -1 is equal to 65535 for 16-bit integers 
print simplify(x + y - 1)

# Creating bit-vector constants
a = BitVecVal(-1, 16)
b = BitVecVal(65535, 16)
print simplify(a == b)

a = BitVecVal(-1, 32)
b = BitVecVal(65535, 32)
# -1 is not equal to 65535 for 32-bit integers 
print simplify(a == b)

