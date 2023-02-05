import sys
sys.stdin = open('input.txt')

n = int(input())
cnt = 1
arr = list(map(int, input().split()))
lst = []
for i in arr:
    lst.insert(-i, cnt)
    cnt += 1

for i in lst:
    print(i, end=' ')