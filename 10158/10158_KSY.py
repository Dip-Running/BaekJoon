w, h = map(int, input().split())    # 가로,세로
p, q = map(int, input().split())    # 초기값 좌표
t = int(input())                    # 개미가 움직일 시간

# 1시간에 1칸 움직이는 개미

# 델타 탐색?
# t 가 20000000인 경우 시간 초과가 난다!!!
dx, dy = 1, 1
for _ in range(t):
    p = p + dx
    q = q + dy
    if p == 0:  # 만약 x 좌표가 0이 되면
        dx = 1  # y좌표는 무조건 +1 이니까 디폴트 값
    elif p == w:    # 만약 x 좌표가 오른쪽 끝에 부딪히면
        dx = -1 # y 좌표는 무조건 +1
    if q == 0:  # y 좌표가 0이 되면
        dy = 1  # x좌표는 무조건 +1
    elif q == h:    # y 좌표가 위에 부딪히면
        dy = -1 # x 좌표는 무조건 +1
    print(p, q)
