fp = Fixedpoint()

a, b, c = Bools('a b c')

fp.register_relation(a.decl(), b.decl(), c.decl())
fp.rule(a,b)
fp.rule(b,c)
fp.set(engine='datalog')

print "current set of rules\n", fp
print fp.query(a)

fp.fact(c)
print "updated set of rules\n", fp
print fp.query(a)
print fp.get_answer()
