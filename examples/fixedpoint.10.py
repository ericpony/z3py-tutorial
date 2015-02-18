
# let max max2 x y z = max2 (max2 x y) z
# let f x y = if x > y then x else y
# assert (f (max f x y z) x) = (max f x y z)


Expr = Datatype('Expr')
Expr.declare('Max')
Expr.declare('f')
Expr.declare('I', ('i', IntSort()))
Expr.declare('App', ('fn',Expr),('arg',Expr))
Expr = Expr.create()
Max  = Expr.Max
I    = Expr.I
App  = Expr.App
f    = Expr.f
Eval = Function('Eval',Expr,Expr,Expr,BoolSort())

x   = Const('x',Expr)
y   = Const('y',Expr)
z   = Const('z',Expr)
r1  = Const('r1',Expr)
r2  = Const('r2',Expr)
max = Const('max',Expr)
xi  = Const('xi',IntSort())
yi  = Const('yi',IntSort())

fp = Fixedpoint()
fp.register_relation(Eval)
fp.declare_var(x,y,z,r1,r2,max,xi,yi)

# Max max x y z = max (max x y) z
fp.rule(Eval(App(App(App(Max,max),x),y), z, r2),
	[Eval(App(max,x),y,r1),
	 Eval(App(max,r1),z,r2)])

# f x y = x if x >= y
# f x y = y if x < y
fp.rule(Eval(App(f,I(xi)),I(yi),I(xi)),xi >= yi)
fp.rule(Eval(App(f,I(xi)),I(yi),I(yi)),xi < yi)

print fp.query(And(Eval(App(App(App(Max,f),x),y),z,r1),
		   Eval(App(f,x),r1,r2),
		   r1 != r2))

print fp.get_answer()
