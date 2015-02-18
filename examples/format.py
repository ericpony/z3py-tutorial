x = IntVector('x', 20)
y = IntVector('y', 20)
f = And(Sum(x) >= 0, Sum(y) >= 0)

set_option(max_args=5)
print "\ntest 1:"
print f

print "\ntest 2:"
set_option(max_args=100, max_lines=10)
print f

print "\ntest 3:"
set_option(max_width=300)
print f

