T = int(input()) # 마지막에 곱할거
my_list = []

for i in range(6):

    m, n = map(int, input().split())
    my_list.append(n)

#print(my_list)
biggest_area = 0

for i in range(6):  # 방향 의미 없으니까 그냥 가장 큰 넓이 찾음
    if biggest_area < my_list[i] * my_list[i-1]:
        biggest_area = my_list[i] * my_list[i-1]
        a = i-1  # a에는 현재 인덱스 -1 저장

#print(biggest_area)
#print(a)

b = my_list[a-2] * my_list[a-3]  ## 어차피 빼야 할 값은 a에서 2칸 떨어진 곳 넓이
biggest_area -= b
#print(biggest_area)

print(biggest_area * T)