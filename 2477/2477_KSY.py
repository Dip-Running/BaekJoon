#참외밭
N = int(input())    # 1m^2에 자라는 참외의 개수

hexagon_list = []
for _ in range(6):  # 육각형
    a, b = list(map(int, input().split()))
    hexagon_list.append([a, b])
# print(hexagon_list)

width = []  # 가로: 1,2
length = [] # 세로: 3,4
for list in hexagon_list:
    if list[0] == 3 or list[0] == 4:    # 3 또는 4는 세로를 결정하는 숫자
        length.append(list[1])          # 길이를 모두 세로 리스트에 추가
        max_length = max(length)            # 세로 길이가 가장 긴 것
        min_length = min(length)            # 세로 길이가 가장 짧은 것

    if list[0] == 1 or list[0] == 2:        # 1 또는 2는 가로를 결정
        width.append(list[1])           # 길이를 모두 가로 리스트에 추가
        max_width = max(width)          # 가로 길이가 가장 긴 것
        min_width = min(width)          # 가로 길이가 가장 짧은 것

area = (max_length * max_width) - (min_length * min_width)
# print(max_length, max_width, min_length, min_width)
# print(area)
print(area * N)