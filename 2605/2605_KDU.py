import sys
sys.stdin = open('input2605.txt')

n = int(input())
numb_lst = map(int, input().split())


line_lst = []  # 저장할 리스트 생성
count = 1      # 몇번째 인간인지 확인용
for i in numb_lst:
    line_lst.insert(i, count)  # 뽑은 번호 위치에 count번째 인간 삽입함
    count += 1

line_lst.reverse()  # 반대여서 뒤집음

for i in line_lst:
    print(i, end=' ')