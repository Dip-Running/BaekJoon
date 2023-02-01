N = int(input())    # 기둥의 개수

a_list = []
for _ in range(N):
    x, y = map(int, input().split())     # y: 높이, x: x좌표
    a_list.append([x,y])                 # x, y 를 이차원 리스트에 배정함   

b_list = sorted(a_list)
# print(b_list)  # x를 기준으로 정렬
M = len(b_list)     # b_list의 갯수

max_list = []
for i in range(len(b_list)):
    max_list.append(b_list[i][1])         # y 값 중 가장 큰 값을 찾자
# print(max_list)  

max = max(max_list)  # 높이가 가장 큰 값 (여기를 기준으로 왼쪽 오른쪽을 보자)
# print(max)

for i in range(M):
    if b_list[i][1] == max:
        max_x = b_list[i][0]      # y 값이 가장 클 때의 x 값
        max_idx = i               # y가 가장 클 때의 인덱스
# print(max_idx)                  # y가 가장 클 때의 인덱스!
        

for i in range(0, max_idx-1):
    if b_list[i][1] >= b_list[i+1][1]:      # 만약에 오른쪽에 있는게 더 작으면 오른쪽거 없애기

        b_list.pop(i+1)
# print(b_list)


# M = 7, max_idx = 4
for i in range(len(b_list)-1, max_idx, -1):
    if b_list[i][1] >= b_list[i-1][1]:      # 만약에 왼쪽에 있는게 더 작으면 왼쪽거 없애기!
        # print(b_list[i][1])
        b_list.pop(i-1)
# print(b_list)                               # 방해되는 기둥 다 지움

area_list = []
for i in range(max_idx-1):
    area_list.append((b_list[i+1][0]-b_list[i][0]) * b_list[i][1])  # 가장 큰 기둥 왼쪽 넓이 구하기
    
area_list.append(b_list[max_idx-1][1])

for i in range(max_idx-1, len(b_list)-1):                               # 가장 큰 기둥 오른쪽 넓이 구하기
    area_list.append((b_list[i+1][0] - b_list[i][0]) * b_list[i+1][1])
    
print(sum(area_list))