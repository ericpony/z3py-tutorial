x = Int('x')
y = Int('y')
f = Function('f', IntSort(), IntSort())
s = Solver()
s.add(f(f(x)) == x, f(x) == y, x != y)
print s.check()
m = s.model()
print "f(f(x)) =", m.evaluate(f(f(x)))
print "f(x)    =", m.evaluate(f(x))


