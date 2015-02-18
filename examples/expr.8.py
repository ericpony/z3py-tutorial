x = Const('x', IntSort())
print eq(x, Int('x'))

a, b = Consts('a b', BoolSort())
print And(a, b)
