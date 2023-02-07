import sys
sys.stdin = open('input.txt', 'r')
#-------------------#
import sys
input = sys.stdin.readline
import math
num, room_size = map(int, input().split())
# 6*2 배열 선언하고
arr = [[0]*6 for _ in range(2)]
# 입력 받으면서 인덱싱 주의하면서 하나씩 값 추가함
for i in range(num):
    x, y = map(int, input().split())
    arr[x][y-1] += 1
    
# 여기서 카운트
cnt = 0
for i in range(2):
    for j in range(6):
        cnt += math.ceil(arr[i][j]/room_size)#올림 씀
print(cnt)