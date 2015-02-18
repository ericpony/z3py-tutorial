x   = Int('x')
x_d = x.decl()
print "is_expr(x_d):     ", is_expr(x_d)
print "is_func_decl(x_d):", is_func_decl(x_d)
print "x_d.name():       ", x_d.name()
print "x_d.range():      ", x_d.range()
print "x_d.arity():      ", x_d.arity()
# x_d() creates an application with 0 arguments using x_d.
print "eq(x_d(), x):     ", eq(x_d(), x)
print "\n"
# f is a function from (Int, Real) to Bool
f   = Function('f', IntSort(), RealSort(), BoolSort())
print "f.name():         ", f.name()
print "f.range():        ", f.range()
print "f.arity():        ", f.arity()
for i in range(f.arity()):
    print "domain(", i, "): ", f.domain(i)
# f(x, x) creates an application with 2 arguments using f.
print f(x, x)
print eq(f(x, x).decl(), f)
