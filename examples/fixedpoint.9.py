set_option(relevancy=0,verbose=1)

def flatten(l):
    return [s for t in l for s in t]


class TransitionSystem():
    def __init__(self, initial, transitions, vars1):
	self.fp = Fixedpoint()        
	self.initial     = initial
	self.transitions = transitions
	self.vars1 = vars1

    def declare_rels(self):
	B = BoolSort()
	var_sorts   = [ v.sort() for v in self.vars1 ]
	state_sorts = var_sorts
	self.state_vals = [ v for v in self.vars1 ]
	self.state_sorts  = state_sorts
	self.var_sorts = var_sorts
	self.state  = Function('state', state_sorts + [ B ])
	self.step   = Function('step',  state_sorts + state_sorts + [ B ])
	self.fp.register_relation(self.state)
	self.fp.register_relation(self.step)

# Set of reachable states are transitive closure of step.

    def state0(self):
	idx = range(len(self.state_sorts))
	return self.state([Var(i,self.state_sorts[i]) for i in idx])
	
    def state1(self):
	n = len(self.state_sorts)
	return self.state([Var(i+n, self.state_sorts[i]) for i in range(n)])

    def rho(self):
	n = len(self.state_sorts)
	args1 = [ Var(i,self.state_sorts[i]) for i in range(n) ]
	args2 = [ Var(i+n,self.state_sorts[i]) for i in range(n) ]
	args = args1 + args2 
	return self.step(args)

    def declare_reachability(self):
	self.fp.rule(self.state1(), [self.state0(), self.rho()])


# Define transition relation

    def abstract(self, e):
	n = len(self.state_sorts)
	sub = [(self.state_vals[i], Var(i,self.state_sorts[i])) for i in range(n)]
	return substitute(e, sub)
	
    def declare_transition(self, tr):
	len_s  = len(self.state_sorts)
	effect = tr["effect"]
	vars1  = [Var(i,self.state_sorts[i]) for i in range(len_s)] + effect
	rho1  = self.abstract(self.step(vars1))
	guard = self.abstract(tr["guard"])
	self.fp.rule(rho1, guard)
	
    def declare_transitions(self):
	for t in self.transitions:
	    self.declare_transition(t)

    def declare_initial(self):
	self.fp.rule(self.state0(),[self.abstract(self.initial)])
	
    def query(self, query):
	self.declare_rels()
	self.declare_initial()
	self.declare_reachability()
	self.declare_transitions()
	query = And(self.state0(), self.abstract(query))
	print self.fp
	print query
	print self.fp.query(query)
	print self.fp.get_answer()
#	print self.fp.statistics()


L = Datatype('L')
L.declare('L0')
L.declare('L1')
L.declare('L2')
L = L.create()
L0 = L.L0
L1 = L.L1
L2 = L.L2


y0 = Int('y0')
y1 = Int('y1')
l  = Const('l', L)
m  = Const('m', L)


t1 = { "guard" : l == L0,
       "effect" : [ L1, y1 + 1, m, y1 ] }
t2 = { "guard" : And(l == L1, Or([y0 <= y1, y1 == 0])),
       "effect" : [ L2, y0,     m, y1 ] }
t3 = { "guard" : l == L2,
       "effect" : [ L0, IntVal(0), m, y1 ]}
s1 = { "guard" : m == L0,
       "effect" : [ l,  y0, L1, y0 + 1 ] }
s2 = { "guard" : And(m == L1, Or([y1 <= y0, y0 == 0])),
       "effect" : [ l,  y0, L2, y1 ] }
s3 = { "guard" : m == L2,
       "effect" : [ l,  y0, L0, IntVal(0) ]}


ptr = TransitionSystem( And(l == L0, y0 == 0, m == L0, y1 == 0),
			[t1, t2, t3, s1, s2, s3],
			[l, y0, m, y1])

ptr.query(And([l == L2, m == L2 ]))

