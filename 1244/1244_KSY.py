N = int(input())   # 스위치 개수
switch = list(map(int, input().split()))    # 스위치 상태 입력 받기
switch.insert(0, 2)     # 0번을 채우고 스위치를 1번 부터 입력하고 싶음 -> 마지막에 제거해야됨 !
# switch: 0~N
students = int(input())  # 학생 수 <= 100

for _ in range(students):
    gender, number = map(int, input().split())  # 성별( 1: 남자, 2: 여자), 번호 <= 스위치 개수

    # 남자인 경우
    if gender == 1:
        for i in range(1, N+1):    # 스위치 개수 +1 만큼 반복
            if i % number == 0: # 스위치의 번호가 배수라면
                if switch[i] == 0:  # 꺼져있는 곳은
                    switch[i] = 1  # 켜기
                else:               # 켜져 있는 곳은
                    switch[i] = 0  # 끄기
        # print(switch)

    # 여자인 경우
    else:
        for j in range(number):
            if 0 <= number + j <= N and 0 <= number - j <= N:     # 범위를 벗어나지 않는 곳에서만
                if switch[number - j] == switch[number + j]:    # 대칭인 요소의 값이 같으면
                    if switch[number - j] == 0:     # 꺼져 있으면
                        switch[number - j] = switch[number + j] = 1     # 켜기
                    elif switch[number - j] == 1:
                        switch[number - j] = switch[number + j] = 0     # 끄기

                else:   # 대칭이 같지 않으면 바로 종료
                    break
# switch.pop(0)   # 0번 제거

# 20개 이상인 경우
for i in range(1, N+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()

# print(*switch)

