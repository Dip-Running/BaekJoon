# import sys
# sys.stdin = open('input.txt', 'r')

col, row = map(int, input().split())
seat = int(input())

# 좌석 배치 못하면 바로 끝
if seat > col * row:
    print(0)
    exit()
# 그리드 설정
##grid 맨아랫줄 기준으로 뒤집어서 좌표 잡음##
grid = [[0] * col for _ in range(row)]
posx, posy = 0, 0   # 현재 좌표 설정
grid[posx][posy] = 1    # 현재 대기순번 입력
# 하[0]우[1]상[2]좌[3] 설정
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
turn = 0 # 이동방향 인덱스
# 1번째 대기순번은 맞춰놨으니 2번째부터, seat(포함)까지 반복
for i in range(2, seat + 1):
    while True:
        nx = posx + dx[turn]    # 가고자 하는 위치 임의 설정
        ny = posy + dy[turn]
        if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0: # grid 내에 있으면
            grid[nx][ny] = i    # 가고자 하는 위치에 대기순번 입력
            posx = nx   # 임의로 설정한 위치를 내 현재 위치로 변경
            posy = ny
            break   # while 탈출
        else:
            turn = (turn + 1) % 4
print(posy + 1, posx + 1)