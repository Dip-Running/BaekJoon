# import sys
# sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
arr = list(map(int, input().split()))
Sum = sum(arr[0:K])
ans = Sum
for i in range(1, N-K+1):
    Sum -= arr[i-1]
    Sum += arr[i+(K-1)]
    if ans < Sum:
        ans = Sum

print(ans)