# 2309
# import sys
# sys.stdin = open("input.txt", "r")
arr = []
for i in range(9):
    arr.append(int(input()))
# 일단 입력하고
ans = []
for i in range(9):  # 9번 돌면서 하나씩 tmp에 저장하고
    tmp = arr.pop(0)
    for j in range(8):  # 8번 돌면서 하나씩 temp에 저장하고
        temp = arr.pop(0)  # 항상 0번째 인덱스 값 pop
        if sum(arr) == 100:  # 합이 100이면 break
            ans.append(sorted(arr))

        arr.append(temp)  # 합이 100 아니면 temp 다시 추가, append는 맨 뒤에 추가하니까
    arr.append(tmp)  # 하나빼고 한바퀴 돌았는데 없으면 tmp 다시 추가

for i in ans[0]:
    print(i)