"""template.py
This is a template"""

def toStrConj(List):
    assert List != []
    clauseStr = '('
    for lit in List:
        clauseStr += lit
        clauseStr += ' and '
    clauseStr += ' (TRUE or -TRUE))'
    return clauseStr

def toStrDisj(List):
    assert List != []
    clauseStr = '('
    for lit in List:
        clauseStr += lit
        clauseStr += ' or '
    clauseStr += '(TRUE and -TRUE) )'

    return clauseStr

    
def toStrCNF(ListList):
    """Convert a formula in CNF represented as a list of list to
    string representation."""
    assert ListList != []
    # Convert each clause into str
    ListStr = [ toStrDisj(disj) for disj in ListList ]
    # Convert the conjunction of things into str
    StrStr = toStrConj(ListStr)

    return StrStr

def main():
    # Specify your value n
    n = 8

    # Preprocessing
    n += 1 # because of Python end range

    # Construct first constraint
    C1a = [[ 'p' + str(i) + 'd' + str(j) for j in range(1,n) ] for i in \
            range(1,n)]
    strC1a = toStrCNF(C1a)

    C1b = [ '(p'+str(i)+'d'+str(j)+' => -p'+str(i)+'d'+str(k)+')' for i in \
            range(1,n) for j in range(1,n) for k in range(1,n) if k != j ]
    strC1b = toStrConj(C1b)

    # Construct second constraint
    C2a = [[ 'p' + str(i) + 'd' + str(j) for i in range(1,n) ] for j in \
            range(1,n)]
    strC2a = toStrCNF(C2a)

    C2b = [ '(p'+str(i)+'d'+str(j)+' => -p'+str(k)+'d'+str(j)+')' for i in \
            range(1,n) for j in range(1,n) for k in range(1,n) if k != i ]
    strC2b = toStrConj(C2b)

    # Construct third constraint
    # -45-deg diag constraint
    C3a = [ '(p'+str(i)+'d'+str(j)+' => -p'+str(i+k)+'d'+str(j+k)+')' for i in\
            range(1,n) for j in range(1,n) for k in range(1,n) \
            if 1 <= (i+k) and (i+k) < n and 1 <= (j+k) and (j+k) < n ]
    strC3a = toStrConj(C3a)

    C3b = [ '(p'+str(i)+'d'+str(j)+' => -p'+str(i-k)+'d'+str(j-k)+')' for i in\
            range(1,n) for j in range(1,n) for k in range(1,n) \
            if 1 <= (i-k) and (i-k) < n and 1 <= (j-k) and (j-k) < n ]
    strC3b = toStrConj(C3b)

    # Construct fourth constraint
    # 45-deg diag constraint
    C4a = [ '(p'+str(i)+'d'+str(j)+' => -p'+str(i+k)+'d'+str(j-k)+')' for i in\
            range(1,n) for j in range(1,n) for k in range(1,n) \
            if 1 <= (i+k) and (i+k) < n and 1 <= (j-k) and (j-k) < n ]
    strC4a = toStrConj(C4a)

    C4b = [ '(p'+str(i)+'d'+str(j)+' => -p'+str(i-k)+'d'+str(j+k)+')' for i in\
            range(1,n) for j in range(1,n) for k in range(1,n) \
            if 1 <= (i-k) and (i-k) < n and 1 <= (j+k) and (j+k) < n ]
    strC4b = toStrConj(C4b)

    #C2 = [[ 'p' + str(i) + 'd' + str(j) for j in range(1,n) ] for i in \
            #range(1,n)]
    # ListStrC1 = [ toStrDisj(disj) for disj in ListListC1 ]
    # StrStrC1 = toStrConj(ListStrC1)
    print toStrConj([strC1a,strC1b,strC2a,strC2b,strC3a,strC3b,strC4a,strC4b])

if __name__ == '__main__':
    main()
