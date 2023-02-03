array = [[0] * 100 for _ in range(100)] # 100 * 100 이차원 리스트에 넓이가 있다면 1로 표시
for _ in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))   # 왼쪽 아래 x, y 오른쪽 위 x, y

    for i in range(x1, x2):
        for j in range(y1, y2):
            array[i][j] = 1     # 직사각형이 있는 칸에 1을 넣어주자
    # print(array)

count = 0
for i in range(100):
    count += array[i].count(1)      # 1이 있는만큼 카운트 세주기

print(count)