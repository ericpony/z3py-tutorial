
"""Please Fill the Input by following methods

If the (x, y) cell is filled with 'n' value,
then put 'pxyn' into the Input list

E.g. Consider following sudoku
  
  ------------------
4 |   | 4 ||   |   |
  --------||--------
3 |   |   || 4 |   |
  ==================
2 |   | 2 ||   |   |
  --------||--------
1 |   |   || 1 |   |
y ------------------
  x 1   2    3   4

(3, 1) cell is filled with 1
Hence 'p311' is in Input list
"""

Input = ['p222', 'p244', 'p311', 'p334']


""" Below is the flow to generate formaula """
I = ['1','2','3','4']
Is = [['1','2'], ['3','4']]

""" Check input integrity """
SI = set(I)
for p in Input:
    if not len(p) == 4 or p[0] != 'p' or not p[1] in SI or not p[2] in SI or not p[3] in SI:
        print('Error:' + p + 'is not a valid input.')

cls = [] """cls: the list of all conjucted clause"""
cls.extend(Input)
for i in I:
    for j in I:
        l = []
        for n in I:
            l.append('p'+i+j+n)
        cls.append( '(' + ('|'.join(l)) + ')' )

for i in I:
    for j in I:
        for n in I:
            for m in I:
                 if m != n:
                    cls.append('(p'+i+j+n+'->~'+'p'+i+j+m+')')
for n in I:
    for i in I:
        l = []
        for j in I:
            l.append('p'+i+j+n)
        cls.append('(' + ('|'.join(l)) +')')

for n in I:
    for j in I:
        l = []
        for i in I:
            l.append('p'+i+j+n)
        cls.append('(' + ('|'.join(l)) +')')

for k1 in Is:
    for k2 in Is:
        for n in I:
            l = []
            for i in k1:
                for j in k2:
                    l.append('p'+i+j+n)
            cls.append('(' + ('|'.join(l)) +')')

print('&'.join(cls))
