# import sys
# sys.stdin = open("input.txt", "r")

N = int(input())
Map = [0] * 1000
# 가장 높은 기둥의 좌표를 중심으로 양쪽 끝에서 모이면서
# 처음 bigger 0 잡아두고
# 해당 좌표가 0이 아닐 때, bigger 보다 해당 좌표 값이 더 크면 bigger 바꾸고
# 한번 좌표 옮길 때마다 Sum += bigger
for i in range(N):
    Locate, Height = map(int, input().split())
    Map[Locate] = Height

Max_index = Map.index(max(Map))
start = 0
bigger = 0
Sum = max(Map)
while start < Max_index:
    if Map[start] != 0:
        if bigger < Map[start]:
            bigger = Map[start]
    start += 1
    Sum += bigger

end = len(Map) - 1
bigger = 0
while end > Max_index:
    if Map[end] != 0:
        if bigger < Map[end]:
            bigger = Map[end]
    end -= 1
    Sum += bigger
print(Sum)
