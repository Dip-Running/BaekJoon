import sys
sys.stdin = open('input.txt')

w, l = map(int, input().split())   # 가로, 세로
N = int(input()) # 칼로 잘라야 하는 점선의 개수
# rectangle = [[0] * w for _ in range(l)]    # 가로, 세로에 맞춘 이차원 리스트

width = [0, w]
length = [0, l] # 마지막 값을 알려주기 위해 w, l을 넣었

for _ in range(N):
    number, line = map(int, input().split(' '))  # 0: 가로, 1: 세로 // 자르고 싶은 번호
    if number == 0: # 가로를 자르자
        length.append(line)  # 세로 배열에 넣어주기(좌표만 넣는다고 생각)세 -> 세로 배열에서 뚝 끊
    else:   # 세로를 자르자
        width.append(line)     # 가로 배열에 넣어주

    width.sort()
    length.sort()   # 정렬해주면 가로 세로가 정해진

    # print(width, length)
    result = 0
    for i in range(len(length) - 1):
        for j in range(len(width) - 1):
            x = width[j+1] - width[j]   # 자른 조각들의 가로 구하기
            y = length[i+1] - length[i] # 자른 조각들의 세로 구하기
            result = max(result, x*y)
print(result)

