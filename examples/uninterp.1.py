A    = DeclareSort('A')
x, y = Consts('x y', A)
f    = Function('f', A, A)

s    = Solver()
s.add(f(f(x)) == x, f(x) == y, x != y)

print s.check()
m = s.model()
print m
print "interpretation assigned to A:"
print m[A]
