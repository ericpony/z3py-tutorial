p, q = Bools('p q')
demorgan = And(p, q) == Not(Or(Not(p), Not(q)))
print demorgan

def prove(f):
    s = Solver()
    s.add(Not(f))
    if s.check() == unsat:
        print "proved"
    else:
        print "failed to prove"

print "Proving demorgan..."
prove(demorgan)
