x = Int('x')
print "is expression: ", is_expr(x)
n = x + 1
print "is application:", is_app(n)
print "decl:          ", n.decl()
print "num args:      ", n.num_args()
for i in range(n.num_args()):
    print "arg(", i, ") ->", n.arg(i)
