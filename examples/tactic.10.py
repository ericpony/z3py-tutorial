t = Then('simplify', 
         'normalize-bounds', 
         'solve-eqs')

x, y, z = Ints('x y z')
g = Goal()
g.add(x > 10, y == x + 3, z > y)

r = t(g)
# r contains only one subgoal
print r

s = Solver()
s.add(r[0])
print s.check()
# Model for the subgoal
print s.model()
# Model for the original goal
print r.convert_model(s.model())
