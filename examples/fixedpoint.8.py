
mc = Function('mc', IntSort(), IntSort(), BoolSort())
n, m, p = Ints('n m p')

fp = Fixedpoint()

fp.declare_var(n,m)
fp.register_relation(mc)

fp.rule(mc(m, m-10), m > 100)
fp.rule(mc(m, n), [m <= 100, mc(m+11,p),mc(p,n)])
    
print fp.query(And(mc(m,n),n < 90))
print fp.get_answer()

print fp.query(And(mc(m,n),n < 91))
print fp.get_answer()

print fp.query(And(mc(m,n),n < 92))
print fp.get_answer()
