students = int(input()) # 학생 수
number_list = list(map(int, input().split()))   # 줄은 선 차례대로 뽑은 번호

# list 에서 index[i] 는 0 ~ i 까지 뽑을 수 있음

student_list = []   # 최종적으로 줄을 선 순서를 담을 빈 리스트

for i in range(len(number_list)):
    student_list.insert((i-number_list[i]), (i+1))  # (원래 index - 자기가 뽑은 인덱스 값) 자리에 (index + 1) 값을 넣자
    # print((i-number_list[i]))   

result = ' '.join([str(n) for n in student_list])   # 리스트 값을 문자열로 출력하기
print(result)

    