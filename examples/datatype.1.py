# Declare a List of integers
List = Datatype('List')
# Constructor cons: (Int, List) -> List
List.declare('cons', ('car', IntSort()), ('cdr', List))
# Constructor nil: List
List.declare('nil')
# Create the datatype
List = List.create()
print is_sort(List)
cons = List.cons
car  = List.car
cdr  = List.cdr
nil  = List.nil
# cons, car and cdr are function declarations, and nil a constant
print is_func_decl(cons)
print is_expr(nil)

l1 = cons(10, cons(20, nil))
print l1
print simplify(cdr(l1))
print simplify(car(l1))
print simplify(l1 == nil)
