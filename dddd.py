def space(n):
    for i in range(n-3):
        print(" ", end='')

def first(): 
    print("  *  ", end=' ')

def second():
    print(" * * ", end=' ')

def third():
    print("*****", end=' ')

def ast_3():
    first()
    second()
    third()

def ast(n):
    for i in range(n//3):
        space(n-(i*3))
        for j in range(i+1):
            first()
            space(n-(i*3))
        print()
        space(n-(i*3))
        for j in range(i+1):
            second()
            space(n-(i*3))
        print()
        space(n-(i*3))
        for j in range(i+1):
            third()
            space(n-(i*3))
        print()

n = int(input())
ast(n)