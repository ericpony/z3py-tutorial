f = Function('f', IntSort(), IntSort())
g = Function('g', IntSort(), IntSort())
a, b, c = Ints('a b c')
x = Int('x')

s = Solver()
s.set(auto_config=False, mbqi=False)

s.add( ForAll(x, f(g(x)) == x, patterns = [f(g(x))]),
       a == g(b),
       b == c,
       f(a) != c )

print s.check()
