from z3 import *

s = Solver()

i = BitVec('in', 32)

F = Function('F', BitVecSort(32), BitVecSort(32))
G = Function('G', BitVecSort(32), BitVecSort(32))
H = Function('H', BitVecSort(32), BitVecSort(32))
K = Function('K', BitVecSort(32), BitVecSort(32))
C = Function('C', BitVecSort(32), BoolSort())
D = Function('D', BitVecSort(32), BitVecSort(32))
L1, L2, L3, L4, L5 = Consts('L1 L2 L3 L4 L5', BitVecSort(32))
L1p, L3p, L5p = Consts('L1p L3p L5p', BitVecSort(32))
L2p = Const('L2p', BoolSort())

s.add(L1 == F(i),
      L2 == L1,
      L3 == K(G(L1)),
      L4 == H(L1),
      L5 == If(C(L2), L3, D(L4)))
s.add(L1p == F(i),
      L2p == C(L1p),
      L3p == If(C(L1p), G(L1p), H(L1p)),
      L5p == If(L2p, K(L3p), D(L3p)))
s.add(L5 != L5p)

print s.check()
