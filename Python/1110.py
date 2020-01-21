n = int(input())
first_n = n

c = 0
while True:
    k = (n//10) + (n%10)
    n = int(str(n%10) + str(k%10))
    c += 1
    if n == first_n:
        print(c)
        break