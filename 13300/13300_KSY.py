# import sys
# sys.stdin = open('input.txt')

N, K = map(int, input().split())   
# N: 수학여행에 참가하는 학생 수
# K: 한 방에 배정할 수 있는 최대 인원 수
boy_student = [0] * 7
girl_student = [0] * 7
room_count = room = 0
for _ in range(N):
    gender, grade = map(int, input().split())   # 성별과 몇 학년인지 받기
    
    if gender == 0: # 여학생이면
        girl_student[grade] += 1    # 여학생 리스트의 학년 인덱스에 1을 더해주자
    else:   # 남학생
        boy_student[grade] += 1
    
# print(girl_student)
# print(boy_student)
# [0, 1, 2, 1, 0, 1, 1]
# [0, 2, 1, 3, 1, 2, 1]

for i in range(7):  # 6학년이여서 7까지 필요
    if girl_student[i] == 0:    # 요소가 0이라면
        room = room     # 방 그대로 유지
    if girl_student[i] % K == 0:    # 요소가 최대인원의 배수라면
        room += (girl_student[i] // K)  # 최대인원으로 나눈 몫 만큼 방 필요
    if girl_student[i] % K != 0:        # 요소가 최대인원의 배수가 아니라면
        room += (girl_student[i] // K) + 1  # 최대인원으로 나눈 몫 +1 만큼 방 필요

    if boy_student[i] == 0: # 남학생 똑같이
        room = room
    if boy_student[i] % K == 0:
        room += (boy_student[i] // K)
    if boy_student[i] % K != 0:
        room += (boy_student[i] // K) + 1
print(room)



