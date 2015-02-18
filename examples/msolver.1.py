x, y = Ints('x y')
s1 = Solver()
s1.add(x > 10, y > 10)
s2 = Solver()
# solver s2 is empty
print s2
# copy assertions from s1 to s2
s2.add(s1.assertions())
print s2
