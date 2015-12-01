from z3 import *

# Create a new solver.
s = Solver()

# Define the uninterpreted function f and constants x and y.
f = Function('f', IntSort(), IntSort())
x, y = Ints('x y')

# Add assertions.
s.add(f(x) == f(y), x != y)

# Check satisfiability.
print s.check()
