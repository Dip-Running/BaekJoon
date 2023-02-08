import sys
sys.stdin = open('input.txt', 'r')
#-------------------#
import sys
input = sys.stdin.readline
'''
1001 * 1001 사이즈 빈 리스트(-1) 만들고 n개의 색종이면 0, 1, 2, --- n으로 배열 값 할당
전체 이중 반복문 돌면서 탐색
'''
n = int(input())
M = 1001    # 전체 사이즈 설정
# 2차원 배열 입력 : 색종이 수 만큼, 하나의 색종이 정보를 1차원 리스트로 받음
arr = [list(map(int, input().split()))for _ in range(n)]
# 전체 사이즈만큼 -1로 초기화
grid = [[-1] * M for _ in range(M)]

# 상위 반복문 하나는 색종이 갯수만큼 반복하는거
for i in range(len(arr)):
    x, y, w, h = arr[i]
    # 여기서부터 이중 반목문이 해당 범위에 i로 배열 값 할당
    for x_ in range(x, x + w):
        for y_ in range(y, y + h):
            grid[x_][y_] = i

# 탐색 코드
cnt = [0] * len(arr)    # 색종이 수만큼 cnt length 설정, 0으로 초기화
# 모든 포인트(인덱스) 들에 대해서
for i in range(M):
    for j in range(M):
        # 0, 1, 2, 3, --- n인게 있는지(색종이 보이는지 확인)
        for k in range(len(cnt)):
            if grid[i][j] == k:
                cnt[k] += 1 # 각자 n번째 색종이 카운트 리스트에 += 1
for i in cnt:
    print(i)    # 전체 0부터 n까지 카운트들 출력