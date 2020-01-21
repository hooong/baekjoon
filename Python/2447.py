import sys

n = int(input())

k = n//3

def draw(i,j,size):
    if (i//size)%3 == 1 and (j//size)%3 == 1:
        sys.stdout.write(' ')
    else:
        if size//3 == 0:
            sys.stdout.write('*')
        else:
            draw(i,j,size//3)

for i in range(n):
    for j in range(n):
        draw(i,j,n)
    sys.stdout.write('\n')
