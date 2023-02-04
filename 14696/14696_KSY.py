# import sys
# sys.stdin = open('input.txt')

N = int(input())    # 총 라운드 수
# 별: 4, 동그라미: 3, 네모: 2, 세모: 1
for _ in range(N):
    a_figure = list(map(int, input().split()))    # list[0]: A가 낸 딱지의 그림의 개수, 그림의 모양(4니까 별 -> 별 1개)
    b_figure = list(map(int, input().split()))    

    a_shape_list = [0] * 5
    b_shape_list = [0] * 5
    for i in range(1, len(a_figure)):
        a_shape_list[a_figure[i]] += 1
    # print(a_shape_list) # 모양별로 몇 개씩 있는지 세주기
    b_shape_list = [0] * 5
    for i in range(1, len(b_figure)):
        b_shape_list[b_figure[i]] += 1

    if a_shape_list[4] > b_shape_list[4]:
        print('A')
        continue
    if a_shape_list[4] < b_shape_list[4]:
        print('B')
        continue
    else:   # 별의 개수가 똑같으면
        if a_shape_list[3] < b_shape_list[3]:   # 동그라미 개수 확인
            print('B')
            continue
        elif a_shape_list[3] > b_shape_list[3]:
            print('A')
            continue
        else:
            if a_shape_list[2] < b_shape_list[2]:
                print('B')
                continue
            elif a_shape_list[2] > b_shape_list[2]:
                print('A')
                continue
            else: 
                if a_shape_list[1] < b_shape_list[1]:
                    print('B')
                    continue
                elif a_shape_list[1] > b_shape_list[1]:
                    print('A')
                    continue
                else:
                    print('D')


