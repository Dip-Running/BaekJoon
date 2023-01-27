#주사위 쌓기
# 문제 못품 : 시간관계상 다음으로 넘어감
import sys
sys.stdin = open("input.txt", "r")
Sum = 0
ceil = 0
bottom = 0
n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    if i == 0:
        ceil = arr.pop(arr.index(min(arr)))
        bottom = -1
        Sum += max(arr)
    else:
        bottom = ceil
        if bottom == arr[0]:
            ceil = arr[5]
        elif bottom == arr[1]:
            ceil = arr[3]
        elif bottom == arr[2]:
            ceil = arr[4]
        elif bottom == arr[3]:
            ceil = arr[1]
        elif bottom == arr[4]:
            ceil = arr[2]
        elif bottom == arr[5]:
            ceil = arr[0]
        print(arr)
        print(f'bottom : {bottom}, bottom.index : {arr.index(bottom)}, ceil : {ceil}, ceil.index : {arr.index(ceil)}')
        arr.pop(arr.index(bottom))
        arr.pop(arr.index(ceil))
        print(arr, '\n')
        Sum += max(arr)

print(Sum)