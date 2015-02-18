def DependsOn(pack, deps):
    if is_expr(deps):
        return Implies(pack, deps)
    else:
        return And([ Implies(pack, dep) for dep in deps ])

def Conflict(*packs):
    return Or([ Not(pack) for pack in packs ])

a, b, c, d, e, f, g, z = Bools('a b c d e f g z')

def install_check(*problem):
    s = Solver()
    s.add(*problem)
    if s.check() == sat:
        m = s.model()
        r = []
        for x in m:
            if is_true(m[x]):
                # x is a Z3 declaration
                # x() returns the Z3 expression
                # x.name() returns a string
                r.append(x())
        print r
    else:
        print "invalid installation profile"

print "Check 1"
install_check(DependsOn(a, [b, c, z]),
              DependsOn(b, d),
              DependsOn(c, [Or(d, e), Or(f, g)]),
              Conflict(d, e),
              Conflict(d, g),
              a, z)

print "Check 2"
install_check(DependsOn(a, [b, c, z]),
              DependsOn(b, d),
              DependsOn(c, [Or(d, e), Or(f, g)]),
              Conflict(d, e),
              Conflict(d, g),
              a, z, g)
