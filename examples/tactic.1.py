x, y = Reals('x y')
g  = Goal()
g.add(x > 0, y > 0, x == y + 2)
print g

t1 = Tactic('simplify')
t2 = Tactic('solve-eqs')
t  = Then(t1, t2)
print t(g)
