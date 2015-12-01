from z3 import *

# Create a new solver.
s = Solver()

# Create an uninterpreted sort.
A = DeclareSort('A')

# Define the uninterpreted function f and constants a and b.
f = Function('f', A, A, A)
a, b = Consts('a b', A)

# Add assertions.
s.add(f(a, b) == a, f(f(a, b), b) != a)

# Check satisfiability.
print s.check()
