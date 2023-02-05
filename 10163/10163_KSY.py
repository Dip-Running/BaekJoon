# 색종이
import sys
sys.stdin = open('input.txt')
N = int(input())    # 색종이 장수
'''
1번 색종이는 1로 표시 '1'-> 안 가린 건 1 인 곳
2번 색종이는 2로 표시 '2~3'-> 2번 색종이가 1번 색종이 위로 가면 3이됨 -> 3번 색종이가 안 가린 건 2, 1번 색종이를 가렸는데 3번 색종이가 안 가렸으면 3
3번 색종이는 4로 표시 '4~7'-> 3번 색종이가 1번 가리면 4, 2번 가리면 5 
4번 색종이는 8로 표시 '8~15'-> 최대: 1번 위 2번 위 3번 위 4번: 15, 최소:8
'''
color_paper = [[0] * 1000 for _ in range(1000)]
for n in range(N):
    x, y, width, length = map(int, input().split())  # 색종이 정보 리스트로 받기
    # (0,0) 가로, 세로
    for i in range(x, x + width):
        for j in range(y, y + length):
            color_paper[i][j] += 2 ** n
# print(color_paper)     # 2의 제곱수로 2차원 리스트 표현
    '''
    내가 지금 하고 싶은 것!!
    1인곳은 1번 색종이
    2~3인 곳은 2번 색종이
    4~7인 곳은 3번 색종이
    8~15인 곳은 4번 색종이
    '''

count = [0] * N
for lst in color_paper:
    for i in range(N):
        for j in range(2**i, 2**(i+1)):
            count[i] += lst.count(j)

for i in range(len(count)):
    print(count[i])

