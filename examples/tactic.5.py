x, y, z = Reals('x y z')
g = Goal()
g.add(Or(x == 0, x == 1), 
      Or(y == 0, y == 1), 
      Or(z == 0, z == 1),
      x + y + z > 2)

# Split all clauses"
split_all = Repeat(OrElse(Tactic('split-clause'),
                          Tactic('skip')))
for s in split_all(g):
    print s
