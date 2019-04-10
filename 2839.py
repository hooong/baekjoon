sugar = int(input())

n = -1 
i=0
sugar_m = sugar
while sugar_m >= 3:
    sugar_m = sugar - (5*i)
    if sugar_m%5 == 0:
        n = sugar_m//5 + i
        break
    elif sugar_m%3 == 0:
        n = sugar_m//3 + i
        i += 1
        continue
    else:
        if sugar_m > 5:
            i += 1
            continue
        else:
            break

print(n)