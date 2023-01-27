#import sys
#sys.stdin = open("input.txt", "r")
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, -1)
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    if x == 1:
        for i in range(y, n+1, y):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
    if x == 2:
        if arr[y] == 0:
            arr[y] = 1
        else:
            arr[y] = 0
        '''cnt = 1
        while y-cnt >= 0 and y+cnt < n:
            if arr[y-cnt] == arr[y+cnt]:
                if arr[y-cnt] == 0:
                    arr[y-cnt] = 1
                    arr[y+cnt] = 1
                else:
                    arr[y - cnt] = 0
                    arr[y + cnt] = 0
            cnt += 1'''
        for k in range(n // 2):
            if y + k > n or y - k < 1: break
            if arr[y + k] == arr[y - k]:
                if arr[y+k] == 0:
                    arr[y-k] = 1
                    arr[y+k] = 1
                else:
                    arr[y+k] = 0
                    arr[y-k] = 0
            else:
                break
arr.pop(0)
for i in arr:
    print(i, end=' ')