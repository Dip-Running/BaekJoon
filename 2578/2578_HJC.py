# import sys
# sys.stdin = open('input.txt', 'r')
#---------------
# import sys
# from pprint import pprint

def check_bingo(Ans):
    bingo = 0
    row = [0]*5

    for a in range(5):
        if sum(Ans[a]) == 0:
            bingo += 1
        for b in range(5):
            row[a] += Ans[b][a]
    for i in range(5):
        if row[i] == 0:
            bingo += 1
    if Ans[0][4] + Ans[1][3] + Ans[2][2] + Ans[3][1] + Ans[4][0] == 0:
        bingo += 1
    if Ans[0][0] + Ans[1][1] + Ans[2][2] + Ans[3][3] + Ans[4][4] == 0:
        bingo += 1
    return bingo

arr = [list(map(int, input().split())) for _ in range(5)]
Ansarr = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            if Ansarr[i][j] in arr[k]:
                arr[k][arr[k].index(Ansarr[i][j])] = 0
        cnt += 1
        if check_bingo(arr) >= 3:
            print(cnt)
            exit()
