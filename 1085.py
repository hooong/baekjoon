x, y, w, h = map(int, input().split())

length = [x,y,w-x,h-y]
length.sort()

print(length[0])