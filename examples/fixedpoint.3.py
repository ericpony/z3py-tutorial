fp = Fixedpoint()
fp.set(engine='datalog')

s = BitVecSort(3)
edge = Function('edge', s, s, BoolSort())
path = Function('path', s, s, BoolSort())
a = Const('a',s)
b = Const('b',s)
c = Const('c',s)

fp.register_relation(path,edge)
fp.declare_var(a,b,c)
fp.rule(path(a,b), edge(a,b))
fp.rule(path(a,c), [edge(a,b),path(b,c)])

v1 = BitVecVal(1,s)
v2 = BitVecVal(2,s)
v3 = BitVecVal(3,s)
v4 = BitVecVal(4,s)

fp.fact(edge(v1,v2))
fp.fact(edge(v1,v3))
fp.fact(edge(v2,v4))

print "current set of rules", fp


print fp.query(path(v1,v4)), "yes we can reach v4 from v1"

print fp.query(path(v3,v4)), "no we cannot reach v4 from v3"

