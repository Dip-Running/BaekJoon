T = int(input())

for i in range(T):
    ch1_dic = {}  # 애들 딕셔너리 초기화
    ch2_dic = {}
    for j in range(1,5):
        ch1_dic[j] = 0
        ch2_dic[j] = 0

    # 입력
    child1 = list(map(int, input().split()))
    child2 = list(map(int, input().split()))

    for i in child1[1:]:  # dict에 저장
        ch1_dic[i] += 1
    for i in child2[1:]:
        ch2_dic[i] += 1

    for i in range(4,0,-1):
        if ch1_dic[i] > ch2_dic[i]:
            print('A')
            break
        elif ch1_dic[i] < ch2_dic[i]:
            print('B')
            break
    else:
        print('D')

    pass