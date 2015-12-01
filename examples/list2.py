from z3 import *

# Create a solver.
s = Solver()

List = Datatype('List')

# Declare constructors.
List.declare('cons', ('car', IntSort()), ('cdr', List))
List.declare('nil')

# Create the datatype.
List = List.create()

# Create shorthands.
cons = List.cons
car = List.car
cdr = List.cdr
nil = List.nil

# Create an uninterpreted function 'atom'.
atom = Function('atom', List, BoolSort())

# Assert axioms for atom.
x = Const('x', List)
s.add(ForAll([x], Implies(Not(atom(x)), cons(car(x), cdr(x)) == x)))

x = Int('x')
y = Const('x', List)
s.add(ForAll([x, y], Not(atom(cons(x, y)))))

# Construct the example formula.
x = Const('x', List)
y = Const('y', List)
f = Function('f', List, List)

# Add assertions.
s.add(car(x) == car(y),
      cdr(x) == cdr(y),
      f(x) != f(y),
      Not(atom(x)),
      Not(atom(y)))

# Check satisfiability.
print s.check()
