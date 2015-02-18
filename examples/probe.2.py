x, y, z = Reals('x y z')
g = Goal()
g.add(x + y + z > 0)

p = Probe('num-consts')
print "num-consts:", p(g)

t = FailIf(p > 2)
try:
    t(g)
except Z3Exception:
    print "tactic failed"

print "trying again..."
g = Goal()
g.add(x + y > 0)
print t(g)

