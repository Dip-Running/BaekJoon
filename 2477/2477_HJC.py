# 2477번
# import sys
# sys.stdin = open("input.txt", "r")
# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
n = int(input())
# 2차원 배열 입력
arr = [list(map(int, input().split())) for _ in range(6)]
# 가로 또는 세로 최대 길이 양옆에는 세로 또는 가로가 오니까
# 가로 세로 최대 길이 곱 - 최대 양옆 뺀 값끼리 곱
wid_max = 0
hei_max = 0
#최댓값일때의 인덱스 저장 변수
wid_ind, hei_ind = 0, 0
for i in range(len(arr)):
  dir = arr[i][0]
  if dir == 1 or dir == 2:
    if wid_max < arr[i][1]:
      wid_max = arr[i][1]
      wid_ind = i
  elif dir == 3 or dir == 4:
    if hei_max < arr[i][1]:
      hei_max = arr[i][1]
      hei_ind = i
# 뺄 때 % 6 한거는 wid_ind - 1이 음수가 나오거나
# wid_ind+1이 7이 나와도 나머지 연산자 써서 index error잡음
subW = abs(arr[(wid_ind-1) % 6][1] - arr[(wid_ind+1) % 6][1])
subH = abs(arr[(hei_ind-1) % 6][1] - arr[(hei_ind+1) % 6][1])
print(((wid_max * hei_max) - (subW * subH)) * n)
