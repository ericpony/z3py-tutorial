from z3 import *

# Create the tree datatype.
Tree = Datatype('Tree')
TreeList = Datatype('TreeList')
Tree.declare('leaf', ('value', IntSort()))
Tree.declare('node', ('children', TreeList))
TreeList.declare('nil')
TreeList.declare('cons', ('car', Tree), ('cdr', TreeList))

Tree, TreeList = CreateDatatypes(Tree, TreeList)

print 'Tree.value(Tree.leaf(10)):'
print Tree.value(Tree.leaf(10))
print ''

print 'simplify(Tree.value(Tree.leaf(10))):'
print simplify(Tree.value(Tree.leaf(10)))
print ''

n1 = Tree.node(TreeList.cons(Tree.leaf(10), TreeList.cons(Tree.leaf(20), TreeList.nil)))
n2 = Tree.node(TreeList.cons(n1, TreeList.nil))
print 'n1 = Tree.node(TreeList.cons(Tree.leaf(10), TreeList.cons(Tree.leaf(20), TreeList.nil)))'
print 'n2 = Tree.node(TreeList.cons(n1, TreeList.nil))'
print ''

print 'simplify(n2 == n1):'
print simplify(n2 == n1)
print ''

print 'simplify(TreeList.car(Tree.children(n2)) == n1):'
print simplify(TreeList.car(Tree.children(n2)) == n1)
print ''
