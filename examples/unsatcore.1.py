p1, p2, p3 = Bools('p1 p2 p3')
x, y = Ints('x y')
# We assert Implies(p, C) to track constraint C using p
s = Solver()
s.add(Implies(p1, x > 10),
      Implies(p1, y > x),
      Implies(p2, y < 5),
      Implies(p3, y > 0))
print s
# Check satisfiability assuming p1, p2, p3 are true
print s.check(p1, p2, p3)
print s.unsat_core()

# Try again retracting p2
print s.check(p1, p3)
print s.model()
