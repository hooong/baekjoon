s = input()
i = 0

count = 0

while i < len(s):
    # =,-을 잡아냄.
    if s[i] in ['=', '-']:
        # dz=을 잡아내기 위해서 이러면 count를 1 감소
        if i > 1 and s[i-2] == 'd' and s[i-1]=='z':
            count -= 1
        i += 1
        continue
    # lj,nj를 잡아냄.
    elif i>0 and s[i] == 'j':
        if s[i-1] in ['l', 'n']:
            i += 1
            continue
    count += 1
    i += 1

print(count)