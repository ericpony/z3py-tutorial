
fp = Fixedpoint()

a, b, c = Bools('a b c')

fp.register_relation(a.decl(), b.decl(), c.decl())
fp.rule(a,b)
fp.rule(b,c)
fp.fact(c)
fp.set(generate_explanations=True, engine='datalog')
print fp.query(a)
print fp.get_answer()

