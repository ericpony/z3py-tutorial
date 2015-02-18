TreeList = Datatype('TreeList')
Tree     = Datatype('Tree')
Tree.declare('leaf', ('val', IntSort()))
Tree.declare('node', ('left', TreeList), ('right', TreeList))
TreeList.declare('nil')
TreeList.declare('cons', ('car', Tree), ('cdr', TreeList))

Tree, TreeList = CreateDatatypes(Tree, TreeList)

t1  = Tree.leaf(10)
tl1 = TreeList.cons(t1, TreeList.nil)
t2  = Tree.node(tl1, TreeList.nil)
print t2
print simplify(Tree.val(t1))

t1, t2, t3 = Consts('t1 t2 t3', TreeList)

solve(Distinct(t1, t2, t3))
