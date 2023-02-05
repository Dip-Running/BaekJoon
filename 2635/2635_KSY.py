num = int(input())

max_list = []   # 길이가 가장 큰 리스트를 받자
for i in range(1, num + 1):     # 첫번째 인덱스는 정해져 있음
    num_list = [num]
    num_list.append(i)          # 두번째 인덱스엔 그냥 다 넣어보자

    idx = 1
    while True:
        next_num = num_list[idx-1] - num_list[idx]  # 다음 정수는 전전에서 전꺼 빼기
        if next_num < 0:    # 만약 뺐는데 음수라면 멈추
            break
        num_list.append(next_num)  # 정수들자을 num_list에 더해주자
        idx += 1    # 인덱스는 1개씩 증가

    if len(max_list) < len(num_list):   # num_list 중에 길이가 가장 큰 리스트를 찾자
        max_list = num_list

print(len(max_list))

for i in range(len(max_list)):
    print(max_list[i], end = ' ')