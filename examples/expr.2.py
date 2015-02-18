x, y = Ints('x y')
print eq(x + y, x + y)
print eq(x + y, y + x)
n = x + y
print eq(n, x + y)
# x2 is eq to x
x2 = Int('x') 
print eq(x, x2)
# the integer variable x is not equal to 
# the real variable x
print eq(Int('x'), Real('x'))
