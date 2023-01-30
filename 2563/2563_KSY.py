N = int(input())    # 색종이 개수

# 10000칸 중 몇 칸인지 구하기
# 이렇게 하면 중복을 세지 않아도 됨

array = [[0]*100 for _ in range(100)]   # 리스트 100개 안에 100개의 요소를 가진 리스트를 만들자
for _ in range(N):
    x, y = map(int, input().split())    # x, y 받기
    
    for i in range(x, x+10):            # 가로 넓이
        for j in range(y, y+10):        # 세로 넓이
            array[i][j] = 1             # i번째 리스트의 j요소를 1로 바꿈

result = 0
for k in range(100):
    result += array[k].count(1)         # 1이 몇개인지 세자

print(result)
