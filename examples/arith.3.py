x, y = Reals('x y')
# Put expression in sum-of-monomials form
t = simplify((x + y)**3, som=True)
print t
# Use power operator
t = simplify(t, mul_to_power=True)
print t


