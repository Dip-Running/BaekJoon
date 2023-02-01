import sys
sys.stdin = open('input2309.txt')

dwarf = []  # 드워프 리스트 생성

for i in range(9):
    dwarf.append(int(input()))

#print(dwarf)
sum_of = sum(dwarf)

for i in range(9):  # 0번째부터
    for one in dwarf[i+1:]:  # 그 뒤 한마리씩 비교하면서
        #print(one, end= ' ')
        if (dwarf[i] + one) == (sum_of - 100):  # 만약 그 두마리 합이 찾아야 할 값과 같으면
            #print(dwarf[i], one)
            a = dwarf[i]
            b = one

dwarf.remove(a)
dwarf.remove(b)

for i in sorted(dwarf):
    print(i)