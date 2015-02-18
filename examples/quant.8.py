A = DeclareSort('A')
B = DeclareSort('B')
f = Function('f', A, B)
finv = Function('finv', B, A)
a1, a2 = Consts('a1 a2', A)
b      = Const('b', B)
x,  y  = Consts('x y', A)

s = Solver()
s.add(a1 != a2,
      f(a1) == b,
      f(a2) == b,
      ForAll(x, finv(f(x)) == x)
      )
print s.check()
