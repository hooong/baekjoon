x, y = map(int, input().split())

dic_mon = {'1':31, '2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31,
'9':30, '10':31, '11':30, '12':31}
dic_day = {'0':"MON", '1':"TUE", '2':"WED",'3':"THU", '4':"FRI", '5':"SAT", '6':"SUN"}

day = 0
for i in range(1,x):
    day += dic_mon[str(i)]

day += y

print(dic_day[str((day-1)%7)])