import sys
sys.stdin = open("input.txt","rt")
# ====================================
import sys
width, height = map(int,input().split())
n = int(input())
store = []

def calcDist(dir,dist): # 왼쪽 위부터 시계방향으로 좌표까지 거리를 측정해서 리턴
    if dir == 1:    # 북쪽일 경우 dist만큼이 끝임
        return dist
    elif dir == 2:  # 남쪽일 경우 가로 쭉, 세로 쭉, 오른쪽 아래 끝에서 좌표까지
        return width + height + (width - dist)  # 그래서 width - dist
    elif dir == 3:  # 동쪽일 경우 가로쭉 세로 쭉 아래 가로 쭉 왼쪽 아래 끝에서 좌표까지
        return width + height + width + (height - dist) # 그래서 height - dist
    else:           # 서쪽일 경우 가로쭉 그리고 내려온 거리 만큼 = dist
        return width + dist

for _ in range(n+1):
    if _ == n:  # n번째에는 동근이 좌표
        direction, distance = map(int,input().split())
    else:       # 나머지는 가게 좌표
        store.append(list(map(int,input().split())))
print(store, direction, distance)
total = 0
dist1 = calcDist(direction, distance) #동근이의 거리
print(dist1)
for i in range(n): # 이게 문제임
    dist2 = calcDist(store[i][0], store[i][1]) #각 상점의 거리
    path1 = abs(dist1 - dist2)  # 시계방향으로 돌았을 때 거리 절댓값
    path2 = 2 * width + 2 * height - path1  # 반시계 방향으로 돌았을 때 거리
    # print(path1, path2)
    total += path1 if path1 < path2 else path2  # 작은거 추가

print(total)