# 1436번 영화감독 숌

# main
n = int(input())

arr = [666]

i = arr[0]+1
while True: 
    if len(arr) == n:
        print(arr[-1])
        break

    str_n = str(i)
    if not str_n.find('666') == -1:
        arr.append(int(i))
        
    i += 1
