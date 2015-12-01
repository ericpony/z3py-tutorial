from z3 import *

# Create a new solver.
s = Solver()

# Define the uninterpreted function f and constant a.
f = Function('f', IntSort(), IntSort())
a = Int('a')

# Add assertions.
s.add(f(f(f(a))) == a, f(f(f(f(f(a))))) == a, f(a) != a)

# Check satisfiability.
print s.check()
