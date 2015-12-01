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

# Create a list.
l = cons(2, cons(1, cons(0, nil)))

print 'simplify(l):'
print simplify(l)
print ''

print 'simplify(car(l)):'
print simplify(car(l))
print ''

print 'simplify(car(cdr(l))):'
print simplify(car(cdr(l)))
print ''
