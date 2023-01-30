import sys
sys.stdin = open("input.txt", "r")

# 1 : 북, 2 : 남 -> 왼쪽부터 거리, 3 : 서, 4 : 동 -> 위쪽부터 거리
x, y = map(int, input().split())
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

x_, y_ = map(int, input().split())

def north(arr, y_):
    Sum = 0
    for i in arr:
        if i[0] == 1:

if x_ == 1:
    print(north(arr, y_))
elif x_ == 2:
    print(south(arr, y_))
elif x_ == 3:
    print(west(arr, y_))
else:
    print(east(arr, y_))