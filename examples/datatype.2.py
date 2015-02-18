def DeclareList(sort):
    List = Datatype('List_of_%s' % sort.name())
    List.declare('cons', ('car', sort), ('cdr', List))
    List.declare('nil')
    return List.create()

IntList     = DeclareList(IntSort())
RealList    = DeclareList(RealSort())
IntListList = DeclareList(IntList)

l1 = IntList.cons(10, IntList.nil)
print l1
print IntListList.cons(l1, IntListList.cons(l1, IntListList.nil))
print RealList.cons("1/3", RealList.nil)

print l1.sort()
