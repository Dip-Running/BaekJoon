import sys
sys.stdin = open('input10157.txt')
sys.setrecursionlimit(10**6)
###재귀로 못품

def check(row, col, cnt, start_lst, final): # 한바퀴 돌기
    # col > row -1 > col -1> row -2> col -2> row -3
    for r in range(start_lst[1], col + start_lst[1]): # 1 col번
        if cnt == final:
            return start_lst
        cnt += 1
        start_lst = [start_lst[0], r]
        #print(start_lst, end= ' ')
    for c in range(start_lst[0] + 1, row + start_lst[0]): # 2 row -1 번
        if cnt == final:
            return start_lst
        cnt += 1
        start_lst = [c, start_lst[1]]
        #print(start_lst, end= ' ')
    # print('b')
    for r in range(start_lst[1] - 1, start_lst[1] - col, -1): # 3 col - 1번
        if cnt == final:
            return start_lst
        cnt += 1
        start_lst = [start_lst[0], r]
        #print(start_lst, end= ' ')
    for c in range(start_lst[0] - 1, start_lst[1], -1): # 4 row - 2번
        if cnt == final:
            return start_lst
        cnt += 1
        start_lst = [c, start_lst[1]]
        #print(start_lst, end= ' ')
    #print('a', end= '    ')
    return check(row - 2, col - 2, cnt, [start_lst[0], start_lst[1] + 1], final)
    
    

for i in range(3):
    row, col = map(int, input().split())
    n = int(input())
    count = 0

    if row * col < n:
        print('0')
    else:
        a = check(row, col, count, [1,1], n)
        print(a[0], a[1])
