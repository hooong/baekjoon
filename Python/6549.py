# 6549번 히스토그램에서 가장 큰 직사각형

# 분할
def devide(start, end):
    global max_area, histo

    dhisto = histo[start:end]
    min_height = min(dhisto)
    min_index = dhisto.index(min_height) + start

    part_max = min_height * len(dhisto)
    if part_max > max_area:
        max_area = part_max

    if end - start == 1:
        return
    else:
        if start < min_index:
            devide(start, min_index)
        if min_index+1 < end:
            devide(min_index+1, end)

# main
while True:
    histo = list(map(int,input().split()))
    n = histo.pop(0)

    if n == 0:
        exit()

    max_area = 0
    devide(0,n)

    print(max_area)
    