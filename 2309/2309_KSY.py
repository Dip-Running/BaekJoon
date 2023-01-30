height_list = []

for i in range(9):
    h = int(input())
    height_list.append(h)
# print(height_list) # [20, 7, 23, 19, 10, 15, 25, 8, 13]
sub = sum(height_list) - 100    # 40

# 2개 합 40 찾기 -> 36개
first = 0   # 초기값 0 설정
second = 0

for i in range(9):
    for j in range(i+1, 9): # first 보다 뒤에 있는 값이 필요
        if height_list[i] + height_list[j] == sub:  # 더해서 40이면
            first = height_list[i]      # first 에 i 할당
            second = height_list[j]     # second 에 j 할당
            break                       # 하나씩만 찾고 멈추기

height_list.remove(first)       # first 리스트에서 삭제
height_list.remove(second)     
            
# print(height_list)
# new_height = ''.join([str(n) for n in height_list])

height_list.sort()  # 오름차순으로 정렬하기

for h in height_list:
    print(h)




            

