a, b, v = map(int, input().split())

x = (v-b) // (a-b)      # 올라갈때만 정상에 도착할 수 있으므로 v <= ax - b(x-1)로 x를 구해볼 수 있다.

if a*x - b*(x-1) >= v:  # 확인하여 계산해보면 x이거나 x+1있다.
    print(x)
else:
    print(x+1)