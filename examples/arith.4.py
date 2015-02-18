x, y = Reals('x y')
# Using Z3 native option names
print simplify(x == y + 2, ':arith-lhs', True)
# Using Z3Py option names
print simplify(x == y + 2, arith_lhs=True)

print "\nAll available options:"
help_simplify()

