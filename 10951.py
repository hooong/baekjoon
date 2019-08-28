# 방법 1
# try:
#     while True:
#         a, b = map(int, input().split())
#         print(a+b)
# except:
#     exit()

# 방법 2
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)