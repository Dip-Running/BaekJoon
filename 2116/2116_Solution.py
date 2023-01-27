# 종류가 같은 주사위도 있을 수 있다
import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
reverse=[5, 3, 4, 1, 2, 0]
ans = 0
for floor in range(1, 7):
    Sum = 0
    for th in arr:
        top = th[reverse[th.index(floor)]]
        if floor + top == 11:
            Sum += 4
        elif floor == 6 or top == 6:
            Sum += 5
        else:
            Sum += 6
        floor = top
    if Sum > ans:
        ans = Sum
print(ans)