def DependsOn(pack, deps):
    return And([ Implies(pack, dep) for dep in deps ])

def Conflict(p1, p2):
    return Or(Not(p1), Not(p2))

a, b, c, d, e, f, g, z = Bools('a b c d e f g z')

solve(DependsOn(a, [b, c, z]),
      DependsOn(b, [d]),
      DependsOn(c, [Or(d, e), Or(f, g)]),
      Conflict(d, e),
      a, z)
