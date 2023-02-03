##temp##
##Not Done!!!##
import sys
sys.stdin = open('input.txt', 'r')

col, row = map(int, input().split())
seat = int(input())

# 좌석 배치 못하면 바로 끝
if seat > col * row:
    print(0)
    exit()
# 그리드 설정
grid = [[0] * col for _ in range(row)]
# 상[0]하[1]좌[2]우[3] 설정
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
