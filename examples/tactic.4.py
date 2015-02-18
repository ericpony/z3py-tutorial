x, y, z = Reals('x y z')
g = Goal()
g.add(Or(x == 0, x == 1), 
      Or(y == 0, y == 1), 
      Or(z == 0, z == 1),
      x + y + z > 2)

# Split all clauses"
split_all = Repeat(OrElse(Tactic('split-clause'),
                          Tactic('skip')))
print split_all(g)

split_at_most_2 = Repeat(OrElse(Tactic('split-clause'),
                          Tactic('skip')),
                         1)
print split_at_most_2(g)

# Split all clauses and solve equations
split_solve = Then(Repeat(OrElse(Tactic('split-clause'),
                                 Tactic('skip'))),
                   Tactic('solve-eqs'))

print split_solve(g)
