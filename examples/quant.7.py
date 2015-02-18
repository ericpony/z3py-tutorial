A = DeclareSort('A')
B = DeclareSort('B')
f = Function('f', A, B)
a1, a2 = Consts('a1 a2', A)
b      = Const('b', B)
x,  y  = Consts('x y', A)

s = Solver()
s.add(a1 != a2,
      f(a1) == b,
      f(a2) == b,
      ForAll([x, y], Implies(f(x) == f(y), x == y),
             patterns=[MultiPattern(f(x), f(y))])
      )
print s.check()
