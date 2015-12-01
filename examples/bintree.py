from z3 import *

# Create a solver.
s = Solver()

# Create the binary tree datatype.
BinaryTree = Datatype('BinaryTree')
BinaryTree.declare('leaf', ('value', IntSort()))
BinaryTree.declare('node', ('value', IntSort()), ('left', BinaryTree), ('right', BinaryTree))
BinaryTree = BinaryTree.create()

# Shorthands.
leaf = BinaryTree.leaf
node = BinaryTree.node
value = BinaryTree.value
left = BinaryTree.left
right = BinaryTree.right

# Create an instance of a binary tree.
t = node (2, (leaf(0)), (leaf(1)))

print 'Values:'
print simplify(value(t))
print simplify(value(left(t)))
print ''

## print 'Constructors:'
## print BinaryTree.constructor(0)
## print BinaryTree.constructor(1)
## print ''

## print 'Accessors:'
## print BinaryTree.accessor(0, 0)
## print BinaryTree.accessor(1, 0)
## print BinaryTree.accessor(1, 1)
## print BinaryTree.accessor(1, 2)
## print ''

## lv = BinaryTree.accessor(0, 0)
## nv = BinaryTree.accessor(1, 0)

## def value(t):
##    if is_true(simplify(BinaryTree.is_leaf(t))):
##        return lv(t)
##    else:
##        return nv(t)

## print 'Values:'
## print simplify(value(t))
## print simplify(value(left(t)))
## print ''

## value = lambda t: If(is_true(simplify(BinaryTree.is_leaf(t))), lv(t), nv(t))

## print 'Values:'
## print simplify(value(t))
## print simplify(value(left(t)))
## print ''
