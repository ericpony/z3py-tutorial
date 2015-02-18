s = Then(With('simplify', arith_lhs=True, som=True),
         'normalize-bounds', 'lia2pb', 'pb2bv', 
         'bit-blast', 'sat').solver()
x, y, z = Ints('x y z')
solve_using(s, 
            x > 0, x < 10, 
            y > 0, y < 10, 
            z > 0, z < 10,
            3*y + 2*x == z)
# It fails on the next example (it is unbounded)
s.reset()
solve_using(s, 3*y + 2*x == z)
