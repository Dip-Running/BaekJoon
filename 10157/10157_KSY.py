# 자리배정
C, R = map(int, input().split())    # 공연장의 크기 C * R
K = int(input())            # K : 관객의 대기 번호

if K > C * R:
    print(0)    # 만약 숫자들 보다 관객 번호가 크면 0을 출력

arr = [[0] * C for _ in range(R)]
dx = [-1, 0, 1, 0]  # 상우하좌
dy = [0, 1, 0, -1]
# 델타 탐색으로 달팽이 움직이기
i = C - 1   # i는 가장 아래이므로 C-1에서 시작
j = 0
k = 0
cnt = 1
while cnt < C * R + 1:
    ni = i + dx[k]
    nj = j + dy[k]
    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 0:  # 크기가 가로는 R까지 세로는 C까지이다
        arr[ni][nj] = cnt
        cnt += 1
        i, j = ni, nj
    else:
        k += 1  # 벽을 만나면 k를 다음요소로 옮겨주는데
        if k > 3:   # k가 3보다 크다면 인덱스 오류가 나니까
            k = k % 4   # k를 4로 나눈 나머지로 대신한다
print(arr)


for i in range(R):
    for j in range(C):
        if arr[i][j] == K:  # 관객번호랑 똑같은 숫자가 있다면
            print(C - i - 1, j + 1) # 0 5 -> 인데스 값을 어떻게 변경해야 하는거지?

