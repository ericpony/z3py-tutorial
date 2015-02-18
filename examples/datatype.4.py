Color, (red, green, blue) = EnumSort('Color', ('red', 'green', 'blue'))

print green == blue
print simplify(green == blue)

c = Const('c', Color)
solve(c != green, c != blue)
