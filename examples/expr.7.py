x, y = Ints('x y')
f    = Function('f', IntSort(), IntSort(), IntSort())
g    = Function('g', IntSort(), IntSort())
n    = f(f(g(x), g(g(x))), g(g(y)))
print n
# substitute g(g(x)) with y and g(y) with x + 1
print substitute(n, (g(g(x)), y), (g(y), x + 1))
