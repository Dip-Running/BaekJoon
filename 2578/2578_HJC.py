##temp##
###not done###
import sys
sys.stdin = open('input.txt', 'r')
#---------------
import sys
from pprint import pprint

def check_bingo(ans):
    bingo = 0
    Sum = 0
    for i in range(5):
        if sum(ans[i]) == 0:
            bingo += 1
            print("가로")
        Sum += ans[i][0]
    if Sum == 0:
        bingo += 1
        print('세로')
    if ans[0][4] + ans[1][3] + ans[2][2] + ans[3][1] + ans[4][0] == 0:
        bingo += 1
        print('오른쪽 위에서 왼쪽 아래')
    if ans[0][0] + ans[1][1] + ans[2][2] + ans[3][3] + ans[4][4] == 0:
        bingo += 1
        print('왼쪽 위에서 오른쪽 아래')
    return bingo

arr = [[0]*5 for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))
Ansarr = [[0] * 5 for _ in range(5)]
for i in range(5):
    Ansarr[i] = list(map(int, input().split()))
cnt = 0

ans = [[0] * 5 for _ in range(5)]
bingo_cnt = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            if Ansarr[i][j] in arr[k]:
                arr[k][arr[k].index(Ansarr[i][j])] = 0
            pprint(arr)
        cnt += 1
        bingo_cnt += check_bingo(arr)
        if bingo_cnt >= 3:
            print(cnt)
            sys.exit()