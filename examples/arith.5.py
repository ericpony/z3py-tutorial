x, y = Reals('x y')
solve(x + 10000000000000000000000 == y, y > 20000000000000000)

print Sqrt(2) + Sqrt(3)
print simplify(Sqrt(2) + Sqrt(3))
print simplify(Sqrt(2) + Sqrt(3)).sexpr()
# The sexpr() method is available for any Z3 expression
print (x + Sqrt(y) * 2).sexpr()
