f = Function('f', IntSort(), IntSort(), IntSort())
x, y = Ints('x y')
f = ForAll([x, y], f(x, y) == 0)
print f.body()
v1 = f.body().arg(0).arg(0)
print v1
print eq(v1, Var(1, IntSort()))
