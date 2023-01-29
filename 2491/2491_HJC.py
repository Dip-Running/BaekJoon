# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))

ans, down_cnt, up_cnt = 2, 1, 1
# 지금 수랑 전 수랑 비교, 작아지면 down_cnt ++, 커지면 up_cnt ++
# 꺾이면 cnt = 1로 초기화
# 답은 2로 해두고, 3개 중 최대를 구함
for i in range(1, n):
    if arr[i-1] <= arr[i]:
        down_cnt += 1
    else:
        down_cnt = 1

    if arr[i] <= arr[i-1]:
        up_cnt += 1
    else:
        up_cnt = 1
    ans = max(ans, down_cnt, up_cnt)

print(ans)
