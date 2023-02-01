# 100 * 100 사이즈 위에 10 * 10 검은 도화지
import sys

sys.stdin = open("input.txt", "r")
# 정수 입력
N = int(input())
# 100 * 100 배열 만들고 0으로 초기화
arr = [[0] * 100 for _ in range(100)]

cnt = 0
# 입력받은 x, y 좌표에 대해 10만큼 반복하며 arr의 해당 범위를 1로 변경
for i in range(N):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            arr[x+j][y+k] = 1
# 다시 쭉 돌면서 1 있으면 카운트
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
#카운트 출력하고 종료
print(cnt)