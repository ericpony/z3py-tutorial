x = Int('x')
y = Int('y')
n = x + y >= 3
print "num args: ", n.num_args()
print "children: ", n.children()
print "1st child:", n.arg(0)
print "2nd child:", n.arg(1)
print "operator: ", n.decl()
print "op name:  ", n.decl().name()
