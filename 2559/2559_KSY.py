# 수열(시간초과)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())    # 전체 날짜의 수, 연속적인 날짜의 수
temp = list(map(int, input().split()))    # 온도를 리스트로 형변환

sum_list = []
# for i in range(N-K+1):  # i가 0부터 10 - 2 + 1 까지
#     sum_list.append(sum(temp[i:i+K]))   # i 부터 i+K 번째까지의 합을 빈 리스트에 추가
# # print(sum_list)

sum_list.append(sum(temp[:K]))
for i in range(N-K):
    sum_list.append(sum_list[i] - temp[i] + temp[i+K])  # 0부터 k 까지 미리 더해놓고 0번 빼고 0+k 번째 더해주기(앞에꺼 빼고 뒤에꺼 더하기)
    
print(max(sum_list))    # 리스트에서 가장 큰 값

