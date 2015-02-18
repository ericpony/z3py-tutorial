x, y, z = Reals('x y z')
g = Goal()
g.add(x**2 - y**2 >= 0)

p = Probe('num-consts')
t = If(p > 2, 'simplify', 'factor')

print t(g)

g = Goal()
g.add(x + x + y + z >= 0, x**2 - y**2 >= 0)

print t(g)
