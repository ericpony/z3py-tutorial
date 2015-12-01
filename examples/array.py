from z3 import *

# Create a new solver.
s = Solver()

# Create the variables.
a = Array('a', IntSort(), IntSort())
i1, i2, j, v1, v2 = Ints('i1 i2 j v1 v2')

# Add assertions.
s.add(i1 == j,
      i1 != i2,
      Select(a, j) == v1,
      Select(Store(Store(a, i1, v1), i2, v2), j) != a[j])

# Check satisfiability.
print s.check()
