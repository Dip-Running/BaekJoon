'''
다이내믹 프로그래밍 (DP) 이용
다이내믹 프로그래밍? dp: i 번째까지 왔을 때 최대 길이
d[0]: 증가할 때 d[1]: 감소할 때
dp 는 처음에 모두 1로 세팅

점화식 찾기
d[i] = d[i-1] + 1 (연속하는 경우에만)

이차원 리스트의 최댓값 구하는 방법
max(map(max, 리스트))
'''

N = int(input())    # 수열의 개수
numbers = list(map(int, input().split()))
dp = [[1] * N for _ in range(2)]    # 이차원 리스트
# print(dp) # [[1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1]]

for i in range(1, N):
    if numbers[i-1] <= numbers[i]:  # 증가할 경우
        dp[0][i] = dp[0][i-1] + 1   # 전에꺼에서 1 더하기
    if numbers[i-1] >= numbers[i]:  # 감소할 경우
        dp[1][i] = dp[1][i-1] + 1   # 전에꺼에서 1 더하기

max_number = max(map(max, dp))
print(max_number)

# max_number_1 = max(dp[0])
# max_number_2 = max(dp[1])

# print(max(max_number_1, max_number_2))