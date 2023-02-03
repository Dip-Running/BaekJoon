# import sys
# sys.stdin = open('input.txt', 'r')

coords = []
cnt = [[0] * 101 for _ in range(101)]
Sum = 0
for i in range(4):
    coords.append(list(map(int, input().split())))
# print(coords)
for i in range(len(coords)):
    for j in range(coords[i][0], coords[i][2]):
        for k in range(coords[i][1], coords[i][3]):
            cnt[j][k] = 1
for i in range(101):
    for j in range(101):
        if cnt[i][j] == 1:
            Sum += 1
print(Sum)
